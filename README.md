# 🏦 Edem - Consultor Virtual de Controladoria & Finanças

> Agente de IA Generativa especializado em consultoria empresarial e financeira. O Edem transforma dados brutos em inteligência estratégica, auxiliando na tomada de decisão de forma segura e local.

## 💡 O Que é o Edem?

O **Edem** (Evolutionary Data & Enterprise Management) é um consultor virtual desenvolvido para apoiar gestores e empreendedores. Diferente de chats genéricos, o Edem aplica conceitos de **controladoria e finanças empresariais** para analisar o cenário do negócio, identificar gargalos e sugerir caminhos estratégicos baseados em dados reais.

**O que o Edem faz:**
- ✅ **Análise de Controladoria:** Interpreta DREs, Balanços e Fluxos de Caixa.
- ✅ **Consultoria Empresarial:** Explica indicadores como EBITDA, ROI e Margem de Contribuição.
- ✅ **Ciência de Dados Aplicada:** Transforma arquivos CSV/JSON em insights de negócio.
- ✅ **Segurança Total:** Roda 100% localmente, garantindo que dados sigilosos da empresa não saiam do ambiente controlado.

---

## 🏗️ Arquitetura do Sistema

```mermaid
flowchart TD
    A[Usuário/Gestor] --> B[Interface Streamlit]
    B --> C[Ollama - Processamento Local]
    C --> D[Base de Conhecimento de Controladoria]
    D --> C
    C --> E[Insights e Relatórios Estratégicos]
Stack Técnica:

Interface: Streamlit (Dashboard Interativo)

Cérebro (LLM): Ollama (Modelo local llama3 ou mistral)

Linguagem: Python (Pandas para manipulação de dados financeiros)

🚀 Como Executar o Edem
1. Configurar o Ambiente de IA (Ollama)
Certifique-se de ter o Ollama instalado e rodando o modelo de sua preferência:

Bash

ollama pull llama3
2. Instalar Dependências
Bash

pip install streamlit pandas requests openpyxl
3. Iniciar a Consultoria
Bash

streamlit run src/edem_app.py
📊 Diferenciais Estratégicos
Visão de Especialista: Diferente de IAs comuns, o Edem foi configurado com premissas de contabilidade consultiva.

Privacidade (Privacy-First): Ideal para o setor contábil/financeiro, onde a confidencialidade é regra.

Abordagem de Controladoria: Foco em eficiência operacional e saúde financeira de longo prazo.

👨‍💻 Autor
Olivio Barreto Contador | Especialista em Controladoria, Finanças e Consultoria Empresarial Graduando em Ciência de Dados

Projeto desenvolvido como parte da especialização em IA Generativa, unindo a expertise contábil com o poder da Ciência de Dados para o futuro da gestão empresarial.


---

### Por que este README funciona para você?
1. **Autoridade:** Ele destaca que o bot não é apenas um "brinquedo", mas uma ferramenta de **contabilidade consultiva**.
2. **Perfil Híbrido:** Ele deixa claro que você entende de finanças (Contador/Especialista) e de tecnologia (Ciência de Dados), o que é raríssimo e muito valorizado.
3. **Foco em Segurança:** Mencionar que o processamento é local (Ollama) é um diferencial gigante para clientes qu
