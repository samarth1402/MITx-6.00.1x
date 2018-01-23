# Problem 3 - Valid Words

# However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game.
# A valid word is in the word list; and it is composed entirely of letters from the current hand.
# Implement the isValidWord function.

# Testing: Make sure the test_isValidWord tests pass.
# In addition, you will want to test your implementation by calling it multiple times on the same hand - what should the correct behavior be?


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    tempHand = hand.copy()
    for char in word:
        if char in hand.keys():
            #this condition checks occuruences of letter in word <= occ. in hand
            if tempHand[char]>0:
                tempHand[char] -= 1
            else:
                return False
        else:
            return False
    if word in wordList:
        return True
    else:
        return False
