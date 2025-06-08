from langchain.agents.agent import AgentOutputParser
from langchain.schema import AgentAction, AgentFinish
import re

# --- Vlastní parser pro výstup LLM ---
class StrictOutputParser(AgentOutputParser):
    def get_last_thought(self, text: str) -> str:
        """
        Extrahuje pouze první řádek po "Thought:" (tj. samotnou myšlenku, ne další řádky).
        Pokud není myšlenka nalezena, vrací prázdný řetězec.
        """
        # Najdi "Thought:" a vezmi jen první řádku po něm (ignoruj další řádky)
        thought_match = re.search(r"Thought:\s*(.*)", text)
        if thought_match:
            # Rozděl podle nového řádku a vezmi jen první část
            return thought_match.group(1).splitlines()[0].strip()
        return ""
    
    def get_final_answer(self, text: str) -> str:
        """
        Extrahuje text po "Final Answer:".
        Pokud není Final Answer nalezena, vrací prázdný řetězec.
        """
        final_answer_match = re.search(r"Final Answer:\s*(.*)", text, re.DOTALL)
        if final_answer_match:
            return final_answer_match.group(1).strip()
        return ""
    
    def get_action_and_input(self, text: str) -> tuple[str, str]:
        """
        Extrahuje název akce a vstup z textu.
        Pokud není akce nalezena, vrací prázdný řetězec pro akci a vstup.
        """
        """
        # Akceptuje i variantu bez "Thought:" a různé varianty Action Input
        # 1. Action: get_stock_price\n   Action Input: AAPL
        # 2. Action: get_stock_price('AAPL')
        # 3. Action: get_stock_price("AAPL")
        # 4. Action: get_stock_price\n   Action Input: 'AAPL'
        # 5. Action: get_stock_price\n   Action Input: "AAPL"
        # 6. Action: get_stock_price\n   Action Input: AAPL
        # 7. Action: None
        # 8. Action: get_stock_price
        # 9. Action: get_stock_price()
        # 10. Action: get_stock_price
        # 11. Action: get_stock_price('AAPL', ...)
        # 12. Action: get_stock_price: AAPL
        # 13. Action: get_stock_price - AAPL
        # 14. Action: get_stock_price = AAPL
        """
        # Nejprve zkusit formát s Action Input
        pattern = re.compile(
            r"Action:\s*(\w+)\s*^ *Action Input:\s*['\"]?([^'\"]+)['\"]?",
            re.MULTILINE | re.IGNORECASE
        )
        match = pattern.search(text)
        if match:
            tool = match.group(1).strip()
            raw_input = match.group(2).strip()
            # Zpracuj vstup: rozděl podle čárek, odstraň uvozovky a mezery
            if "," in raw_input:
                args = [arg.strip().strip("'\"") for arg in raw_input.split(",")]
                tool_input = args if len(args) > 1 else args[0]
            else:
                tool_input = raw_input.strip("'\"")
            return tool, tool_input
        # fallback: Action: get_stock_price('AAPL')
        pattern2 = re.compile(
            r"Action:\s*(\w+)\s*^ *Action Input:\s*(.*)",
            re.IGNORECASE
        )
        match2 = pattern2.search(text)
        if match2:
            tool = match2.group(1).strip()
            raw_input = match2.group(2).strip()
            if raw_input:
                args = [arg.strip().strip("'\"") for arg in raw_input.split(",")]
                tool_input = args if len(args) > 1 else args[0]
            else:
                tool_input = ""
            return tool, tool_input

        return "", ""

    def parse(self, text: str) -> AgentAction | AgentFinish:
        
        text = text.strip()
        # Pokud je přítomen Final Answer, vždy jej preferuj
        if "Final Answer:" in text:
            final_answer_match = self.get_final_answer(text)
            if final_answer_match:
                return AgentFinish(
                    return_values={"output": final_answer_match},
                    log=text,
                )
        # Pokud je Action: None, ignoruj Action a hledej Final Answer
        action_none_match = re.search(r"Action:\s*None", text, re.IGNORECASE)
        if action_none_match:
            final_answer_match = self.get_final_answer(text)
            if final_answer_match:
                return AgentFinish(
                    return_values={"output": final_answer_match},
                    log=text,
                )
            # Pokud není Final Answer, prostě ignoruj Action: None
            raise ValueError(f"Cannot parse output: {text}")
        # Nejprve zkusit formát s Action Input (včetně více argumentů oddělených čárkou)
        tool, tool_input = self.get_action_and_input(text)
        if tool and tool_input is not None:
            return AgentAction(tool=tool, tool_input=tool_input, log=text)
        raise ValueError(f"Cannot parse output: {text}")