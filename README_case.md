# Agora que já sabemos o básico do Python, vamos falar do Pandas

Agora que aprendemos sobre **variáveis, operadores, strings, listas e controle de fluxo**, chegou a hora de trabalhar com **dados reais** dentro do **Databricks**!  

---

## 1. Como Inserir Dados no Databricks?

No Databricks, podemos inserir dados de diferentes formas:  
✅ **Por meio de arquivos CSV** (dados estruturados).  
✅ **Através de um banco de dados SQL**.  
✅ **Consumindo uma API externa** (dados dinâmicos).  

Vamos começar **carregando um arquivo CSV** e entendendo como esses dados são estruturados!  

---

## 2. Inserindo Dados por CSV*

O **CSV (Comma-Separated Values)** é um dos formatos mais comuns para armazenar dados.  
Ele é uma **tabela estruturada** onde os valores são separados por **vírgulas** ou **pontos e vírgulas**.

### **📌 Como fazer o upload de um CSV no Databricks?**  
1️⃣ Acesse o **Databricks UI** e vá até a aba **"Data"**.  
2️⃣ Clique em **"Create Table"** e depois em **"Upload File"**.  

📌 **Exemplo de leitura do CSV no Databricks com Pandas:**
```python
import pandas as pd

df_spark = spark.read.table("transacoes_clientes_csv")
df_pandas = df.toPandas()
print(df_pandas.head())
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

## **4️⃣ O que é o Pandas?**  

O **Pandas** é uma **biblioteca do Python** usada para **manipular e analisar dados tabulares**.  
Ele é **essencial para ciência de dados** e funciona como uma **planilha do Excel dentro do Python**.

📌 **Principais recursos do Pandas:**  
✅ Permite **ler e escrever arquivos CSV, Excel e SQL**.  
✅ Possui funções para **filtrar, transformar e agrupar dados**.  
✅ Integra-se facilmente com **Databricks, APIs e bancos de dados**.  

🔹 **Exemplo de funções úteis no Pandas:**  
```python
print(df.head())     # Exibir as primeiras 5 linhas
print(df.info())     # Mostrar informações do DataFrame
print(df.describe()) # Estatísticas das colunas numéricas
```

---

## **5️⃣ Onde o Pandas é Utilizado?**  

O Pandas é **amplamente utilizado** em diferentes áreas:

🔹 **Ciência de Dados & Machine Learning** → Processamento e análise de grandes volumes de dados.  
🔹 **Análises Financeiras** → Estudo de preços de ações, câmbio, criptomoedas.  
🔹 **ETL e Engenharia de Dados** → Extração e transformação de dados para bancos SQL e Big Data.  
🔹 **Automação de Relatórios** → Geração de gráficos e insights para tomada de decisões.  

📌 **Exemplo de uso real:**
```python
# Filtrando usuários com idade maior que 26 anos
df_filtrado = df[df["Idade"] > 26]
print(df_filtrado)
```

✅ Agora já sabemos **como inserir e manipular dados com Pandas no Databricks!**  

---

### **📌 Conclusão**
🔥 **Aprendemos como carregar um CSV no Databricks** e **entendemos como os dados são estruturados**.  
🚀 **Vimos que o Pandas facilita a manipulação de tabelas**, tornando análises e cálculos muito mais fáceis.  

➡️ **Agora, vamos avançar para manipular esses dados no Databricks com SQL e APIs!** 🔥

Aqui estão exemplos de comandos **Pandas** aplicados ao **DataFrame** fornecido:

---

### **📌 1️⃣ Filtragem de Dados**
Selecionando transações onde o **valor total** é **maior que 100.000**:

```python
df_filtrado = df[df["quantidade_btc"] > 1]
print(df_filtrado.head())  # Exibe as primeiras linhas do DataFrame filtrado
```


Para contar quantos registros atendem à condição **`quantidade_btc > 1`**, você pode usar o método **`.shape[0]`** ou **`.count()`**:

---

### **📌 Usando `.shape[0]` (Mais comum)**
```python
quantidade_transacoes = df[df["quantidade_btc"] > 1].shape[0]
print(f"Número de transações com mais de 1 BTC: {quantidade_transacoes}")
```
✅ Retorna o **número total de linhas** onde a condição é verdadeira.

---

### **📌 Usando `.count()`**
```python
quantidade_transacoes = df[df["quantidade_btc"] > 1]["quantidade_btc"].count()
print(f"Número de transações com mais de 1 BTC: {quantidade_transacoes}")
```
✅ Conta apenas os valores **não nulos** na coluna `quantidade_btc`.

Ambos os métodos funcionam, mas **`.shape[0]` é mais genérico e recomendado!** 🚀


---

### **📌 2️⃣ Ordenação de Dados**
Ordenando as transações pelo **preço do Bitcoin**, do **maior para o menor**:

```python
df_ordenado = df.sort_values(by="preco_btc", ascending=False)
print(df_ordenado.head())  # Exibe as primeiras transações ordenadas pelo preço do BTC
```

---

### **📌 3️⃣ Agrupamento de Dados**
Agrupando transações por **mês de compra** e somando o **valor total**:

```python
# Criando uma nova coluna para armazenar o mês e ano da compra
df["mes_compra"] = df["data_compra"].dt.to_period("M")

# Agrupando por mês e somando o valor total das transações
df_agrupado = df.groupby("mes_compra")["valor_total"].sum().reset_index()

print(df_agrupado)  # Exibe o total de transações agrupadas por mês
```

---

### **📌 4️⃣ Selecionando Colunas Específicas**
Selecionando apenas as colunas **cliente, data_compra e valor_total**:

```python
df_selecionado = df[["cliente", "data_compra", "valor_total"]]
print(df_selecionado.head())  # Exibe apenas as colunas selecionadas
```

---

### **📌 5️⃣ Criando Novas Colunas**
Criando uma **coluna booleana** para identificar **compras acima de 200.000**:

```python
df["total_de_compra"] = df["preco_btc"] * df["quantidade_btc"]
print(df[["cliente", "preco_btc", "quantidade_btc", "total_de_compra"]].head())
```
✅ Agora, cada transação mostra o **valor total da compra**. 🚀  
Se precisar de mais manipulações, me avise!