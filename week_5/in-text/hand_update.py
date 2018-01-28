# Exercise: hand


# In this problem, you'll be asked to read through an object-oriented implementation of the hand from the word game problem of Problem Set 4.
# You'll then be asked to implement one of its methods.

# When you have completed reading through the file, implement the update method.

def update(self, word):
    """
    Does not assume that self.hand has all the letters in word.

    Updates the hand: if self.hand does have all the letters to make
    the word, modifies self.hand by using up the letters in the given word.

    Returns True if the word was able to be made with the letter in
    the hand; False otherwise.

    word: string
    returns: Boolean (if the word was or was not made)
    """
    # Your code here
    handCopy = self.hand.copy()
    try:
        for letter in word:
            if self.hand[letter] > 0:
                self.hand[letter] -= 1
            else:
                self.hand = handCopy.copy()
                return False
    except KeyError:
        self.hand = handCopy.copy()
        return False
    else:
        return True