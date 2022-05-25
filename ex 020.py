from random import shuffle
n1=str(input('aluno 01'))
n2=str(input('Aluno 02'))
n3=str(input('Aluno 03'))
n4=str(input('Aluno 04'))
lista=[n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)