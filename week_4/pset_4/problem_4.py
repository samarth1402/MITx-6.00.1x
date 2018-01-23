# Problem 4 - Hand Length

# Implement the helper calculateHandlen function,


def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    count = 0
    for freq in hand.keys():
        count += freq
    return count