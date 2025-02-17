<p align="center">
  <a href="https://suajornadadedados.com.br/"><img src="https://github.com/lvgalvao/data-engineering-roadmap/raw/main/pics/logo.png" alt="Jornada de Dados"></a>
</p>
<p align="center">
    <em>Nossa missão é fornecer o melhor ensino em engenharia de dados</em>
</p>

Bem-vindo a **Jornada de Dados**

# 🚀 Jornada de Dados - Python do zero no Databricks

# Principais Métodos Python para a Área de Dados

import requests
import pandas as pd

# 1. Print - Exibir mensagens no console
print("Hello, Databricks!")

# 2. Len - Retornar o tamanho de uma lista, tupla ou string
data = [10, 20, 30, 40]
print(len(data))  # Saída: 4

# 3. Type - Verificar o tipo de dado de um objeto
print(type(data))  # Saída: <class 'list'>

# 4. Append - Adicionar elementos a uma lista
data.append(50)
print(data)  # Saída: [10, 20, 30, 40, 50]

# 5. Extend - Adicionar múltiplos elementos a uma lista
data.extend([60, 70, 80])
print(data)  # Saída: [10, 20, 30, 40, 50, 60, 70, 80]

# 6. Pop - Remover e retornar um elemento da lista
print(data.pop())  # Saída: 80
print(data)  # Lista após remoção

# 7. Keys - Retornar as chaves de um dicionário
dic = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
print(dic.keys())  # Saída: dict_keys(['nome', 'idade', 'cidade'])

# 8. Values - Retornar os valores de um dicionário
print(dic.values())  # Saída: dict_values(['Ana', 25, 'São Paulo'])

# 9. Items - Retornar os pares chave-valor de um dicionário
print(dic.items())  # Saída: dict_items([('nome', 'Ana'), ('idade', 25), ('cidade', 'São Paulo')])

# 10. Get - Obter um valor do dicionário sem erro se a chave não existir
print(dic.get("idade"))  # Saída: 25

# Métodos do Pandas

# 11. Criar um DataFrame
df = pd.DataFrame({"Nome": ["Ana", "Carlos"], "Idade": [25, 30]})
print(df)

# 12. Ler um CSV
df_csv = pd.read_csv("dados.csv")
print(df_csv.head())

# 13. Informações gerais do DataFrame
print(df.info())

# 14. Estatísticas descritivas do DataFrame
print(df.describe())

# 15. Seleção de colunas
print(df["Nome"])  # Selecionar uma coluna específica

# 16. Filtrar dados
print(df[df["Idade"] > 25])  # Filtrar onde Idade > 25

# 17. Agrupar dados por uma coluna
print(df.groupby("Nome").mean())

# 18. Ordenar valores
print(df.sort_values(by="Idade", ascending=False))

# 19. Adicionar uma nova coluna
df["Salário"] = [3000, 4000]
print(df)

# 20. Salvar o DataFrame em um CSV
df.to_csv("dados_processados.csv", index=False)

# Novos comandos para obtenção e manipulação de dados da API Bitcoin

# 21. Fazer um request para API do Bitcoin
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

# 22. Criar um DataFrame com os preços do Bitcoin
bitcoin_data = {
    "moeda": ["USD", "EUR", "GBP"],
    "preco": [data["bpi"]["USD"]["rate_float"],
              data["bpi"]["EUR"]["rate_float"],
              data["bpi"]["GBP"]["rate_float"]]
}

df_bitcoin = pd.DataFrame(bitcoin_data)
print(df_bitcoin)

# 23. Salvar os dados do Bitcoin em CSV
df_bitcoin.to_csv("bitcoin_data.csv", index=False)

# 24. Carregar o CSV salvo e fazer o append dos novos dados
existing_df = pd.read_csv("bitcoin_data.csv")
new_data = pd.DataFrame(bitcoin_data)
updated_df = pd.concat([existing_df, new_data], ignore_index=True)
print(updated_df)

# 25. Salvar o DataFrame atualizado
df_bitcoin.to_csv("bitcoin_data_atualizado.csv", index=False)
