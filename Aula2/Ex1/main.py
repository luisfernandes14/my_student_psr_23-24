#!/usr/bin/env python3

from colorama import Fore, Back, Style
#Fore cor da letra, back é o fundo
maximum_number = 10


def getDividers(value):
    #create and empty list
    dividers = []

    for i in range(1,value):
        if value%i == 0:
            dividers.append(i) #adicionar o dividers a uma lista
    
    return dividers



def isPerfect(value):
    dividers = getDividers(value)
    return sum(dividers)==value
   





def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number): #for cycle to go from 0 to 10
        if isPerfect(i):
            print('Number ' + Fore.RED + str(i) + Style.RESET_ALL + ' is perfect.' )
        #dividers = getDividers(i)
        #print("Number " + str(i) + " has dividers " + str(dividers))  

if __name__ == "__main__":
    main()


