# ACERTE O NÚMERO DE 1 A 10!

'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja acertado.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.
'''

'''
-----------------------------------------------------------
Método 5Q's para montar um algoritmo:

Analise criticamente o problema e descubra:
(Tente explicar o problema para si e investigue até compreendê-lo por completo.)

1. Quais são os dados de entrada (input) necessários?
2. O que devo fazer com estes dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
-----------------------------------------------------------
'''

'''
1. Gerar um valor aleatório de 1 a 10 e armazená-lo. Depois solicitar um número ao usuário.
2. Comparar o número dado pelo usuário com o gerado pelo programa.
3. O usuário deverá informar um número cujo valor esteja entre 1 até 10.
4. Uma comparação do chute do usuário com o valor aleatório gerado e,
    Se o chute for maior que o valor gerado, exibir "chutou alto" e solicitar novamente,
    Se o chute for menor que o valor gerado, exibir "chutou baixo" e solicitar novamente,
    Se o chute for igual ao valor gerado, exibir "acertou!" e voltar ao passo 1.
5. input numero_aleatorio de 1 a 10
    input chute
    if chute < numero:
        print('Chutou baixo!')
    if chute > numero:
        print('Chutou alto!)
    if chute = numero:
        print('Você acertou!)
'''

while True:
    import random

    numero_aleatorio = random.randint(1, 10) # Gera um número de 1 a 10
    acertou = False
    while acertou == False:
    
        chute = int(input('Chute um valor de 1 a 10: '))

        if chute < numero_aleatorio:
            print('Chutou baixo!')
        elif chute > numero_aleatorio:
            print('Chutou alto!')
        elif chute == numero_aleatorio:
            acertou = True
            print('Você acertou!')

    jogar_novamente = input('Você quer jogar novamente? (s/n): ')
    if jogar_novamente.lower() != 's':
        break