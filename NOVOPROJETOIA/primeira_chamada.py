import os 
import requests 
from dotenv import load_dotenv

load_dotenv

apui_key = os.getenv("OPEN_API_KEY")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}", 
    "Content-Type": "application/json"
}

body = {
    "model": "gpt-4o-mini"
    "messages": [
        {"role": "user", "content": "Explique o que é Python em 1 frase"}
    ],
}

resposta = requests.post(url, headers=headers, json=body)
dados = resposta.json()

print(dados)

print(dados["choices"])
#com 1 item

print(dados["choices"] [0] ["message"] ["content"])
#mostra o priemiro e o unico item da lista em um dicionario 

resposta = dados["choices"] [0] ["message"] ["content"]