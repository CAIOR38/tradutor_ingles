#calculadora de IMC
alt=float(input('qual a sua altura?'))
peso=float(input('qual o seu peso?'))
imc=peso/(alt*2)
print('seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif imc <= 25:
    print('peso ideal')
elif imc <= 30:
    print('sobrepeso')
elif imc <= 40:
    print('obesidade')
elif imc >= 40:
    print('obesidade mórbida')