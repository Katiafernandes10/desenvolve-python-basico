#3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado 
# multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a 
# quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:

#leitura de dados (entrada)

produto1 = input("Digite o nome do produto 1: ")
p1= float(input("Digite o valor do produto 1: "))
q1 = int(input("Digite a quantidade do produto 1: "))
total1 = p1 * q1
print (total1)
produto2 = input("Digite o nome do produto 2: ")
p2= float(input("Digite o valor do produto 2: "))
q3 = int(input("Digite a quantidade do produto 2: "))
total2 = p2 * q3
print (total2)
produto3 = input("Digite o nome do produto 3: ")
p3= float(input("Digite o valor do produto 3: "))
q3 = int(input("Digite a quantidade do produto 3: "))
total3 = p3 * q3
print(total3)

#processamento 
Total_geral = total1+total2+total3

#impressão de dados (saída)
print(f"Total: R${Total_geral:,.2f}")
