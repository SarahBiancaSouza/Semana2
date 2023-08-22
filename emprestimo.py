valor_casa = float(input('Valor da casa?'))
salario = float(input('Quanto você ganha por mês?'))
tempo_pagamento = int(input('Em quantos meses?'))
#se o valor da prestaçao mensal for maior que 30% do salario devera ser negado

valor_prestacao = (valor_casa/tempo_pagamento)
porcentagem_salario = (salario/100)*30

if(valor_prestacao > porcentagem_salario):
    print('Emprestimo negado')
else:
    print('Emprestimo APROVADO!')


