def selection_sort(L):
    suffixSt = 0    #index at which suffix starts
    while suffixSt != len(L):
        for i in range (suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1