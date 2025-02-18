 
<p align="center">
  <a href="https://suajornadadedados.com.br/"><img src="https://github.com/lvgalvao/data-engineering-roadmap/raw/main/pics/logo.png" alt="Jornada de Dados"></a>
</p>
<p align="center">
    <em>Nossa missão é fornecer o melhor ensino em engenharia de dados</em>
</p>

Bem-vindo a **Jornada de Dados**

# Intensivo de Python no Databricks

Este projeto tem como objetivo apresentar os primeiros comandos de Python. 

# Começando com o Python

---

## 1. Print - Exibir mensagens no console

O comando **`print()`** é uma das primeiras funções que aprendemos ao começar a programar. Ele é usado para **exibir informações na tela**, tornando possível visualizar resultados e mensagens durante a execução do código.

🔹 **Por que `print()` é importante?**
- Ajuda a depurar o código (verificando valores intermediários).
- Permite exibir mensagens para o usuário.
- Facilita a interação com o console.

🔹 **Exemplo de uso básico:**
```python
print("Olá, Jornada de dados!")
```
✅ **Saída:**  
```
Olá, Jornada de dados!
```

🔹 **O que está acontecendo?**
- `print()` é uma **função embutida (built-in function)** no Python.
- Ele recebe um **argumento**, que no caso é o texto `"Olá, Jornada de dados!"`, e exibe esse texto no console.

🔹 **O que é um argumento?**
Um **argumento** é um valor passado para um método ou função para modificar seu comportamento.  
No exemplo acima, `"Olá, Jornada de dados!"` é o **argumento passado para `print()`**, e ele define o que será exibido na tela.

---

## 2. Operadores

Os **operadores matemáticos** são usados para **realizar cálculos** e operações matemáticas no Python. Eles são essenciais para trabalhar com **números**, seja em **cálculos simples**, **análises de dados** ou **operações em bancos de dados**.

🔹 **Tipos de operadores matemáticos:**
```python
print(1 + 2)  # Soma → Retorna 3
print(4 - 3)  # Subtração → Retorna 1
print(2 * 2)  # Multiplicação → Retorna 4
print(4 / 2)  # Divisão → Retorna 2.0
print(5 // 2) # Divisão inteira → Retorna 2 (descarta o decimal)
print(5 % 2)  # Módulo → Retorna 1 (resto da divisão)
print(2 ** 3) # Exponenciação → Retorna 8 (2 elevado a 3)
```

🔹 **Por que operadores são importantes?**
- Permitem fazer cálculos simples e complexos.
- São usados em **análises estatísticas** e **operações com DataFrames** no Pandas.
- Facilitam a manipulação de dados numéricos.

---

## 3. Variáveis

### **📌 Variáveis no Python**  

Uma **variável** é um **espaço na memória** onde armazenamos valores que podem ser usados posteriormente. No Python, não precisamos declarar o tipo da variável explicitamente – o interpretador identifica automaticamente.  

---

### **📌 Como criar variáveis**  
```python
# Criando variáveis
nome = "Jornada de Dados"  # String
idade = 25  # Inteiro
altura = 1.75  # Float

# Exibindo valores
print(nome)  # Saída: Jornada de Dados
print(idade)  # Saída: 25
print(altura)  # Saída: 1.75
```

📌 **Exemplo de uso no mundo real:**  

```python
preco = 100
desconto = 10
preco_final = preco - desconto  # Aplicando desconto
print(preco_final)  # Saída: 90
```

## 4 Type - Verificar o tipo de dado

O Python **trabalha com diferentes tipos de dados**, e a função `type()` nos permite verificar o tipo de qualquer objeto.

🔹 **Exemplo de uso:**
```python
print(type(10))       # <class 'int'> (Número inteiro)
print(type(3.14))     # <class 'float'> (Número decimal)
print(type("Python")) # <class 'str'> (Texto)
```

🔹 **Por que `type()` é útil?**
- Permite **entender melhor os dados** com os quais estamos trabalhando.
- Evita **erros de tipo**, como tentar somar um número com um texto.

---

## 5. Strings - Trabalhando com Textos
No Python, um **texto** é representado pelo tipo de dado **`str` (string)**. Strings são **sequências de caracteres**, sempre **entre aspas simples (`'`) ou duplas (`"`).**

🔹 **Exemplo de strings:**
```python
# String com aspas duplas
print("Olá, Jornada de dados!")

# String com aspas simples
print('Python é incrível!')

# Concatenando strings (juntando textos)
print("Olá" + ", " + "Jornada de dados!")  # Saída: Olá, Jornada de dados!
```

🔹 **Manipulação de strings:**  
```python
mensagem = "Python é incrível!"
print(mensagem.upper())  # Converte para maiúsculas
print(mensagem.lower())  # Converte para minúsculas
print(len(mensagem))     # Retorna o tamanho da string
print(mensagem.replace("Python", "Data Science"))  # Substitui palavras
```

### **🚨 Erro ao concatenar `str` + `int`**
Strings **não podem ser concatenadas** diretamente com números (int). Se tentarmos, ocorre um erro:
```python
print("Minha idade é " + 25)  # ❌ Erro
```
🔴 **Erro:** `TypeError: can only concatenate str (not "int") to str`

📌 **Como corrigir?** Convertendo o número para string usando `str()`
```python
print("Minha idade é " + str(25))  # ✅ Correto
```
✅ **Saída:** `Minha idade é 25`

---

## 6. Operadores de comparação

Os **operadores de comparação** são usados para comparar dois valores e **retornam `True` ou `False`**, dependendo do resultado.

