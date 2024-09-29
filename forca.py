import random

clear = "\n" * 1
stars = "***************"

def jogar():
    mensagem_abertura()
    palavra_secreta = carrega_palavras()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    letras_erradas = []

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        print(clear)
        chute = pede_chute()
        
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros+=1
            print(clear)
            print(stars)
            desenha_forca(erros)
            print("OH NÃO! A PALAVRA NÃO TEM '{}'. FALTAM MAIS *{}* TENTATIVAS.".format(chute,6 - erros))
            letras_erradas.append(chute)
            #print(stars)
            print("VOCÊ JÁ TENTOU: {}".format(letras_erradas))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print(clear)
        print("***************\nPARABÉNS, VOCÊ ACERTOU! A PALAVRA ERA => {} !".format(palavra_secreta))
    else:
        print(clear)
        print("***************\nQUE PENA, VOCÊ PERDEU! A PALAVRA ERA => {} !".format((palavra_secreta)))

def mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

def carrega_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("***************\nCHUTE UMA LETRA: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("________")
    print("|/     |")

    if(erros==1):
        print("|      O  ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("|         ")

    if (erros==2):
        print("|      O  ")
        print("|      |  ")
        print("|      |  ")
        print("|         ")
        print("|         ")

    if (erros==3):
        print("|      O  ")
        print("|     /|  ")
        print("|      |  ")
        print("|         ")
        print("|         ")

    if (erros==4):
        print("|      O  ")
        print("|     /|\ ")
        print("|      |  ")
        print("|         ")
        print("|         ")

    if (erros==5):
        print("|      O  ")
        print("|     /|\ ")
        print("|      |  ")
        print("|     /   ")
        print("|         ")

    if (erros==6):
        print("|      O  ")
        print("|     /|\ ")
        print("|      |  ")
        print("|     / \ ")
        print("|         ")

if(__name__ == "__main__"):
    jogar()