import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./Data/perfil_cliente.json'))
transacoes = pd.read_csv('./Data/transacoes.csv')
historico = pd.read_csv('./Data/historico_atendimento.csv')
produtos = json.load(open('./Data/programas_consultoria.json'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['ramo_de_atividade']}
OBJETIVO: {perfil['objetivo_principal']}


TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT (Definição da Variável) ============
# ============ SYSTEM PROMPT ============
# O texto PRECISA estar entre aspas triplas para o Python entender que é apenas texto
SYSTEM_PROMPT = '''
Você é o Edem, um consultor de controladoria e finanças corporativas.

OBJETIVO:
Analisar os dados enviados do cliente, ponderando diagnóstico e objetivo, a fim de fazer recomendações de melhoria.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema ensino de consultoria em gestão financeira;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
'''''

# ============ MONTAR CONTEXTO ============
contexto = f'''
CLIENTE: {perfil.get('nome', 'N/A')}, {perfil.get('idade', 'N/A')} anos
RAMO: {perfil.get('ramo_de_atividade', 'N/A')}
OBJETIVO: {perfil.get('objetivo_principal', 'N/A')}

TRANSAÇÕES RECENTES:
{transacoes.head(10).to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.head(5).to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
'''

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"{SYSTEM_PROMPT}\n\nCONTEXTO DO CLIENTE:\n{contexto}\n\nPergunta: {msg}"
    
    try:
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
        dados = r.json()
        
        # Verificando se 'response' realmente existe antes de acessar
        if 'response' in dados:
            return dados['response']
        else:
            # Se der erro, o Ollama costuma enviar o motivo no campo 'error'
            erro_ollama = dados.get('error', 'Resposta desconhecida')
            return f"O Ollama respondeu com um erro: {erro_ollama}"
            
    except Exception as e:
        return f"Erro técnico na chamada: {e}"

# ============ INTERFACE STREAMLIT ============
st.title("🎓 Edem, o Consultor Virtual")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)