def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invertedDic={}
    #adds element to inverted dic with key and values interchanged
    for key_d,value_d in d.items():
        #adds key and its value to the inverted dictionary
        if value_d not in invertedDic:
            invertedDic[value_d]=[key_d]
        #appends the value to the list of there value if key already in dictionary
        else:
            invertedDic[value_d].append(key_d)
    # at this moment the value list is not sorted
    for key in invertedDic.keys():
        invertedDic[key].sort()
    # values list in inverted dictionary sorted
    return invertedDic
