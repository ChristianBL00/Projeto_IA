import os
from dotenv import load_dotenv

load_dotenv

apui_key = os.getenv("OPEN_API_KEY")

if api_key:
    print("Key carregada!")
else: 
    print("Key deu ruim :/")