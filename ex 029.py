velo=int(input('Velocidade permitida:'))
print('Velocidade atual {}'.format(velo))
if velo > 80 :
    print('Você não foi multado')
else:
    print('Você foi multado')
multa=(velo-80)*7
print('Sua multa foi de {}'.format(multa))