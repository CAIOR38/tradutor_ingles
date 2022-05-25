numero=int(input('Informe um numero'))
u= numero // 1 % 10
d= numero // 10*10
c= numero // 100*10
n=str(numero)
print('Analisando o numero {}'.format(numero))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
#print('Milhar : {}'.format(n[0]))