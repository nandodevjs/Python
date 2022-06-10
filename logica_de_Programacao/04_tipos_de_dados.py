"""
Str - String = Texto
Int - Inteiro = É um número inteiro, pode ser zero, positivo ou negativo
Float - Flutuante = É um número que pode ser quebrado com vírgula ou ponto. Ex: 1,0 OU 1.0
Bool - Booleano = verdadeiro ou falso = True or False 10 == 10? True
"""
print(type('Olá'))
print(type(10))
print(type(1.5))
print(type(10 == 10))

#converter os tipos
teste = 10.8
print(type(teste))

teste = int(teste)
print(type(teste))
print(teste)

#Exercícios:

#String: Nome
print('Harvy Spector', type('Harvy Spector'))
#Idade: int
print(32, type(32))
#Altura: Float
print(1.80, type(1.80))
#Você é maior de idade?
print(32 >= 21, type(32 >= 21))