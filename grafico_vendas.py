import matplotlib.pyplot as plt

# Dados de exemplo
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [120, 90, 150, 80, 200]

def gerar_grafico_vendas(meses, vendas):
    plt.figure(figsize=(10, 6))
    plt.bar(meses, vendas, color='royalblue')
    plt.xlabel('Mês')
    plt.ylabel('Vendas (em unidades)')
    plt.title('Vendas Mensais')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    gerar_grafico_vendas(meses, vendas)
