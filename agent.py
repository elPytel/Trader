from langchain.prompts import PromptTemplate
from langchain.agents import Tool
from localOllamaLLM import *
from StrictOutputParser import *

class Agent():
    """Agent pro zpracování dotazů pomocí LLM a nástrojů.
    """

    def __init__(self, llm: OllamaLLM, prompt: PromptTemplate):
        """Inicializace agenta s LLM a parserem výstupu.
        """
        self.llm = llm
        self.prompt = prompt

class Memory():
    """Jednoduchá paměť pro agenta, která uchovává scratchpad."""
    def __init__(self):
        self.scratchpad = []
    
    def add_observation(self, observation: str):
        """Přidá pozorování do scratchpadu."""
        self.scratchpad.append(observation)

    def get_scratchpad(self) -> str:
        """Vrátí celý scratchpad jako text."""
        return "\n".join(self.scratchpad)

class MyAgentExecutor():
    def __init__(self, agent: Agent, output_parser: AgentOutputParser, memory: Memory = None, tools: list[Tool] = [], logging: bool = True):
        self.agent = agent
        self.output_parser = output_parser
        self.tools = tools
        self.logging = logging

    def _process_step(self, inputs: dict) -> tuple:
        """Zpracuje vstup a vrátí (action, thought)."""
        prompt_text = self.agent.prompt.format(
            input=inputs["input"],
            tools=inputs["tools"],
            agent_scratchpad=inputs["agent_scratchpad"],
            last_thought=inputs.get("last_thought", "")
        )
        response = self.agent.llm.invoke(prompt_text)
        if self.logging:
            output = response.strip()
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write("INPUT:\n" + prompt_text + "\n")
                f.write("OUTPUT:\n" + output + "\n")
                f.write("-" * 80 + "\n")
        
        last_thought = self.output_parser.get_last_thought(response)
        return self.output_parser.parse(response), last_thought

    def execute(self, inputs: dict) -> str:
        """Spouští agenta, dokud nedojde k finální odpovědi. Ukládá last_thought."""
        while True:
            action, last_thought = self._process_step(inputs)
            inputs["last_thought"] = last_thought
            if isinstance(action, AgentFinish):
                return action.return_values["output"]
            elif isinstance(action, AgentAction):
                tool_output = next((tool.func(action.tool_input) for tool in self.tools if tool.name == action.tool), None)
                if tool_output is None:
                    inputs["agent_scratchpad"] += f"\nObservation: {action.tool}({action.tool_input}) = Error: Tool not found!\n"
                else:
                    inputs["agent_scratchpad"] += f"\nObservation: {action.tool}({action.tool_input}) = {tool_output}\n"
            else:
                raise ValueError(f"Unexpected output type: {type(action)}")