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
   