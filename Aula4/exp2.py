#!/usr/bin/env python3

import argparse
from time import time
import datetime
import random
import string
from nltk.corpus import words
from collections import namedtuple
from pprint import pprint
from readchar import readkey
import readchar
from datetime import datetime
from colorama import Fore, Back, Style
#nltk.download('words')

from nltk.corpus import words

# Define o namedtuple Input

Input = namedtuple('Input', ['requested', 'received', 'duration'])

def obtain_input_answer(x,random_word, bem_sucedido):

    start_time = time()

    if x == 1:
    
        keys = []

        keys = ""
        
        print(f"Digite: {random_word} : ",end = "",flush=True) 


        while len(keys) < len(random_word):

            key = readchar.readchar()
            if ord(key) == 32:
                break
        
            keys += key

            print(key, end = "",flush=True)   
            
        print() 
         

        if keys == random_word:
            print(Fore.GREEN+ f"Correto!" + Style.RESET_ALL + "Voce inseriu " + Fore.GREEN + f"{keys}" + Style.RESET_ALL)
            bem_sucedido += 1
        elif ord(key) == 32:
            print(Fore.YELLOW + f"Teste cancelado" + Style.RESET_ALL)

           
        else:
            print(Fore.RED + f"Incorreto! Voce inseriu" + Style.RESET_ALL + "Voce inseriu " + Fore.RED + f"{keys}" + Style.RESET_ALL)
        
        
  

    else:

        print(f"Digite: {random_word} ")

        key = readkey()

        if key == random_word:
            print(Fore.GREEN+ f"Correto!" + Style.RESET_ALL + "Voce inseriu " + Fore.GREEN + f"{key}" + Style.RESET_ALL)
            bem_sucedido += 1

        elif ord(key) == 32:
            print(Fore.YELLOW + f"Teste cancelado" + Style.RESET_ALL)
           
        else:
            print(Fore.RED + f"Incorreto! Voce inseriu" + Style.RESET_ALL + "Voce inseriu " + Fore.RED + f"{key}" + Style.RESET_ALL)
  
    return bem_sucedido, key , keys

def temp_mx( bem_sucedido, tempo_decorrido,word_length): 

    args = arg_init()
    input_records = []
    x=0 # oque faz??
    number_of_types=0
    bem_sucedido=0
    start_time= time()
    while True:

        tempo_inicio=time()
        
        if args.use_words:
            x=1
            random_word = generate_random_word(word_length)
        else:
            random_word = random.choice(string.ascii_lowercase)
        
        bem_sucedido, key = obtain_input_answer(x,random_word, bem_sucedido)
        input_ascii = ord(key)

        tempo_fim=time()
        tempo_tentativa=  round(tempo_fim- tempo_inicio ,2)

        if input_ascii == 32:
            break

        number_of_types +=1
        input_record = Input(requested=random_word, received=key, duration=tempo_tentativa)
        input_records.append(input_record)  # Adicione o registro à lista
        end_time=time()
        tempo_decorrido= round(end_time - start_time, 2)

        if tempo_decorrido >= args.max_value:
            break    
        
    #end_time=time()
    #nao precisa

    #for record in input_records:

    #    print(record.requested)
    #    print(record.received)
    #    print(record.duration) 

    print(f"De {number_of_types} tentativas voce acertou  {bem_sucedido} em {tempo_decorrido} segundos.")   
    return number_of_types, bem_sucedido, tempo_decorrido, input_records  


def input_mx( bem_sucedido, tempo_decorrido,word_length,keys): 

    args = arg_init()
    input_records = []
    x=0 # oque faz??
    number_of_types=0
    bem_sucedido=0 
    start_time=time()

    while True:
        tempo_inicio=time()
        if args.use_words:
            x=1
            random_word = generate_random_word(word_length)
        else:
            random_word = random.choice(string.ascii_lowercase)
        
        bem_sucedido, key , keys= obtain_input_answer(x,random_word, bem_sucedido)

        input_ascii = ord(key)

        tempo_fim=time()
        tempo_decorrido=  round(tempo_fim- tempo_inicio ,2)

        if input_ascii == 32:

            break

        number_of_types +=1
        input_record = Input(requested=random_word, received=key, duration=tempo_decorrido)
        input_records.append(input_record)  # Adicione o registro à lista

        if number_of_types >= args.max_value:
            break    

    end_time=time()
    tempo_decorrido= round(end_time - start_time,2)     #nao precisa 
    #for record in input_records:

     #   print(record.requested)
      #  print(record.received)
       # print(record.duration) 

    print(f"De {number_of_types} tentativas voce acertou  {bem_sucedido} em {tempo_decorrido} segundos.")   
    return number_of_types, bem_sucedido, tempo_decorrido, input_records, keys  


def generate_random_word(length):

    word_list = words.words()
    random_word = random.choice(word_list)
    
    return random_word

def arg_init():

    # Configurar o parser de argumentos de entrada

    parser = argparse.ArgumentParser(description="Definição do modo de teste")

    parser.add_argument("-utm", "--use_time_mode", action="store_true",
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.")
    parser.add_argument("-mv", "--max_value", type=int,
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.")
    parser.add_argument("-uw", "--use_words", action="store_true",
                        help="Usar o modo de digitação de palavras em vez de digitação de caracteres individuais.")
    parser.add_argument("-lt","--level_test",type=int,help="Para o modo de palavras selecione a dificuldade do nivel de 1 a 3")
    
    return parser.parse_args()     

#############################    MAIN    #######################

def main():

    # Variaveis
    data_hora = datetime.now()
    test_start = data_hora.strftime("%Y-%m-%d %H:%M:%S")
    tentativa = 0
    bem_sucedido = 0
    tempo_decorrido =0
    
    #Chamada da função arg_init()
       
    args = arg_init()

    print("Tempo Máximo:", args.max_value)
    print("Time mode:", args.use_time_mode)
    print("Use words:", args.use_words)
    print("Level test:",args.level_test)

    input("Pressione ENTER para iniciar o desafio...")

    # Atribuir o length

    if args.use_words:
        word_length = random.randint(2, 10)
    else:
        word_length = 1

    if args.use_time_mode:

        number_of_types, bem_sucedido, tempo_decorrido, input_records,keys= temp_mx( bem_sucedido, tempo_decorrido)

    else:

        number_of_types, bem_sucedido, tempo_decorrido, input_records = input_mx(bem_sucedido,tempo_decorrido,word_length)  

    # Statistic

    accuracy = str(round((bem_sucedido / number_of_types)* 100)) + '%' if number_of_types > 0 else str(0) + '%'
    type_average_duration = sum(input_record.duration for input_record in input_records) / number_of_types if number_of_types > 0 else 0

    type_hit_average_duration = sum(input_record.duration for input_record in input_records if input_record.requested == input_record.received and bem_sucedido > 0) / bem_sucedido if bem_sucedido > 0 else 0

    type_miss_average_duration = sum(input_record.duration for input_record in input_records if input_record.requested != input_record.received and number_of_types - bem_sucedido > 0) / (number_of_types - bem_sucedido) if number_of_types - bem_sucedido > 0 else 0


    data_hora_fim = datetime.now()
    test_end = data_hora_fim.strftime("%Y-%m-%d %H:%M:%S")

    result_dict = {
        'accuracy': accuracy,
        'inputs': input_records,
        'number_of_hits': bem_sucedido,
        'test_start': test_start,
        'test_end': test_end,
        'number_of_types': number_of_types,
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration
        }      
    pprint(result_dict)

    
if __name__ == "__main__":
    main()