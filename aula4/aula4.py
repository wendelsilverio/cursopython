"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booliano/lógico - True/False 10 == 10
"""
print('Luiz', type('Luiz'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))

# Casting - Converte um tipo em outro
print('Luiz', type('Luiz'), bool('Luiz'))
print('10', type('10'), type(int('10')))
# print('Luiz', int('Luiz'))  # Erro: ValueError: invalid literal for int() with base 10: 'Luiz'
print('Luiz', float('10.5'))
print('Luiz', float('10'))

# Exercício ################

# String: nome
print('Wendel Silvério', type('Wendel Silvério'))

# Idade: int
print(42, type(42))

# Altura: float
print(1.73, type(1.73))

# É maior de idade 10 > 20
print(42 > 18, type(42 > 18))
