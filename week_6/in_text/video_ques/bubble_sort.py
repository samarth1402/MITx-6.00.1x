def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range( 1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

# my version of bubble_sort which is a little better
def bubble_sort_sam(L):
    for i in range(len(L)):
        swap = True
        for j in range(1, len(L) - i):
            if L[j-1] > L[j]:
                swap = False
                L[j-1],L[j] = L[j], L[j-1]
        if swap == True:
            return L
    return L

