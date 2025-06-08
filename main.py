import yfinance as yf

from localOllamaLLM import *
from StrictOutputParser import *
from agent import *

# --- Definice nástroje ---
import yfinance as yf

def get_stock_price(ticker: str) -> str:
    """
    Retrieve the current stock price for a given ticker symbol. Example: get_stock_price('AAPL')

    Arguments:
        ticker -- Ticker symbol of the stock (e.g., 'AAPL' for Apple Inc.)

    Returns:
        A string with the current stock price formatted to two decimal places.
        The price is in USD and represents the regular market price.
        If the price cannot be found, returns an error message.
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
    
def convert_money(amount: float, from_currency: str, to_currency: str) -> str:
    """
    Convert an amount from one currency to another using the current exchange rate.
    
    Arguments:
        amount -- The amount to convert.
        from_currency -- The currency code of the original amount (e.g., 'USD').
        to_currency -- The currency code to convert to (e.g., 'EUR').
    
    Returns:
        A string with the converted amount formatted to two decimal places.
        If the conversion fails, returns an error message.
    """
    try:
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        if from_currency == to_currency:
            return f"{amount:.2f} {to_currency}"
        
        # Použijeme yfinance pro získání aktuálního kurzu
        ticker = f"{from_currency}{to_currency}=X"
        stock = yf.Ticker(ticker)
        rate = stock.info.get("regularMarketPrice")
        
        if rate is None:
            return f"Exchange rate for {from_currency} to {to_currency} not found."
        
        converted_amount = amount * rate
        return f"{converted_amount:.2f} {to_currency}"
    except Exception as e:
        return f"Chyba: {e}"

def get_traded_shares(exchange: str = "NASDAQ") -> list:
    """
    Retrieve a list of traded shares on a specified stock exchange.
    Arguments:
        exchange -- The stock exchange to retrieve shares from. Supported values are 'NASDAQ', 'NYSE', 'AMEX'.
    Returns:
        A list of ticker symbols for the traded shares on the specified exchange.
        Raises ValueError if the exchange is not supported.
    """
    import pandas as pd
    exchange = exchange.upper()
    if exchange not in {"NASDAQ", "NYSE", "AMEX"}:
        raise ValueError("Podporované hodnoty exchange jsou: 'NASDAQ', 'NYSE', 'AMEX'.")

    url = "https://old.nasdaq.com/screening/companies-by-name.aspx?exchange={}&render=download"
    df = pd.read_csv(url.format(exchange))
    return df['Symbol'].dropna().tolist()
    
stock_tools = [
    Tool(
        func=get_stock_price,
        name=get_stock_price.__name__,
        description=get_stock_price.__doc__,
    ),
    Tool(
        func=convert_money,
        name=convert_money.__name__,
        description=convert_money.__doc__,
    )
]

# --- Prompt pro agenta ---
prompt_template = """
You are an agent that must strictly follow the output format below.
Your name is "Karel" and you are a helper agent that can answer questions about stock prices and traded shares,
or 
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
- After using a tool, WAIT for the tool result before giving the Final Answer.
- Do NOT output anything except exactly one of the formats above.
- Do NOT output Markdown or any extra text.

Respond with exactly one format, and nothing else.

If you used a tool in your last response, you must wait for the tool result before giving the Final Answer.
The tool result will be provided in the next step as an observation in the agent scratchpad below.
If you know the answer without using a tool, you can give the Final Answer directly.
If you get all the information you need from the tool result, you can give the Final Answer.

If the user is chatting with you, and you dont need to use a tool, you can give the Final Answer directly
as the response to the user.
- Do not outout Action or Action Input in this case.

User may speak to you in Czech, so you must understand and respond in Czech.

You have access to the following tools:
{tools}

Agent scratchpad:
{agent_scratchpad}

Last thought:
{last_thought}

USER PROMPT: {input}
"""


prompt = PromptTemplate(
    input_variables=["input", "tools", "agent_scratchpad", "last_thought"],
    template=prompt_template
)

# --- Inicializace agenta ---
llm = OllamaLLM(temperature=0)

agent = Agent(
    llm=llm, 
    prompt=prompt
)

agent_executor = MyAgentExecutor(
    agent=agent,
    output_parser=StrictOutputParser(),
    tools=stock_tools
)

# remove the debug log file if it exists
import os
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

# Hlavní funkce pro spuštění agenta
def run():
    print("AI agent běží. Napiš 'exit' pro ukončení.")
    tools_str = "\n".join(
        f"{tool.name}: \n    {tool.description}" for tool in stock_tools
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
            "agent_scratchpad": agent_scratchpad,
            "last_thought": ""
        }

        try:
            response = agent_executor.execute(inputs)
            print("Agent:", response)
        except Exception as e:
            print("Chyba:", e)


if __name__ == "__main__":
    run()