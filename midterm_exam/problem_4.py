def getSublists(L, n):
    '''
    :param L: List input
    :param n: length of subset
    :return: A list containing all the subsets
    '''
    subList=[]
    i=0
    # checks if a subset can ne formed if it starts form i th element
    while i+n <= len(L):
        # adds subset to sublist
        subList.append(L[i:i+n])
        i += 1
    return subList

