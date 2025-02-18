## **📌 Categorizar se houve lucro ou prejuízo na compra de Bitcoin**

Nosso objetivo é **comparar o preço de compra do Bitcoin com o preço atual** para determinar se houve **lucro ou prejuízo** na operação.

---

## **1️⃣ O que é uma API?**
Uma **API (Application Programming Interface)** é um **meio de comunicação entre sistemas**. No nosso caso, vamos utilizar uma API de preços de criptomoedas para obter **o valor atual do Bitcoin** e compará-lo com os preços armazenados em nosso DataFrame.

📌 **Exemplo do funcionamento da API:**  
- Enviamos uma requisição para um **servidor** (API do Bitcoin).
- O servidor nos retorna um **JSON** com o preço atual.
- Salvamos esse valor e o utilizamos para análise.

---

## **2️⃣ Como usar o requests para consumir uma API**
O **`requests`** é uma biblioteca do Python que permite **fazer requisições HTTP** para APIs e recuperar dados.

🔹 **Exemplo de requisição à API do Bitcoin:**
```python
import requests

# URL da API para obter o preço atual do Bitcoin em USD
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# Fazendo a requisição para a API
response = requests.get(url)

# Convertendo o JSON para um dicionário Python
dados = response.json()

# Extraindo o preço do Bitcoin em dólares
preco_atual_btc = dados["bpi"]["USD"]["rate_float"]

print(f"Preço atual do Bitcoin: ${preco_atual_btc:.2f}")
```

📌 **Explicação do código:**
- `requests.get(url)`: Faz uma **requisição GET** para a API.
- `response.json()`: Converte o **JSON** da resposta para um **dicionário Python**.
- `dados["bpi"]["USD"]["rate_float"]`: Acessa a chave do JSON que contém o preço atual.

---

## **3️⃣ O que é uma função?**
Uma **função** é um bloco de código **reutilizável** que executa uma tarefa específica.  
Usamos funções para **organizar código, evitar repetições e torná-lo mais eficiente**.

📌 **Sintaxe básica de uma função em Python:**
```python
def nome_da_funcao(parametros):
    # Código da função
    return resultado
```

🔹 **Exemplo de uma função que soma dois números:**
```python
def soma(a, b):
    return a + b

resultado = soma(5, 10)
print(resultado)  # Saída: 15
```

---

## **4️⃣ Criando uma função para verificar lucro ou prejuízo**
Agora que já entendemos **API, funções e if**, vamos criar uma **função para categorizar as compras**.

📌 **Lógica da função:**
1. Se o **preço de compra for menor** que o **preço atual**, houve **lucro**.
2. Caso contrário, houve **prejuízo**.

🔹 **Código da função:**
```python
def verificar_lucro(preco_compra):
    if preco_compra < preco_atual_btc:
        return "Lucro"
    else:
        return "Prejuízo"
```

📌 **Explicação do código:**
- A função **recebe um valor** (`preco_compra`).
- Compara com o **preço atual do Bitcoin** (`preco_atual_btc`).
- **Retorna `"Lucro"`** se o preço de compra for menor que o atual, **senão retorna `"Prejuízo"`**.

---

## **5️⃣ Aplicando a função no DataFrame com `.apply()`**
Agora que temos a função `verificar_lucro()`, podemos aplicá-la **a cada linha do DataFrame Pandas**.

🔹 **Código para aplicar a função no DataFrame:**
```python
df["resultado_operacao"] = df["preco_btc"].apply(verificar_lucro)
```

📌 **Explicação do código:**
- `df["preco_btc"].apply(verificar_lucro)`:  
  - Aplica a função `verificar_lucro()` **a cada valor da coluna `preco_btc`**.
  - O resultado é armazenado na nova coluna **`resultado_operacao`**.

---

## **6️⃣ Código Completo**
```python
import pandas as pd
import requests

# Obtendo o preço atual do Bitcoin da API
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
dados = response.json()
preco_atual_btc = dados["bpi"]["USD"]["rate_float"]

# Criando a função para verificar lucro ou prejuízo
def verificar_lucro(preco_compra):
    if preco_compra < preco_atual_btc:
        return "Lucro"
    else:
        return "Prejuízo"

# Criando o DataFrame com dados simulados
dados = {
    "cliente": ["Sherry Decker", "Gerald Hensley", "Timothy Duncan"],
    "preco_btc": [202677.81, 233598.53, 156207.19],
    "quantidade_btc": [0.75138, 0.34418, 0.46826]
}

df = pd.DataFrame(dados)

# Aplicando a função para categorizar cada transação
df["resultado_operacao"] = df["preco_btc"].apply(verificar_lucro)

# Exibindo o DataFrame atualizado
print(df)
```

---

## **7️⃣ Conclusão**
- **Uma API** permite buscar dados **externos** automaticamente.
- O **requests** nos ajuda a **fazer requisições HTTP** e extrair **JSON**.
- Criamos **uma função para comparar preços e determinar lucro ou prejuízo**.
- **Aplicamos essa função ao DataFrame** com `apply()`.

Esse processo é fundamental para **análises financeiras** e pode ser aplicado em **qualquer outro mercado**. Se precisar de mais detalhes ou adaptações, me avise!