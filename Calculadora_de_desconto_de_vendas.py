#UM dos meus primeiros projetinhos em Python! Calculadora de Desconto Simples 🐍
# Estou no 2º semestre e tô super animado com isso!


print("=== Calculadora de Desconto para Vendas ===")
print("Use ponto para decimais (ex: 99.90)\n")


try:
    valor_original = float(input("Digite o Valor do produto (R$): "))
    desconto_porcentagem = float(input("Digite o Desconto (%) : "))
   
    desconto_valor = valor_original * (desconto_porcentagem / 100)
    valor_final = valor_original - desconto_valor
   
    print("\n=== Resultado ===")
    print(f"Valor original: R$ {valor_original:.2f}")
    print(f"Desconto: {desconto_porcentagem}% → R$ {desconto_valor:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print(f"Você economizou: R$ {desconto_valor:.2f} 🎉")


except ValueError:
    print("Ops! Digite só números válidos, por favor.")

