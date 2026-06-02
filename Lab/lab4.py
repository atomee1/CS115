
def concatenateList(L, item):
    ''' Concatenates list with every new added item and value  '''
    return [L[0] + item[1], [item] + L[1]]


def compare(L1, L2):
    ''' Compares first element of two lists and returns list with greater value '''
    if L1[0] > L2[0]:
        return L1
    return L2


def knapsack(capacity, itemsList):
    ''' Returns list identifying maximum value of items given maximum capacity,
        as well as a sub-list containing items involved in optimal solution '''

    if capacity <= 0 or itemsList == []:
        return [0, []]
    
    elif itemsList[0][0] > capacity:
        return knapsack(capacity, itemsList[1:])
    
    else:
        use = concatenateList(knapsack(capacity - itemsList[0][0], itemsList[1:]), itemsList[0])
        lose = knapsack(capacity, itemsList[1:])

        return compare(use,lose)
