numero=int(input('Vamos escolher quem começa o jogo:'))
resultado = numero % 2
print ('O resultado é {}'.format(resultado))
if resultado ==0:
    print('par')
else:
    print('impar')



