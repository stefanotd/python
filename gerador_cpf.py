"""
Gerar CPFs

"""
from random import randint
numero_aleatorio = str(randint(100000000,900000000))


novo_cpf = numero_aleatorio
result1 = result2 = 0
digito1 = digito2 = ''

for posicao,ind1 in enumerate(range(10,1,-1)):
    result1=result1+int(novo_cpf[posicao])*ind1

digito1 = 11 - ( result1 % 11)
if digito1>9:
    digito1 = 0
novo_cpf = novo_cpf+str(digito1)

for posicao,ind2 in enumerate(range(11,1,-1)):
    result2 = result2 + int(novo_cpf[posicao])*ind2

digito2 = 11 - (result2 % 11)
if digito2 > 9:
    digito2 = 0
novo_cpf = novo_cpf+str(digito2)

print(novo_cpf)


