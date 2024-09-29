import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_tentativas = 0
rodada = 1

print("Qual nivel de dificuldade?")
print("(1)FACIL /// (2)MEDIO /// (3)DIFICIL")

nivel=int(input("Defina o Nível: "))

if(nivel==1):
    total_tentativas=20
elif(nivel==2):
    total_tentativas=10
else:
    total_tentativas=5

for rodada in range(1,total_tentativas+1):
    print("Tentativa {} de {}".format(rodada,total_tentativas) )
    chute_str = input("Digite um número de 1 a 100: ")
    chute = int(chute_str)
    print("Você digitou ", chute_str)

    if(chute<1 or chute>100 ):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute==numero_secreto
    maior = chute>numero_secreto
    menor = chute<numero_secreto

    if (acertou):
        print("*********************************")
        print("Você acertou!")
        print("*********************************")
        break
    else:
        if(maior):
            print("*********************************")
            print("Você errou, o número secreto é *** MENOR ***!")
            print("*********************************")
        if(menor):
            print("*********************************")
            print("Você errou, o número secreto é *** MAIOR ***!")
            print("*********************************")

print("*********************************")
print("Fim de jogo.")
print("*********************************")
