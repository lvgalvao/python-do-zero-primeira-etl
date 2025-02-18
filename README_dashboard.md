Aqui está um **README** detalhado sobre a biblioteca **Plotly**, cobrindo desde a introdução até a utilização e principais métodos:

---

## 📊 Plotly - Biblioteca para Visualização de Dados Interativa

### 🔹 O que é o Plotly?
O **Plotly** é uma biblioteca poderosa para visualização de dados em Python, oferecendo gráficos interativos de alta qualidade. Ele suporta uma ampla variedade de gráficos, como:
- Gráficos de linha, barras, dispersão, pizza e histograma
- Mapas geoespaciais
- Gráficos 3D e de superfície
- Dashboards interativos
- Gráficos estatísticos e financeiros

O grande diferencial do **Plotly** é a **interatividade**, permitindo zoom, hover e filtragem diretamente nos gráficos.

---

## 🛠️ Como instalar o Plotly?

Para instalar a biblioteca Plotly, basta rodar:

```bash
pip install plotly
```

Se for usar em Jupyter Notebook, também é recomendável instalar **jupyter-dash** para gráficos interativos:

```bash
pip install jupyter-dash
```

---

## 🚀 Como utilizar o Plotly?

O **Plotly** possui duas principais abordagens:
1. `plotly.express` → Interface de alto nível (mais simples e rápida)
2. `plotly.graph_objects` → Interface mais detalhada para personalização avançada

### 🔹 Exemplo básico com `plotly.express`
```python
import plotly.express as px
import pandas as pd

# Criando um DataFrame fictício
df = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valores": [10, 20, 30, 40]
})

# Criando um gráfico de barras interativo
fig = px.bar(df, x="Categoria", y="Valores", title="Gráfico de Barras Interativo")
fig.show()
```

**Principais características**:
✔ Simplicidade na criação de gráficos  
✔ Customização automática  
✔ Menos código necessário  

---

## 🔹 Métodos e Funções do `plotly.express`

O `plotly.express` fornece uma API de alto nível para gerar gráficos com menos código. Aqui estão alguns dos principais métodos:

### 📊 1. Gráficos de Linhas (`px.line`)
```python
fig = px.line(df, x="Categoria", y="Valores", title="Gráfico de Linha")
fig.show()
```

### 📊 2. Gráficos de Barras (`px.bar`)
```python
fig = px.bar(df, x="Categoria", y="Valores", title="Gráfico de Barras")
fig.show()
```

### 📊 3. Gráficos de Dispersão (`px.scatter`)
```python
fig = px.scatter(df, x="Categoria", y="Valores", title="Gráfico de Dispersão")
fig.show()
```

### 📊 4. Gráficos de Pizza (`px.pie`)
```python
fig = px.pie(df, names="Categoria", values="Valores", title="Gráfico de Pizza")
fig.show()
```

### 📊 5. Gráficos de Densidade (`px.density_heatmap`)
```python
fig = px.density_heatmap(df, x="Categoria", y="Valores", title="Heatmap")
fig.show()
```

---

## 🔹 Métodos e Funções do `plotly.graph_objects`
Se precisar de mais controle sobre os gráficos, pode usar `plotly.graph_objects`:

### 📌 Criando um Gráfico de Linhas com `graph_objects`
```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Categoria"], y=df["Valores"], mode="lines+markers", name="Linha"))
fig.update_layout(title="Gráfico de Linha com graph_objects")
fig.show()
```

✔️ Permite personalizações avançadas  
✔️ Ideal para gráficos mais detalhados  

---

```python
import plotly.express as px

# Convertendo a coluna "mes_compra" para string
df["mes_compra_str"] = df["mes_compra"].astype(str)

# Gráfico 1: Total de Compra por Mês
fig1 = px.bar(df.groupby("mes_compra_str")["total_de_compra"].sum().reset_index(),
              x="mes_compra_str",
              y="total_de_compra",
              title="Total de Compra por Mês",
              labels={"mes_compra_str": "Mês", "total_de_compra": "Total de Compra (USD)"},
              text_auto=True)
fig1.show()

# Gráfico 2: Distribuição de Lucro vs Prejuízo
fig2 = px.pie(df, names="resultado_operacao",
              title="Distribuição de Lucro vs Prejuízo",
              hole=0.3)
fig2.show()

# Gráfico 3: Evolução do Preço do Bitcoin ao longo do Tempo
fig3 = px.line(df, x="data_compra", y="preco_btc",
               title="Evolução do Preço do Bitcoin ao longo do Tempo",
               labels={"data_compra": "Data da Compra", "preco_btc": "Preço do BTC (USD)"},
               markers=True)
fig3.show()
```

