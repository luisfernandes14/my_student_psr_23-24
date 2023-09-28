from math import sqrt
#ponto de interrogação 

def getDividers(value):
    #create and empty list
    dividers = []
    limit = (value/2)
    for i in range(1,limit):
        if value%i == 0:
            dividers.append(i) #adicionar o dividers a uma lista
    
    return dividers



def isPerfect(value):
    dividers = getDividers(value)
    return sum(dividers)==value
   