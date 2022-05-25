dia=int(input('Quantos dias alugados?'))
km=int(input('Quantos km rodados?'))
pago= (dia * 60)+(km*0.15)
print('O total a pagar é R${}'.format(pago))