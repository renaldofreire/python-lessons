# O volume de uma esfera com raio r é *****. 
# Qual é o volume de uma esfera com raio 5?

msg_abertura = print('Calculadora de Volume de Esfera.')
valor_raio = input('Qual o valor do raio? ')

total_raio = int(valor_raio) ** 3

vol_pi = ((4 * int(total_raio)) / 3) * 3.14
arredonda_pi = round(vol_pi,2)


print('O volume aproximado de unidades cúbicas é ' + str(arredonda_pi) + '.')
#print(total_raio)


