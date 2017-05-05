from random import randint
a = (randint(0,99))

print ('eu escolhi um número de 0 a 99')

b = 'inicio'
i = 0
while (a!=b):
  b = int (input('diga, qual o número que escolhi?'))
  if a > b:
    print ('meu número é MAIOR que esse')
  if a < b:
    print ('meu número é MENOR que esse')
  i+=1

print ('Parabéns, eu pensei no número %0.1i' %a)
print ('você acertou em %0.1i tentativas' %i)
