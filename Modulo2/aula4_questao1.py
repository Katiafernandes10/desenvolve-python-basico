#1 - Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura),
#  bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado.

#leitura de dados (entrada)
comprimento = int(input("Digite o comprimento: ") )
largura = int (input("Digite a largura: "))
preco_m2 = float(input("valor do me2: "))

#Processamento
area = comprimento * largura #m2
preco_total = area * preco_m2

#Impressão de dados (saída)
print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f}")
