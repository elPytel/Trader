import requests
import json

while True:
    user_input = input("👤 Vy: ")
    if user_input.lower() == 'exit':
        break

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": user_input,
                "stream": False
            }
        )
        response.raise_for_status()
        data = response.json()

        if 'response' in data:
            print(f"🤖 AI: {data['response']}")
        else:
            print("❌ Chyba: Odpověď neobsahuje klíč 'response'.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Chyba při komunikaci: {e}")
    except json.JSONDecodeError:
        print("❌ Chyba při dekódování JSON odpovědi.")

