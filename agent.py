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
    
    def clear(self):
        """Vymaže scratchpad."""
        self.scratchpad = []

class MyAgentExecutor():
    def __init__(self, agent: Agent, output_parser: AgentOutputParser, memory: Memory = Memory(), tools: list[Tool] = [], logging: bool = True):
        self.agent = agent
        self.output_parser = output_parser
        self.tools = tools
        self.logging = logging
        self.memory = memory

    def _process_step(self, inputs: dict) -> tuple:
        """Zpracuje vstup a vrátí (action, thought)."""
        prompt_text = self.agent.prompt.format(
            input=inputs["input"],
            tools=inputs["tools"],
            agent_scratchpad=self.memory.get_scratchpad(),
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
                # Pokud je tool_input seznam (více argumentů), rozbal je při volání funkce
                tool_output = None
                for tool in self.tools:
                    if tool.name == action.tool:
                        if isinstance(action.tool_input, list):
                            tool_output = tool.func(*action.tool_input)
                        else:
                            tool_output = tool.func(action.tool_input)
                        break
                if tool_output is None:
                    self.memory.add_observation(f"Observation: {action.tool}({action.tool_input}) = Error: Tool not found!")
                else:
                    self.memory.add_observation(f"Observation: {action.tool}({action.tool_input}) = {tool_output}")
            else:
                raise ValueError(f"Unexpected output type: {type(action)}")