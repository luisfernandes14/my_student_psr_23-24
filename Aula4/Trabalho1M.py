#!/usr/bin/env python3
# --------------------------------------------------
# Typing test program.
# Miguel Bento Simoes.
# Nuno Seabra
# Luís Fernandes
# PSR - Parte 4
# --------------------------------------------------

# Imports 

import argparse
from time import time
import datetime
from readchar import readkey
import random
import string
import nltk
from nltk.corpus import words
from collections import namedtuple
from colorama import Fore,Back,Style

# NamedTuple chamado Input que possui três campos: 'requested', 'received' e 'duration'



# Functions

def aguardar_tecla():

    print("Pressione uma tecla para começar o desafio...")

    digitado = readkey()


def generate_random_word():

    word_list = words.words()
    return random.choice(word_list)
   

def caracter_function(args):
    Input = namedtuple('Input', ['requested', 'received', 'duration'])

    tentativa=0
    bem_sucedido = 0

    start_time = time() 

    while True:

        tempo_atual = time()
        tempo_decorrido = int(tempo_atual - start_time )

        if tempo_decorrido >= args.max_value:
            break  

        random_ascii = random.randint(97,122)
        random_caracter = chr(random_ascii)

        print(f"Digite: {random_caracter} : ") 
        ti = time()

        key = readkey()

        tf = time()
        duration = tf-ti
        input_ascii = ord(key)

        if input_ascii == 32:

            break

        elif key == random_caracter:
            print(Fore.GREEN + f"Correto" + Fore.WHITE + ", voce inseriu! " + Fore.GREEN + f"{key}" + Fore.WHITE)
            bem_sucedido += 1
        else:
            print(Fore.RED+"Incorreto" + Fore.WHITE + ". Tente novamente.")

        tentativa +=1
        input_record = Input( requested = random_caracter, received = key, duration = duration)    

    print(f"\nEm {tentativa} tentativas voce acertou em: {bem_sucedido}, em {tempo_decorrido} segundos.") 

    print(input_record.requested)  
    print(input_record.received)   
    print(input_record.duration)        


def main():



    bem_sucedido = 0
    tentativa=0

    # Configurar o parser de argumentos de entrada

    parser = argparse.ArgumentParser(description="Definição do modo de teste")
    parser.add_argument("-utm", "--use_time_mode", action="store_true",
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.")
    parser.add_argument("-mv", "--max_value", type=int,
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.")
    parser.add_argument("-uw", "--use_words", action="store_true",
                        help="Usar o modo de digitação de palavras em vez de digitação de caracteres individuais.")
    
    args = parser.parse_args()

    #Printar os argumentos

    print("Tempo Máximo:", args.max_value)
    print("Time mode:", args.use_time_mode)
    print("Use words:", args.use_words)

    tempo_decorrido = 0

    aguardar_tecla()

    if not args.use_words and args.use_time_mode:

        print("Função de caracter e tempo maximo:")

        start_time = time() 

        while True:

            tempo_atual = time()
            tempo_decorrido = int(tempo_atual - start_time )

            if tempo_decorrido >= args.max_value:
                break
            

            random_ascii = random.randint(97,122)
            random_caracter = chr(random_ascii)

            print(f"Digite: {random_caracter} : ") 

            #user_input = input(f"Digite: {random_caracter} : ") 
            #input_ascii = ord(readkey(user_input))
            key = readkey()
            input_ascii = ord(key)

            if input_ascii == 32:

                break

            elif key == random_caracter:
                print(Fore.GREEN + f"Correto" + Fore.WHITE + ", voce inseriu! " + Fore.GREEN + f"{key}" + Fore.WHITE)
                bem_sucedido += 1
            else:
                print("Incorreto. Tente novamente.")

            tentativa +=1    

        print(f"Em {tentativa} tentativas voce acertou em: {bem_sucedido}, em {tempo_decorrido} segundos.")        

    elif not args.use_words and not args.use_time_mode:  

        caracter_function(args) 

    elif  args.use_words and args.use_time_mode:

            print("Função de palavra e tempo maximo:")  

            start_time = time()
            print("Função de palavra")

            generate_random_word()
        

            while True:

                tempo_atual = time()
                tempo_decorrido = int(tempo_atual - start_time )

                if tempo_decorrido >= args.max_value:
                    break

                print(f"tempo decorrido {tempo_decorrido} ")

                random_word = generate_random_word()
                user_input = input(f"Digite {random_word} : ")

                if user_input.lower() == random_word:

                    print(f"Correto, voce inseriu! {user_input}")
                    bem_sucedido += 1

                else:

                    print("Incorreto!")

                tentativa += 1    

            print(f"Em {tentativa} tentativas voce acertou em: {bem_sucedido}, em {tempo_decorrido} segundos.")

    elif   args.use_words and not args.use_time_mode: 

            print("Função de palavra e input maximo:")  

            start_time = time()

            generate_random_word()
        
            while True:

                tempo_atual = time()

                tempo_decorrido = int(tempo_atual - start_time )

                if tentativa >= args.max_value:
                    break

                random_word = generate_random_word()
                user_input = input(f"Digite {random_word} : ")

                if user_input.lower() == random_word:

                    print(f"Correto, voce inseriu! {user_input}")
                    bem_sucedido += 1

                else:

                    print("Incorreto!")  

                tentativa += 1 

            print(f"De {tentativa} tentativas voce acertou em: {bem_sucedido}, com um tempo de jogo de: {tempo_decorrido} segundos.")        


if __name__ == "__main__":
    main()

    # python3 backupinicial.py -utm -mv 10 -uw 
