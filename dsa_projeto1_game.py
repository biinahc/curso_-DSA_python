import random
import unicodedata
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_hangman(chances):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

def eh_letra_valida(letra):

    letra_normalizada = unicodedata.normalize('NFD', letra).encode('ascii', 'ignore').decode('utf-8')
    return letra.isalpha() and letra == letra_normalizada

def game():
    limpa_tela()
    print("\nBem-vindo ao jogo da forca 🎮!")
    print("Adivinhe a palavra abaixo:")
    print("Vamos jogaaaar :)\nc")
    
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'pitaya', 'kiwi', 'rambutan', 'caju', ' pequi', 'sapoti', 'umbu', 'bacuri', 'acerola', 'alfarroba']
    
    palavra = random.choice(palavras)
    
    lista_letras_palavras = [letra for letra in palavra]
    
    tabuleiro = ["_"] * len(palavra)
    
    chances = 6
    
    letras_tentativas = []
    
    while chances > 0:
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")
        
        tentativa = input("\nDigite uma letra: ").lower().strip()
        
        if len(tentativa) != 1 or not eh_letra_valida(tentativa):
            print("Entrada inválida! Digite apenas uma letra sem acentos.")
            continue
        
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue
        
        letras_tentativas.append(tentativa)
        
        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")
            
            for indice in range(len(lista_letras_palavras)):
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
            
            if "_" not in tabuleiro:
                print("\nVocê VENCEEEEEU 🎉🎉! A palavra era: {}".format(palavra))
                break
        else:
            print("Ops. Essa letra não está na palavra :(!")
            chances -= 1
    
    if "_" in tabuleiro:
        print("\nGAMER OVER! Você perdeu tururururu 😭! A palavra era: {}.".format(palavra))

if __name__ == "__main__":
    game()
    print("\nParabéns! Obrigada por ver e testar meu aprendizado em programação em Python com a DSA.🎮 :)\n")
