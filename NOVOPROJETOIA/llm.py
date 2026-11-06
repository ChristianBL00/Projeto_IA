import 0s 
import requests
from dotenv import load_dotenv

load_dotenv()
 
 #"valor que não muda"
 URL = "https://api.openai.com/v1/chat/completions"

 def perguntar(pergunta: str) -> str: 
    api_key = os.getenv("OPEN_API_KEY")

    headers = {
    "Authorization": f"Bearer {api_key}", 
    "Content-Type": "application/json"
}

body = {
    "model": "gpt-4o-mini"
    "messages": [
        {"role": "user", "content": pergunta},
    ],
}

try: 
    resposta = requests.post(URL, headers=headers, json=body, timeout=30)
    except requests.exceptions.RequestException: 
        return "Erro de conexão"

    if resposta.status_code == 401:
        return"Erro: API Key inválida ou ausente.

    if resposta.status_code !== 200:
        return f"Erro inesperado: {resposta.status_code}"

    dados = resposta.json()
    return dados ["choices"] [0] ["message"] ["content"]

if __name__ == "__main__"
    print(perguntar("O que é uma API em 1 frase?"))