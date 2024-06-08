'''
PROJETO 3 - Medidor de Velocidade

Considerando a velocidade máxima permitida de 80km/h em uma determinada rua.
Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve, grave ou gravíssima.
Se o motorista estiver abaixo da velocidade máxima, seu programa deve exibir "não houve multa";
caso esteja até 10km/h acima, deve exibir: "levou multa leve";
se for entre 11 a 20km/h acima, exibir: "levou multa grave";
e acima de 20km/h da velocidade máxima, exibir: "levou multa gravíssima".
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
while True: # Laço opcional só para executar o código apenas uma vez.
    velocidade_maxima = 80
    velocidade = 0

    velocidade = int(input('Qual a velocidade? '))

    if velocidade <= velocidade_maxima:
        print('Não houve multa.')
    elif velocidade <= velocidade_maxima + 10:
        print('Levou multa leve.')
    elif velocidade <= velocidade_maxima + 20:
        print('Levou multa grave.')
    elif velocidade >= velocidade_maxima + 21:
        print('Levou multa gravíssima.')