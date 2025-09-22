import pandas as pd
import matplotlib.pyplot as plt

# Exemplo de dados financeiros
dados = {
    "Data": ["2025-09-01", "2025-09-02", "2025-09-03", "2025-09-04"],
    "Descrição": ["Venda Produto A", "Compra Matéria Prima", "Venda Produto B", "Pagamento Salário"],
    "Tipo": ["Receita", "Despesa", "Receita", "Despesa"],
    "Valor": [500, 200, 300, 150]
}

# Criar DataFrame
df = pd.DataFrame(dados)
df["Data"] = pd.to_datetime(df["Data"])

# Calcular total de receitas e despesas
receitas = df[df["Tipo"] == "Receita"]["Valor"].sum()
despesas = df[df["Tipo"] == "Despesa"]["Valor"].sum()
lucro = receitas - despesas

print(f"💰 Total de Receitas: R$ {receitas}")
print(f"📉 Total de Despesas: R$ {despesas}")
print(f"📊 Lucro/Prejuízo: R$ {lucro}")

# Gráfico de receitas vs despesas
resumo = df.groupby("Tipo")["Valor"].sum()
resumo.plot(kind="pie", autopct='%1.1f%%', colors=["#4CAF50", "#F44336"], startangle=90)
plt.title("Receitas vs Despesas")
plt.ylabel("")
plt.show()