```python
print(10 > 5)   # Maior que → True
print(10 < 5)   # Menor que → False
print(10 >= 10) # Maior ou igual a → True
print(10 <= 9)  # Menor ou igual a → False
print(10 == 10) # Igualdade → True
print(10 != 5)  # Diferente de → True
```

## 7. Fluxo de controle

### **📌 Fluxo de Controle: `if` e `else` em Detalhes**
O **fluxo de controle** no Python permite que o código tome **decisões** com base em **condições**.  
O **`if`** verifica se uma condição é verdadeira e executa um bloco de código, enquanto o **`else`** define um bloco alternativo para quando a condição for falsa.

---

### **1️⃣ Como Funciona o `if` e `else`?**
A estrutura básica do **`if` e `else`** é:
```python
if condição:
    # Bloco executado se a condição for verdadeira
else:
    # Bloco executado se a condição for falsa
```
Cada bloco de código dentro do `if` e `else` **precisa estar indentado corretamente**.

---

### **2️⃣ Exemplo Simples**
```python
idade = 20

if idade >= 18:
    print("Você pode dirigir!")  # Esse código será executado porque a condição é verdadeira
else:
    print("Você não pode dirigir.")  # Esse código só executaria se a condição fosse falsa
```
✅ **Saída:** `Você pode dirigir!`  

🔹 **Explicação do Código:**  
- A variável `idade` tem o valor **20**.
- O `if` verifica **se `idade` é maior ou igual a 18**.
- Como 20 **é maior que 18**, a condição é verdadeira e **executa o bloco dentro do `if`**.
- O `else` **é ignorado** porque sua execução só ocorre **se a condição for falsa**.

---

### **3️⃣ Identação no Python**
A **identação** (espaço antes da linha de código) é fundamental no Python, pois define **quais linhas pertencem ao bloco do `if` ou do `else`**.

🔹 **Exemplo Correto:**
```python
idade = 16

if idade >= 18:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir.")  # A indentação está correta
```

❌ **Exemplo Incorreto (Sem Identação):**
```python
idade = 16

if idade >= 18:
print("Você pode dirigir!")  # ❌ Erro de identação
else:
print("Você não pode dirigir.")  # ❌ Erro de identação
```
🔴 **O Python retornará um erro de `IndentationError`!**

✅ **Regra Geral:** Sempre use **4 espaços** ou **Tab** para identação.

---

### **4️⃣ `if`, `elif` e `else` (Múltiplas Condições)**
Podemos adicionar condições intermediárias usando `elif` (**else if**).  

🔹 **Exemplo de `if` com `elif` e `else`**
```python
nota = 85

if nota >= 90:
    print("Aprovado com excelência!")
elif nota >= 70:
    print("Aprovado!")
else:
    print("Reprovado!")
```
✅ **Saída:** `Aprovado!`

🔹 **Explicação:**  
- Se `nota` for **maior ou igual a 90**, imprime `"Aprovado com excelência!"`.
- Se `nota` for **maior ou igual a 70**, mas **menor que 90**, imprime `"Aprovado!"`.
- Se `nota` for **menor que 70**, imprime `"Reprovado!"`.

---

## 8.Listas

Uma **lista** é uma estrutura de dados que armazena **múltiplos valores** em uma única variável. As listas são **ordenadas**, **mutáveis** (podemos modificar seus valores) e aceitam diferentes tipos de dados dentro dela.  

💡 **Exemplo mais próximo: Lista de Pessoas**  

```python
pessoas = ["Alice", "Bruno", "Carlos", "Diana"]
print(pessoas)  
# Saída: ['Alice', 'Bruno', 'Carlos', 'Diana']
```

---

### **📌 Como Criar uma Lista?**  
Para criar uma lista, usamos **colchetes `[ ]`** e separamos os itens por vírgula:  

```python
numeros = [1, 2, 3, 4, 5]  # Lista de números
nomes = ["Ana", "João", "Pedro"]  # Lista de strings
mistura = [10, "Texto", 3.14, True]  # Lista com diferentes tipos de dados
```

---

### **📌 Acessando Elementos de uma Lista**  
Os elementos de uma lista podem ser acessados pelos seus **índices**, começando do `0`:  

```python
print(pessoas[0])  # Saída: Alice (primeiro elemento)
print(pessoas[2])  # Saída: Carlos (terceiro elemento)
```

Podemos também acessar **de trás para frente** usando **índices negativos**:  

```python
print(pessoas[-1])  # Saída: Diana (último elemento)
print(pessoas[-2])  # Saída: Carlos (penúltimo elemento)
```

---

### **📌 Modificando Listas**  
As listas são **mutáveis**, ou seja, podemos alterar seus valores:  

```python
pessoas[1] = "Beatriz"  # Substituindo 'Bruno' por 'Beatriz'
print(pessoas)  
# Saída: ['Alice', 'Beatriz', 'Carlos', 'Diana']
```

---

### **📌 Adicionando e Removendo Itens**  

- **Adicionar um item ao final da lista:**  
```python
pessoas.append("Eduardo")  
print(pessoas)  
# Saída: ['Alice', 'Beatriz', 'Carlos', 'Diana', 'Eduardo']
```

- **Remover um item específico:**  
```python
pessoas.remove("Carlos")  
print(pessoas)  
# Saída: ['Alice', 'Beatriz', 'Diana', 'Eduardo']
```

- **Remover o último item da lista:**  
```python
pessoas.pop()  
print(pessoas)  
# Saída: ['Alice', 'Beatriz', 'Diana'] (Eduardo foi removido)
```

---

### **📌 Saber o Tamanho da Lista (`len()`)**  

A função `len()` retorna a quantidade de itens dentro de uma lista:  

```python
data = [10, 20, 30, 40]
print(len(data))  # Saída: 4
```
