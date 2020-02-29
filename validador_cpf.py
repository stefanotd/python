cpf = input('Digite um cpf: ')
novo_cpf = ''
result1 = result2 = 0
digito1 = digito2 = ''

if cpf.isnumeric():
    cpfnro = int(cpf)

    for posicao,ind1 in enumerate(range(10,1,-1)):
        novo_cpf = novo_cpf+cpf[posicao]
        result1=result1+int(cpf[posicao])*ind1

    digito1 = 11 - ( result1 % 11)
    if digito1>9:
        digito1 = 0
    novo_cpf = novo_cpf+str(digito1)

    for posicao,ind2 in enumerate(range(11,1,-1)):
        result2 = result2 + int(cpf[posicao])*ind2

    digito2 = 11 - (result2 % 11)
    if digito2 > 9:
        digito2 = 0
    novo_cpf = novo_cpf+str(digito2)

    if cpf == novo_cpf:
        print('Cpf é válido!')
    else:
        print('Cpf inválido!')

else:
    print('Digite somente números!')
