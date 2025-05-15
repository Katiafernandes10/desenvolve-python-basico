#2 - Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 
#Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. 

# Leitura de dados (entrada)
fahrenheit = int (input("Digite a temperaturaem F: "))

#Processamento
celsius = (fahrenheit -32) * 5/9

#Impressão de dados (saída)
print(f"{fahrenheit} graus Fahrenhet são {int(celsius)} graus Celsius")