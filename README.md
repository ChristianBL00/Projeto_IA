# Avaliação Técnica - Contraturno IA

**Lista** mesclada cobrindo o que foi estudado: Python base, API/Groq, .env, chat com memória, prompt de sistema,
arquivo de contexto e Streamlit.

---

## Questão 1 — Objetiva
```bash
No Python, o que a função input() sempre devolve?
A. Um número inteiro
B. Um booleano (True/False) 
C. Uma string (texto) - Opção correta
D. Uma lista
```
---

## Questão 2 — Justificativa
```bash
A API key deve ficar no arquivo .env para garantir a segurança do projeto e a separação de configurações do código-fonte.
Isso evita que credenciais sensíveis sejam compartilhadas acidentalmente ao enviar o código para repositórios públicos como o GitHub.
Se a chave for exposta, hackers podem usá-la para consumir seus dados pessoais de forma indevida.
```
---

## Questão 3 — Objetiva
```bash
  Observe o trecho:
  historico = [
 {"role": "system", "content": "Você é um tutor."},
  {"role": "user", "content": "Oi"},
 ]
O que historico é?
A. Uma string
B. Uma lista de dicionários - Opção correta
C. Um número
D. Uma função
```
---

## Questão 4 — Código (completar)
```bash
Complete o código abaixo para que o programa some números até a pessoa digitar 0, e no final imprima a soma.
total = 0
while True:
 n = int(input("Número (0 para sair): "))
 if n == 0:
 break  
 total += n  
print(f"Soma: {total}")
```
---

## Questão 5 — Justificativa + conceito
```bash
Na aula do chat sem histórico, se a pessoa digita:
1. Meu nome é Ana
2. Qual é o meu nome?
o modelo costuma não lembrar.
a. Por que isso acontece? (2–4 linhas)
Porque o modelo não possui memória automática entre as mensagens. Sem histórico, ele recebe apenas a mensagem atual e não consegue recuperar informações anteriores.

b. O que mudamos no código para o modelo passar a lembrar? Cite a estrutura de dados usada.
Adicionamos uma estrutura de dados chamada lista, que armazena o histórico das mensagens e o envia junto com a nova pergunta, permitindo que o modelo consulte as informações anteriores.
```
---
## Questão 6 — Objetiva (API / JSON)
```bash
Depois de uma chamada bem-sucedida à API (status 200), o texto da resposta fica em:
dados["choices"][0]["message"]["content"]
O que significa o [0] nesse caminho?
A. É o nome do modelo
B. Pega o primeiro item da lista choices - Opção correta
C. É a API key
D. Apaga a mensagem do usuário
```
---
## Questão 7 — Código (escrever)
```bash
Escreva uma função carregar_contexto(caminho="contexto.txt") que:
1. Abre o arquivo com encoding="utf-8"
2. Lê o conteúdo e devolve a string (com .strip())
3. Se o arquivo não existir, imprime um aviso e devolve "" (string vazia)
Não precisa limitar o tamanho do arquivo.

def carregar_contexto(caminho: str = "contexto.txt") -> str:
    try:
        with open(caminho, encoding="utf-8") as arquivo:
            texto = arquivo.read().strip()
    except FileNotFoundError:
        print(f"Aviso: arquivo '{caminho}' não encontrado. Seguindo sem contexto.")
        return ""
```
---
## Questão 8 — Código + justificativa
(Streamlit / projeto)
```bash
a. Código: Complete o trecho do Streamlit para guardar o histórico entre cliques:
import streamlit as st
if "historico" not in st.session_state:
    st.session_state.historico = []
pergunta = st.chat_input("Digite...")
if pergunta:
 st.session_state.historico.append({"role": "user", "content": pergunta})

b. Justificativa: Em 2–4 linhas, explique por que, no Streamlit, usamos st.session_state em vez de uma
variável comum historico = [].
Usamos st.session_state porque o Streamlit executa o código novamente a cada interação. Uma variável comum perde seu valor nessas atualizações, enquanto o session_state mantém os dados durante a sessão, preservando o histórico de mensagens.
```
