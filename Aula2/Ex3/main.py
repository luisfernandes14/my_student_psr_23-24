#!/usr/bin/env python3
import argparse

from colorama import Fore, Back, Style
#Fore cor da letra, back é o fundo
from myfunctions import isPerfect

""" maximum_number = 10 """



def main():
    #Process command line argument
    parser = argparse.ArgumentParser(description= 'Script to compute perfect numbers ')
    parser.add_argument('-mn', '--maximum_number', type=int, help=' max number', required=True)
    parser.add_argument('-n', '--name', type=str, help=' A name to print',required=False,default='António')
    
    args = vars(parser.parse_args()) #cria um dicionario em python
    print(args)

 

    print("Hi" + args['name'] + "Starting to compute perfect numbers up to " + str(args['maximum_number']))

    for i in range(1, args['maximum_number'] + 1): #for cycle to go from 0 to 10
        if isPerfect(i):
            print('Number ' + Fore.RED + str(i) + Style.RESET_ALL + ' is perfect.' )
        #dividers = getDividers(i)
        #print("Number " + str(i) + " has dividers " + str(dividers))  

if __name__ == "__main__":
    main()


