'''
Regras:
Iniciar com letra
Pode conter números
Separar o nome com underline _
Sempre ser com letras minúsculas
'''

nome = 'Harvy Spector'
idade = 32
altura = 1.80
maior_de_idade = idade >= 21
peso = 80

#Exercício

#Calcule o IMC
imc = peso/(altura**2)

print(nome, 'possui', idade, 'de idade, e seu IMC é', imc)