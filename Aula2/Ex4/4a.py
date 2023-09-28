#!/usr/bin/env python3
import argparse
import readchar

from colorama import Fore, Back, Style
#Fore cor da letra, back é o fundo


def printAllCharsUpTo():
    print('Press a key to read a char')
    key= readchar.readkey()
    print('User pressed key ',key)

    number=ord(key)
    print('The number corresponding is ' + str(number))


    for i in range(32,number):
        print(chr(i))
def main():
    printAllCharsUpTo()   

if __name__ == '__main__':
    main()