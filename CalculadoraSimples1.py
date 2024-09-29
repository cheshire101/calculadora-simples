import random
numero1=0 
numero2=0
resultado=0
operacao=''

numero1=int(input('digite o primeiro valor: '))
operacao=input('digite a operacao:')
numero2=int(input('digite o segundo valor: '))

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
else:
    resultado='Operacao invalida'
    
print(str(numero1)  + ' ' + str(operacao) + ' ' + str(numero2) + '=' + str(resultado))

#python tem uma especie de hierarquia, deixe sempre o comando na linha anterior do comando acima.

#trocando de programa

base=0
altura=0
lado=0
pi=3,14
raio=0
diagonalMaior=0
diagonalMenor=0
resultado2=0
calculo=''

calculo=input(str('Digite a Operacao (Triangulo, Losango, etc...): '))

if calculo == 'triangulo':
    base=float(input('DIgite a base'))
    altura=float(input('Digite a altura'))
    reultado=(base*altura)/2
    print('a area do quadrado é: ' + resultado)