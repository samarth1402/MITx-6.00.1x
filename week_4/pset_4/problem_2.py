# Problem 2 - Dealing with Hands

# REPRESENTING HANDS

# A hand is the set of letters held by a player during the game.
# The player is initially dealt a set of random letters.
# For example, the player could start out with the following hand: a, q, l, m, u, i, l.
# In our program, a hand will be represented as a dictionary:
# the keys are (lowercase) letters and the values are the number of times the particular letter is repeated in that hand.
# For example, the above hand would be represented as: hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}

# Notice how the repeated letter 'l' is represented.
# Remember that with a dictionary, the usual way to access a value is hand['a'], where 'a' is the key we want to find.
# However, this only works if the key is in the dictionary; otherwise, we get a KeyError.
# To avoid this, we can use the call hand.get('a',0).
# This is the "safe" way to access a value if we are not sure the key is in the dictionary.
# d.get(key,default) returns the value for key if key is in the dictionary d, else default.
# If default is not given, it returns None, so that this method never raises a KeyError.

# For example:
# >>> hand['e']
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# KeyError: 'e'
# >>> hand.get('e', 0)
# 0

# REMOVING LETTERS FROM A HAND (YOU IMPLEMENT THIS)

# The player starts with a hand, a set of letters.
# As the player spells out words, letters from this set are used up.
# For example, the player could start out with the following hand: a, q, l, m, u, i, l.
# The player could choose to spell the word quail .
# This would leave the following letters in the player's hand: l, m.
# Your task is to implement the function updateHand, which takes in two inputs - a hand and a word (string).
# updateHand uses letters from the hand to spell the word, and then returns a copy of the hand, containing only the letters remaining.

# For example:
# >>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# >>> displayHand(hand) # Implemented for you
# a q l l m u i
# >>> hand = updateHand(hand, 'quail') # You implement this function!
# >>> hand
# {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
# >>> displayHand(hand)
# l m

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    remHand = hand.copy()
    for char in word:
        if remHand[char] > 0:
            remHand[char] -= 1
        else:
            del remHand[char]
    return remHand