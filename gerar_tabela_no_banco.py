import random
import pandas as pd
import psycopg2
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
    2017: (6000, 130000),
    2018: (24000, 110000),
    2019: (20000, 90000),
    2020: (50000, 120000),
    2021: (60000, 700000),
    2022: (120000, 440000),
    2023: (180000, 500000),
    2024: (600000, 700000),  # Valor fixo
    2025: (500000, 600000)  # Valor fixo
}

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="transacoes_pbpt",
    user="transacoes_pbpt_user",
    password="TMigRMGDiJDMPz1efl0F4plHaNWjlHyF",
    host="dpg-cuqbmgggph6c73d0l5m0-a.ohio-postgres.render.com",
    port="5432"
)
cur = conn.cursor()

# Criar tabela no banco de dados
cur.execute('''
    DROP TABLE IF EXISTS transacoes_clientes;
    CREATE TABLE IF NOT EXISTS transacoes_clientes (
        id SERIAL PRIMARY KEY,
        cliente VARCHAR(100),
        data_compra TIMESTAMP,
        preco_btc DECIMAL(10,2),
        quantidade_btc DECIMAL(10,5)
    )
''')
conn.commit()

# Gerar transações aleatórias e inserir no banco de dados
for cliente in clientes:
    data_compra = random_date(start_date, end_date)
    ano = data_compra.year
    preco_min, preco_max = btc_prices.get(ano, (150000, 350000))  # Garantir valores válidos
    preco_btc = round(random.uniform(preco_min, preco_max), 2)
    quantidade_btc = round(random.uniform(0.001, 1.5), 5)  # Variação de compra de 0.001 até 1.5 BTC
    
    cur.execute(
        "INSERT INTO transacoes_clientes (cliente, data_compra, preco_btc, quantidade_btc) VALUES (%s, %s, %s, %s)",
        (cliente, data_compra, preco_btc, quantidade_btc)
    )

# Confirmar alterações e fechar conexão
conn.commit()
cur.close()
conn.close()

print("Transações inseridas no banco de dados com sucesso!")