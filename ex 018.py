from math import radians,sin, cos, tan
an=float(input('Digite o ângulo que você deseja:'))
seno=sin(radians(an))
print('O ângulo de {} tem o Seno de {:4f}'.format(an,seno))
cosseno=cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:4f}'.format(an,cosseno))
tangente= tan(radians(an))
print('O ângulo da TANGENTE é {:4f}'.format(an,tangente))