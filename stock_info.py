import yfinance as yf
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.schema import AgentAction, AgentFinish
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents.agent import AgentOutputParser
import re

from localOllamaLLM import *

# --- Definice nástroje ---
import yfinance as yf

def get_stock_price(ticker: str) -> str:
    """
    Retrieve the current stock price for a given ticker symbol. Example: get_stock_price('AAPL')
    """
    try:
        ticker = ticker.strip().strip("'\"")
        stock = yf.Ticker(ticker)
        # Zkus použít history jako zálohu, pokud info selže
        price = stock.info.get("regularMarketPrice")
        if price is None:
            data = stock.history(period="1d")
            if not data.empty and "Close" in data:
                price = float(data["Close"].iloc[-1])
            else:
                return f"Price for {ticker} not found."
        return f"{price:.2f}"
    except Exception as e:
        return f"Chyba: {e}"

stock_tool = Tool(
    name="get_stock_price",
    func=get_stock_price,
    description=get_stock_price.__doc__,
)

# --- Vlastní parser pro výstup LLM ---
class StrictOutputParser(AgentOutputParser):
    def parse(self, text: str) -> AgentAction | AgentFinish:
        text = text.strip()
        if text.startswith("Final Answer:"):
            return AgentFinish(
                return_values={"output": text[len("Final Answer:"):].strip()},
                log=text,
            )
        # Opravený tolerantní regex na různé varianty Action Input
        pattern = re.compile(
            r"Thought:\s*(.*?)\s*^ *Action:\s*(.*?)\s*^ *Action Input:\s*(.*)",
            re.DOTALL | re.MULTILINE | re.IGNORECASE
        )
        match = pattern.search(text)
        if not match:
            # fallback: zkusit Action a Action Input na jednom řádku (např. Action: get_stock_price('TSLA'))
            pattern2 = re.compile(
                r"Thought:\s*(.*?)\s*^ *Action:\s*(\w+)\((.*?)\)",
                re.DOTALL | re.MULTILINE | re.IGNORECASE
            )
            match2 = pattern2.search(text)
            if match2:
                thought = match2.group(1).strip()
                tool = match2.group(2).strip()
                tool_input = match2.group(3).strip().strip("'\"")
                return AgentAction(
                    tool=tool,
                    tool_input=tool_input,
                    log=text,
                )
            raise ValueError(f"Cannot parse output: {text}")
        thought = match.group(1).strip()
        tool = match.group(2).strip()
        tool_input = match.group(3).strip().strip('"').strip("'")
        return AgentAction(
            tool=tool,
            tool_input=tool_input,
            log=text,
        )

# --- Prompt pro agenta ---
prompt_template = """
You are an agent that must strictly follow the output format below.
You MUST respond in exactly one of these two formats, and NEVER include both in the same response.
If you need to use a tool, ONLY output the tool format and do NOT include any answer, observation, or commentary.
If you are ready to answer, ONLY output the final answer format.

Format 1: (for tool use, do NOT answer yet)
Thought: <your thought>
Action: <tool name>
Action Input: <input>

Format 2: (for final answer, ONLY after tool result)
Final Answer: <your answer>

STRICT RULES:
- NEVER output both Action and Final Answer in the same response.
- NEVER output 'Observation', 'Action Observation', or any commentary.
- After using a tool, WAIT for the tool result before giving the Final Answer.
- Do NOT output anything except exactly one of the formats above.
- Do NOT output Markdown or any extra text.

Respond with exactly one format, and nothing else.

You have access to the following tools:
{tools}

Agent scratchpad:
{agent_scratchpad}

USER PROMPT: {input}
"""

prompt = PromptTemplate(
    input_variables=["input", "tools", "agent_scratchpad"],
    template=prompt_template
)

# --- Inicializace agenta ---
llm = OllamaLLM(temperature=0)

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
)

llm_agent = LLMSingleActionAgent(
    llm_chain=llm_chain,
    output_parser=StrictOutputParser(),
    stop=["\nObservation:"],
    allowed_tools=["get_stock_price"],
)

agent = AgentExecutor.from_agent_and_tools(
    agent=llm_agent,
    tools=[stock_tool],
    verbose=True,
    handle_parsing_errors=True,
)

# remove the debug log file if it exists
import os
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

# Hlavní funkce pro spuštění agenta
def run():
    print("AI agent běží. Napiš 'exit' pro ukončení.")
    tools_str = "\n".join(
        f"{tool.name}: \n    {tool.description}" for tool in [stock_tool]
    )
    agent_scratchpad = ""
    while True:
        query = input("Ty: ")
        if query.lower() == "exit":
            break
        # Vstup pro agenta
        inputs = {
            "input": query,
            "tools": tools_str,
            "agent_scratchpad": agent_scratchpad
        }

        try:
            response = agent.run(inputs)
            print("Agent:", response)

            # Po zavolání toolu přidej jeho výstup do scratchpadu (simulace LangChain agenta)
            agent_scratchpad += f"\nObservation: {response}\n"
        except Exception as e:
            print("Chyba:", e)


if __name__ == "__main__":
    run()