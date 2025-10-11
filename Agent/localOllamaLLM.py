from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import requests
import json

LOG_FILE = "llm_debug.log"

# --- Vlastní třída OllamaLLM ---
class OllamaLLM(LLM):
    temperature: float = 0.0
    model: str = "mistral"
    api_url: str = "http://localhost:11434/api/generate"
    system_instructions: str = ""  # nebo úplně odstraň tento atribut

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        full_prompt = self.system_instructions + prompt
        response = requests.post(
            self.api_url,
            json={
                "model": self.model,
                "prompt": full_prompt,
                "temperature": self.temperature,
                "stream": True,
                "stop": stop
            },
            stream=True
        )

        if response.status_code != 200:
            raise ValueError(f"Error from Ollama API: {response.status_code} - {response.text}")

        output = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                output += data.get("response", "")
        
        return output

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"model": self.model}

    @property
    def _llm_type(self) -> str:
        return "ollama"