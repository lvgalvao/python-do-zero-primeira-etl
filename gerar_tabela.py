import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Inicializar Faker para gerar nomes
fake = Faker()
Faker.seed(42)
random.seed(42)

# Gerar 100 clientes únicos
clientes = [fake.name() for _ in range(100)]

# Função para gerar uma data aleatória entre 2017 e 2025
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

start_date = datetime(2017, 1, 1)
end_date = datetime(2025, 2, 17)

# Faixa de preços do Bitcoin de 2017 até 2025 (valores aproximados em BRL)
btc_prices = {
    2017: (3000, 65000),
    2018: (12000, 55000),
    2019: (10000, 45000),
    2020: (25000, 60000),
    2021: (30000, 350000),
    2022: (60000, 220000),
    2023: (90000, 250000),
    2024: (120000, 300000),
    2025: (150000, 350000)
}

# Gerar transações aleatórias
transacoes = []
for cliente in clientes:
    data_compra = random_date(start_date, end_date)
    ano = data_compra.year
    preco_min, preco_max = btc_prices.get(ano, (150000, 350000))  # Garantir valores válidos
    preco_btc = round(random.uniform(preco_min, preco_max), 2)
    quantidade_btc = round(random.uniform(0.001, 1.5), 5)  # Variação de compra de 0.001 até 1.5 BTC
    valor_total = round(preco_btc * quantidade_btc, 2)
    transacoes.append((cliente, data_compra, preco_btc, quantidade_btc, valor_total))

# Criar DataFrame
columns = ["cliente", "data_compra", "preco_btc", "quantidade_btc", "valor_total"]
df_transacoes = pd.DataFrame(transacoes, columns=columns)

# Exibir as primeiras linhas
print(df_transacoes)

# Salvar em CSV
df_transacoes.to_csv("transacoes_clientes.csv", index=False)
