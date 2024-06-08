# FATORIAL DE UM NÚMERO
# Usando o método 5Q's do Jhonatan
# Este projeto pode ser feito em qualquer outra linguagem

'''
Crie um programa que recebe um número e imprime o seu fatorial.

---------------------------------------------------------
Método 5Q's para montar um algoritmo:

Analise criticamente o problema e descubra:
(Tente explicar o problema para si e investigue até compreendê-lo por completo.)

1. Quais são os dados de entrada (input) necessários?
2. O que devo fazer com estes dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
---------------------------------------------------------
'''

'''
Aplicando o método...

1. Um valor em número.
2. Calcular o fatorial de um número que for informado ao programa e o exibir na tela.
3. O número deve ser um valor positivo e inteiro.
4. A exibição do valor do fatorial do número informado.
5. input numero = inteiro e > 0
    fatoral = 1
    loop de 1 a numero
        fatorial = fatorial * numero
    print(fatorial)
'''

numero = int(input('Digite um número: '))

while numero < 0:
    print('O número deve ser positivo e inteiro.')
    numero = int(input('Digite um número: '))

if numero > 0:
    fatorial = 1
    for item in range(1,numero + 1):
        fatorial = fatorial * item
    print('O resultado é: ')
    print(fatorial)

'''
-----------------------------------------------------------
--------------------- CURIOSIDADE -------------------------
-----------------------------------------------------------

Em Python, você pode verificar se um número é par ou ímpar usando o operador de módulo %, que retorna o resto de uma divisão.
Neste código, numero % 2 calcula o resto da divisão de numero por 2. Se o resto for 0, isso significa que numero é divisível por 2 e, portanto, é par. Se o resto não for 0, isso significa que numero não é divisível por 2 e, portanto, é ímpar.

------------------------------------------
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')
------------------------------------------

ou

------------------------------------------
if numero % 2 != 0:
    print('O número é ímpar.)
else:
    print('O número é par.)
------------------------------------------

Os códigos são redundantes, caso precise verificar se é par ou ímpar, basta um deles.
Só muda o operador de verificação.
--------------------------------------------------------
'''




