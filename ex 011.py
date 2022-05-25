altura=float(input('Digite a altura da parede:'))
largura=float(input('Digite a largura da parede:'))
área= altura*largura
print('A sua parede tem a dimensão de {}*{} e sua área é {}'.format(altura,largura,área))
tinta=área/2
print('Para pintar essa parede você precisa de {} baldes e tinta'.format(tinta))