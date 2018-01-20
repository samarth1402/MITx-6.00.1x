#code snipet for video 3 of of 8-exceptions

#code for a programmer-made error message

def get_ratios(L1, L2):
    """
    Assumes: L1 and L2 are the lists of equal length of numbers
    :return: a list containing L1[i]/L2[i]
    """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('Nan'))     #Nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios