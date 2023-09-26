#!/usr/bin/env python3

from colorama import Fore, Back, Style
#Fore cor da letra, back é o fundo
maximum_number = 10

def isPerfect(value):
    accuumulator = 0
    for i in range(1,value):
        if value%i== 0:
            accuumulator = accuumulator + i
    #ver se a soma dos divisores inteiros é igual ao proprio número
    return accuumulator == value 

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number): #for cycle to go from 0 to 10
        if isPerfect(i):
            print('Number ' + Fore.RED + str(i) + Style.RESET_ALL + ' is perfect.' )
      

if __name__ == "__main__":
    main()


