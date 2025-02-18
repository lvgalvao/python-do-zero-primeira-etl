# Agora que já sabemos o básico do Python, vamos falar do Pandas

# **Manipulação de Dados com Pandas**
Agora que já aprendemos os conceitos básicos de Python, vamos aprender a **trabalhar com dados tabulares** utilizando **Pandas**. O Pandas é uma **biblioteca poderosa** para manipulação de dados em Python e é amplamente utilizada para **análises estatísticas, ETL (Extração, Transformação e Carga de Dados) e Machine Learning**.

---

## **1. Criando um DataFrame**
No Pandas, um **DataFrame** é uma **estrutura de dados tabular**, similar a uma **tabela do Excel**. Ele organiza os dados em **linhas e colunas**, permitindo operações eficientes.

---

### 1. Como Inserir Dados no Databricks?

No Databricks, podemos inserir dados de diferentes formas:  
✅ **Por meio de arquivos CSV** (dados estruturados).  
✅ **Através de um banco de dados SQL**.  
✅ **Consumindo uma API externa** (dados dinâmicos).  

Vamos começar **carregando um arquivo CSV** e entendendo como esses dados são estruturados!  

---

### 2. Inserindo Dados por CSV*

O **CSV (Comma-Separated Values)** é um dos formatos mais comuns para armazenar dados.  
Ele é uma **tabela estruturada** onde os valores são separados por **vírgulas** ou **pontos e vírgulas**.

### **📌 Como fazer o upload de um CSV no Databricks?**  
1️⃣ Acesse o **Databricks UI** e vá até a aba **"Data"**.  
2️⃣ Clique em **"Create Table"** e depois em **"Upload File"**.  

📌 **Exemplo de leitura do CSV no Databricks com Pandas:**
```python
import pandas as pd

df_spark = spark.read.table("transacoes_clientes_csv")
df = df_spark.toPandas()
print(df.head())
```

---

## 3. Mas que estrutura de dados são essas?

Quando lemos um CSV, os dados podem ser armazenados de diferentes formas:  
- Em uma **lista comum** (`list`) → Menos organizada, difícil de manipular.  
- Em **listas dentro de listas** (`list of lists`) → Estruturada, mas sem recursos avançados.  
- Em um **DataFrame** (`pandas.DataFrame`) → Melhor para manipulação de dados!  

### **📌 Exemplo de como os dados são organizados**  

🔹 **Representação como Lista Simples:**
```python
dados = ["Alice", 30, "São Paulo"]
```

🔹 **Representação como Lista dentro de Lista (Tabela Estruturada):**
```python
dados = [
    ["Alice", 30, "São Paulo"],
    ["Bob", 25, "Rio de Janeiro"],
    ["Carol", 27, "Belo Horizonte"]
]
```
📌 **Mas o que acontece se tivermos milhares de linhas?**  
Aqui entra o **DataFrame**, que facilita o manuseio dos dados!

🔹 **Representação como DataFrame Pandas:**
```python
import pandas as pd

dados = {
    "Nome": ["Alice", "Bob", "Carol"],
    "Idade": [30, 25, 27],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

df = pd.DataFrame(dados)
print(df)
```

✅ **Agora temos uma tabela estruturada, fácil de manipular!**

---

## **2️⃣ Criando Novas Colunas**
Podemos criar colunas utilizando operações matemáticas, funções personalizadas e expressões condicionais.

🔹 **Criando uma nova coluna `total_de_compra`** (preço * quantidade):
```python
df["total_de_compra"] = df["preco_btc"] * df["quantidade_btc"]
print(df[["cliente", "preco_btc", "quantidade_btc", "total_de_compra"]].head())
```

---

## **3️⃣ Filtragem de Dados**
A filtragem de dados no Pandas é semelhante ao uso do **filtro no Excel**, permitindo selecionar subconjuntos de dados que atendem a determinadas condições.

🔹 **Selecionando transações onde a `quantidade_btc` é maior que 1**:
```python
df_filtrado = df[df["quantidade_btc"] > 1]
print(df_filtrado)
```

🔹 **Contando quantas transações atendem à condição acima**:
```python
quantidade_transacoes = df[df["quantidade_btc"] > 1].shape[0]
print(f"Número de transações com mais de 1 BTC: {quantidade_transacoes}")
```

---

## **4️⃣ Ordenação de Dados**
Ordenar um DataFrame é similar ao **ordenar uma tabela no Excel**.

🔹 **Ordenando transações pelo `preco_btc` do maior para o menor**:
```python
df_ordenado = df.sort_values(by="preco_btc", ascending=False)
print(df_ordenado.head())
```

---

## **5️⃣ Selecionando Colunas**
Podemos selecionar apenas algumas colunas para exibição.

