# using recussion

# not effecient as a new copy of list is made on each recussion call
def bisect_search1(L,e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search1(L[:half],e)
        else:
            return bisect_search1(L[half:],e)

# the same copy of list  is reused
def bisect_search2(L,e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid : #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)
if bisect_search2([1,2,3,4], 5) :
    pass
else:
    print("yo")