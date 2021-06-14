"""
Variáveis
Iniciar com letra, pode conter números, separar _, letra minúsculas
"""
nome = 'Luiz Otávio'
idade = 32  # int
altura = 1.80  # float
e_maior = idade > 18  # bool
peso = 80

imc = peso / altura ** 2

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