🔹 **Selecionando apenas `cliente`, `data_compra` e `total_de_compra`**:
```python
df_selecionado = df[["cliente", "data_compra", "total_de_compra"]]
print(df_selecionado.head())
```

---

## **6️⃣ Agrupamento de Dados**
No Excel, **Tabelas Dinâmicas (Pivot Table)** permitem resumir grandes volumes de dados. No Pandas, usamos `groupby()` para essa finalidade.

### **Explicação Detalhada do Código**

O código abaixo faz duas operações principais:
1. **Criação de uma nova coluna `mes_compra`** extraindo o mês e ano da coluna `data_compra`.
2. **Agrupamento das transações por mês** e soma dos valores da coluna `total_de_compra`.

```python
df["mes_compra"] = df["data_compra"].dt.to_period("M")

df_agrupado = df.groupby("mes_compra")["total_de_compra"].sum().reset_index()
print(df_agrupado)
```

---

## **1️⃣ Criando a Coluna `mes_compra`**
```python
df["mes_compra"] = df["data_compra"].dt.to_period("M")
```

### **O que acontece aqui?**
- `df["data_compra"]` → É a coluna que contém as datas das transações.
- `.dt.to_period("M")` → Converte a data completa (`YYYY-MM-DD`) para um **período de mês e ano** (`YYYY-MM`).
- `df["mes_compra"]` → Criamos uma nova coluna contendo apenas o **mês e ano da compra**.

### **Exemplo**
Suponha que `data_compra` tenha os seguintes valores:

| data_compra        | mes_compra |
|--------------------|-----------|
| 2025-01-26        | 2025-01   |
| 2024-12-09        | 2024-12   |
| 2024-09-26        | 2024-09   |

Agora, temos uma **coluna que representa apenas o mês e ano da compra**, facilitando a agregação por períodos.

---

## **2️⃣ Agrupamento das Transações por Mês**
```python
df_agrupado = df.groupby("mes_compra")["total_de_compra"].sum().reset_index()
```

### **O que acontece aqui?**
- `df.groupby("mes_compra")` → Agrupa os dados por mês.
- `["total_de_compra"].sum()` → Soma os valores da coluna `total_de_compra` dentro de cada mês.
- `.reset_index()` → Restaura o índice do DataFrame, garantindo que `mes_compra` continue como coluna normal.

### **Exemplo**
Se tivermos essas transações:

| mes_compra | total_de_compra |
|------------|----------------|
| 2025-01    | 50.000         |
| 2025-01    | 75.000         |
| 2024-12    | 30.000         |
| 2024-09    | 100.000        |
| 2024-09    | 40.000         |

Após o agrupamento (`groupby("mes_compra")`) e soma dos valores (`sum()`), o resultado será:

| mes_compra | total_de_compra |
|------------|----------------|
| 2025-01    | 125.000        |
| 2024-12    | 30.000         |
| 2024-09    | 140.000        |

Agora temos um **resumo mensal** das transações.

---

## **Resumo Final**
📌 **Objetivo do código**:
- Extrair **mês e ano** das datas de compra.
- Agrupar os dados por mês.
- Somar o **total de compras** realizadas em cada mês.

📌 **Benefícios**:
- Permite **análises temporais** de vendas.
- Útil para criar **gráficos de tendência** no tempo.
- Similar a **Tabelas Dinâmicas do Excel**, mas em código.

Se precisar de mais explicações, me avise!

---

## **7️⃣ Aplicando Condições (If no Pandas)**
No Excel, podemos criar **colunas condicionais** usando `SE()`. No Pandas, usamos `apply()`.

🔹 **Criando uma coluna que indica se a compra foi acima de R$ 200.000**:
```python
df["alta_compra"] = df["total_de_compra"] > 200000
print(df[["cliente", "total_de_compra", "alta_compra"]].head())
```

---

## **8️⃣ Estatísticas Básicas**
Podemos gerar estatísticas rápidas sobre os dados.

🔹 **Verificando estatísticas descritivas**:
```python
print(df.describe())  # Mostra média, mínimo, máximo e desvio padrão
```

🔹 **Verificando se há valores nulos**:
```python
print(df.isnull().sum())  # Conta quantos valores nulos existem por coluna
```

---

## **9️⃣ Salvando e Carregando Arquivos**
🔹 **Salvando o DataFrame em CSV**:
```python
df.to_csv("transacoes_processadas.csv", index=False)
```

🔹 **Lendo um CSV salvo anteriormente**:
```python
df_lido = pd.read_csv("transacoes_processadas.csv")
print(df_lido.head())
```

---

## **📌 Conclusão**
- Aprendemos **como criar, manipular e analisar dados no Pandas**.
- Exploramos **filtragem, ordenação, agregação e estatísticas**.
- Fizemos **comparação com operações comuns no Excel**.
- Criamos **novas colunas e aplicamos condições**.

O Pandas é uma ferramenta poderosa para **engenharia e ciência de