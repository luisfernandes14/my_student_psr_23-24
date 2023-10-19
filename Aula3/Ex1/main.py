#!/usr/bin/env python3
import argparse
import readchar

from colorama import Fore, Back, Style



print(keys)

n_numeric=0
for key in keys:
    if key.isnumeric():
    n_numeric +=1

print('You pressed on ' + str(n_numeric)) + ' numeric keys')

#Ex5b
numerical_keys = []
for key in keys:
    if key.isnumeric():
        numerical_keys.append(key)

print(str(numerical_keys))

#Ex5c
d_keys={}
for key_idx, key in enumerate(keys):
    d_keys[key_idx]= key

print(str(d_keys))

#Ex5d
numerical_keys.sort()
print(str(numerical_keys))

#Ex5e
numerical_keys2= [x for x keys if x.isnumeric()]
d_keys2={idx:x for idx, x in enumerate(keys)}
print(str(numerical_keys2))

for idx_key,key in enumerate(keys):
    print(Fore.RED + str(idx_key)+Style.RESET_ALL+ ': the key pressed was '+Fore.GREEN + Back.MAGENTA + key + Style.RESET_ALL)



main():
    countNumberUpto('x')





if __name__ == '__main__':
    main()