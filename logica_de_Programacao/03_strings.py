"""Strings são textos em Python, qualquer palavra ou caracter que estiver dentro de aspas,
 sejam elas simples ou duplas, será tratado como string pelo Python"""

print('Isso é uma string')

#Caso eu queira usar aspas dentro de uma string, devo utilizar da seguinte forma:

print('Isso é uma "string"') # Diferenciando as aspas simples com as duplas ou vice-versa (Este é o mais indicado)

print('Isso é uma \'string\'') # Usando barra invertida para ignorar as aspas

# Caso você queira que o Python ignore os caracteres especiais que possuem função como o barra \, basta colocar uma letra antes da string

print(r'Isso é uma \"string\"')