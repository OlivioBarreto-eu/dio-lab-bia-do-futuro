# Base de Conhecimento

> [!TIP]
> **Prompt usado para esta etapa:**
> 
> Organize a base de conhecimento do agente "Edu" usando os 4 arquivos da pasta `data/` (em anexo). Explique pra que serve cada arquivo e monte um exemplo de contexto formatado que será enviado pro LLM. Preencha o template abaixo.
>
> [cole ou anexe o template `02-base-conhecimento.md` pra contexto]

## Dados Utilizados

| Arquivo | Formato | Para que serve no Edu? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, ou seja, dar continuidade ao atendimento de forma mais eficiente. |
| `perfil_cliente.json` | JSON | Mapeamento do perfil do cliente, suas necessidades e abordagem indicada. |
| `programas_consultoria.json` | JSON | Conhecer os produtos disponíveis para que eles possam ser ofertados ao cliente. |
| `transacoes.csv` | CSV | Analisar padrão de fluxo de caixa do cliente e usar essas informações para analisar o cenario e tomar decisões. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Modificados todos os dados, abaixo segue o que foi feito em alterações:
historico de atendimento: Relatado da prospecção ao fechamento com o cliente
perfild do cliente: Mapeamento de quem é o cliente e necessidades de atendimento
Programas de consultoria: pacotes de serviço a serem ofertados
Transações: movimentações financeira de teste pasa simular o historico do cliente

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json

perfil = json.load(open('./data/perfil_cliente.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/programas_consultoria.json'))
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, gaarntindo que o Agente tenha o melhor contexto possível. Lembrando que, em soluções mais robustas, o ideal é que essas informaçoes sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```text
DADOS DO CLIENTE E PERFIL (data/perfil_investidor.json):
{
  "nome": "João & Silva LTDA",
  "tempo de atividade": 5,
  "Ramo de Atividade": "Comercio de eletronicos e variedades",
  "faturamento_mensal": 500000.00,
  "Nivel_de_organicao": "precario",
  "objetivo_principal": "possibilitar gestão com dados, indicadores e ajustar o caixa",
  "possui_restricao": true,
  "metas": [
    {
      "meta": "Negociar fornecedores inadimplentes e organizar caixa",
      "valor_necessario": 150000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Elaborar demonstrativos de resultado",
      "valor_necessario": 0.00,
      "prazo": "2026-06"
    }
  ]
}

TRANSACOES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Venda de smartphones,Receita de vendas,28000.00,entrada
2025-10-02,Compra de estoque fornecedor A,Fornecedores,32000.00,saida
2025-10-03,Pagamento de energia elétrica,Despesas fixas,2700.00,saida
2025-10-05,Venda de acessórios,Receita de vendas,15000.00,entrada
2025-10-07,Frete e logística,Despesas operacionais,3800.00,saida
2025-10-10,Pagamento folha funcionários,Despesas operacionais,27000.00,saida
2025-10-12,Receita online marketplace,Receita de vendas,22000.00,entrada
2025-10-15,Pagamento fornecedor B,Fornecedores,23000.00,saida
2025-10-18,Marketing digital,Despesas comerciais,6500.00,saida
2025-10-20,Venda empresarial,Receita de vendas,40000.00,entrada
2025-10-25,Taxas bancárias,Despesas financeiras,1200.00,saida
2025-10-28,Pagamento de aluguel,Despesas fixas,15000.00,saida
2025-10-30,Impostos sobre vendas,Impostos,9000.00,saida
2025-11-01,Venda de Black Friday,Receita de vendas,90000.00,entrada
2025-11-02,Compra de estoque fornecedor C,Fornecedores,55000.00,saida
2025-11-03,Pagamento de transporte,Despesas operacionais,4000.00,saida
2025-11-05,Serviço de manutenção elétrica,Despesas de manutenção,3000.00,saida
2025-11-06,Receita de loja física,Receita de vendas,45000.00,entrada
2025-11-07,Pagamento folha funcionários,Despesas operacionais,28000.00,saida
2025-11-09,Receita via PIX,Receita de vendas,26000.00,entrada
2025-11-12,Impostos e encargos,Impostos,9500.00,saida
2025-11-15,Despesa com internet,Despesas fixas,1200.00,saida
2025-11-18,Compra de novos produtos,Fornecedores,24000.00,saida
2025-11-20,Venda corporativa,Receita de vendas,48000.00,entrada
2025-11-25,Marketing digital,Despesas comerciais,8000.00,saida
2025-11-28,Aluguel loja,Despesas fixas,15000.00,saida
2025-11-30,Taxas financeiras,Despesas financeiras,1600.00,saida
2025-12-01,Venda de natal,Receita de vendas,95000.00,entrada
2025-12-02,Compra de estoque natalino,Fornecedores,62000.00,saida
2025-12-05,Frete extra,Despesas operacionais,6500.00,saida
2025-12-06,Serviço de consultoria,Despesas administrativas,6000.00,saida
2025-12-07,Receita de vendas online,Receita de vendas,32000.00,entrada
2025-12-10,Pagamento fornecedor D,Fornecedores,25000.00,saida
2025-12-15,Venda corporativa,Receita de vendas,40000.00,entrada
2025-12-20,Pagamento de folha,Despesas operacionais,30000.00,saida
2025-12-22,Impostos sobre vendas,Impostos,12000.00,saida
2025-12-27,Marketing Natal,Despesas comerciais,9000.00,saida
2025-12-30,Aluguel loja,Despesas fixas,15500.00,saida

HISTORICO DE ATENDIMENTO DO CLIENTE (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,telefone,dificultade de caixa,Cliente buscou auxilio por dificuldades financeiras,sim
2025-09-22,chat,Negociação do diagnostico,enviado orçamento ao cliente e aprovado,sim
2025-10-01,in-loco,Realização do diagnsotico,levantamento aprofundado da real situação do cliente,sim
2025-10-12,videochamada,Apresentação do diagnostico,apresentado e oferecidos programas e aceite por parte do cliente,sim
2025-10-25,email,Informativo de agenda e inicio do trabalho,enviada agenda de atendimento e escopo do trabalho,sim

PRODUTOS DISPONIVEIS PARA ENSINO (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliário (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "Dividend Yield (DY) costuma ficar entre 6% a 12% ao ano",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto montado abaixo, se baiseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relevantes, otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é ter todas as informações relevantes disponíveis em seu contexto.

```
DADOS DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Construir reserva de emergência
- Reserva atual: R$ 10.000 (meta: R$ 15.000)

RESUMO DE GASTOS:
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90

PRODUTOS DISPONÍVEIS PARA EXPLICAR:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Imobiliário - FII (risco médio)
- Fundo de Ações (risco alto)
```
