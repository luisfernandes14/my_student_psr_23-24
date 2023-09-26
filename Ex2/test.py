#!/usr/bin/env python3

from colorama import Fore, Back, Style
#Fore cor da letra, back é o fundo
maximum_number = 10
#usar aqui ./test.py | grep "is prime" | wc -l, para descobrir quantos numeros primos tem até 10000
def isPrime(value):
    for i in range(2,value):
        if value%i == 0:
            #print("The number " + str(value) + " is not prime because we can divide by "+ str(i))
            return False
    return True
    

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(0, maximum_number): #for cycle to go from 0 to 10
        if isPrime(i):
            print('Number ' + Fore.RED + str(i) + Style.RESET_ALL + ' is prime.' )
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()

