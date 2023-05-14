import random
from palavra import palavras 
palavra_secreta = random.choice(palavras)
letras = []
chances = 3


print("*** BEM VINDO AO JOGO DA FORCA***") #Apresentação do jogo
print("Adivinha a palavra abaixo: ")

while True:                                 #Aqui fica a lógica por trás do jogo, onde é responsável por preencher as letras de acordo com a palavra secreta que é aleatória
    for letra in palavra_secreta:
        if letra.lower() in letras:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"<-- Você tem {chances} chances")  #Mostra quantas chances o jogador ainda tem
    tentativa = input("Escolha sua letra: ")  #Opção para o usuário inserir a sua tentativa de letra
    letras.append(tentativa.lower())          
    if tentativa.lower() not in palavra_secreta.lower():  #Verifica se a tentativa do usuário está dentro da palavra secreta, caso não esteja, reduz a quantidade de chances
        chances -= 1
        
    ganhou = True
    for letra in palavra_secreta:     #Verifica se a letra está dentro da palavra secreta, caso não esteja, irá retornar como falsa a vitória
        if letra.lower() not in letras:
            ganhou = False
            
    if chances == 0 or ganhou:   #Encerra o jogo caso o usuário acerte a palavra secreta ou suas tentativas chegem a 0
        break

if ganhou:
    print(f"Parabéns você ganhou. A palavra era: {palavra_secreta}") #Mensagem por acertar a palavra
else:
    print(f"Você perdeu! A palavra era: {palavra_secreta}") #Mensagem por errar a palavra em todas as tentativas

