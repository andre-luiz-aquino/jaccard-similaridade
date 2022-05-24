cliente1 = []
cliente2 = []
desconto = 0
Qtd_produtos = int(input("Quantos produtos o cliente 1 comprou? "))
for produto in range(Qtd_produtos):
  produto = input("Qual produto o cliente 1 levou?  ")
  cliente1.append(produto)
Qtd_produtos = int(input("Quantos produtos o cliente 2 comprou? "))
for produto in range(Qtd_produtos):
  produto = input("Qual produto o cliente 2 levou?  ")
  cliente2.append(produto)

c1 = set(cliente1)
c2 = set(cliente2)

if len(cliente1) >= 1 or len(cliente2) >=1:
  similaridade = float(len(c1.intersection(c2)) / len(c1.union(c2))) * 100
  diferença = (c1.difference(c2))
if similaridade <= 30:
  desconto = (Qtd_produtos >=1) * 15
  print("Similaridade foi de,", similaridade)
  print("O desconto do produto",diferença, "recomendado é de ",desconto)
elif similaridade > 30 and similaridade <=49:
  desconto = (Qtd_produtos >=1) * 10
  print("Similaridade foi de,", similaridade)
  print("O desconto do produto",diferença, "recomendado é de",desconto)
elif similaridade >= 50 and similaridade <= 99:
  print("Produtos recomendados: ", diferença)
else:
  print("Similaridade foi de 100%, não há recomendações.")