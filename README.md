<p align="center">
  <a href="https://suajornadadedados.com.br/"><img src="https://github.com/lvgalvao/data-engineering-roadmap/raw/main/pics/logo.png" alt="Jornada de Dados"></a>
</p>
<p align="center">
    <em>Nossa missão é fornecer o melhor ensino em engenharia de dados</em>
</p>

Bem-vindo a **Jornada de Dados**

# 🚀 Jornada de Dados - ETL com Databricks

## 📌 Sobre este Projeto
Este repositório contém um **carrossel detalhado**, explicando o processo de **ETL (Extract, Transform, Load)** utilizando o **Databricks Community**. O foco é em **analistas de dados** que já possuem conhecimentos em **Excel** e desejam fazer a transição para **Python e Spark**.

## 📂 Estrutura do Projeto
O projeto está dividido em blocos sequenciais para facilitar o aprendizado:

1. **Introdução e Configuração do Databricks**
2. **Instalação e Importação de Bibliotecas**
3. **Extração de Dados da API do Bitcoin**
4. **Extração de Dados de um Arquivo Excel**
5. **Transformação e Limpeza de Dados**
6. **Unificação das Fontes de Dados**
7. **Conversão para Spark DataFrame**
8. **Armazenamento no Databricks**
9. **Consultas SQL e Análise Exploratória**
10. **Criação de Dashboard Básico**

## 📌 Como Executar o Projeto

### 1️⃣ Criar Conta no Databricks Community
Acesse [Databricks Community](https://community.cloud.databricks.com) e crie uma conta gratuita.

### 2️⃣ Criar um Notebook no Databricks
Dentro do Databricks, crie um **notebook Python** e execute o primeiro comando para testar o ambiente:

```python
print("Hello, Databricks!")
```

### 3️⃣ Instalar Bibliotecas Necessárias
Execute o seguinte comando para instalar os pacotes essenciais:

```python
%pip install requests pandas openpyxl
```

### 4️⃣ Extração de Dados da API do Bitcoin
Execute o seguinte código para extrair os preços do Bitcoin:

```python
import requests
import pandas as pd

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

bitcoin_data = {
    "moeda": ["USD", "EUR", "GBP"],
    "preco": [data["bpi"]["USD"]["rate_float"],
              data["bpi"]["EUR"]["rate_float"],
              data["bpi"]["GBP"]["rate_float"]]
}

df_bitcoin = pd.DataFrame(bitcoin_data)
print(df_bitcoin)
```

### 5️⃣ Upload e Leitura de um Arquivo Excel

1. No Databricks, clique em **Data** (barra lateral esquerda).
2. Clique em **Upload File** e selecione sua planilha Excel.
3. Copie o caminho do arquivo para usarmos no código.

Agora, carregue os dados no Pandas:

```python
df = pd.read_excel("/dbfs/FileStore/tables/transacoes.xlsx")
display(df)
```

### 6️⃣ Transformar e Limpar os Dados
Adicione um timestamp aos dados do Bitcoin:

```python
from datetime import datetime
df_bitcoin["data_extracao"] = datetime.now()
```

Outras etapas de transformação incluem:
- Remover dados duplicados.
- Converter formatos de colunas.
- Criar colunas calculadas.

### 7️⃣ Conversão para Spark DataFrame

Para melhorar a performance, convertemos os **DataFrames Pandas em Spark**:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ETL_Bitcoin").getOrCreate()

df_spark = spark.createDataFrame(df_bitcoin)
df_spark.show()
```

### 8️⃣ Armazenamento no Databricks

Podemos salvar os dados como **tabela Delta** para futuras consultas:

```python
df_spark.write.format("delta").mode("overwrite").save("/mnt/delta/bitcoin")
```

### 9️⃣ Consultas SQL

Agora podemos consultar os dados diretamente via SQL:

```sql
SELECT * FROM delta.`/mnt/delta/bitcoin` LIMIT 10;
```

### 🔟 Criar um Dashboard no Databricks
Com os dados processados, podemos criar visualizações dentro do Databricks para análise exploratória.

---

## 📌 Contribuição
Este projeto é aberto para melhorias! Se quiser contribuir:
1. **Fork** o repositório.
2. Crie uma branch: `git checkout -b minha-feature`
3. Adicione suas modificações e commite: `git commit -m 'Minha nova feature'`
4. Envie um **pull request** 🚀

## 📌 Contato
Se tiver dúvidas ou quiser discutir melhorias, entre em contato pelo LinkedIn: [Luciano Vasconcelos](https://www.linkedin.com/in/lucianovasconcelos).

