# Problem 3 - CiphertextMessage

# Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial.
# If message is the encrypted message, and s is the shift used to encrypt the message,
# then apply_shift(message, 26-s) gives you the original plaintext message.


# Fill in the methods in the class CiphertextMessage acording to the specifications in ps6.py.
# The methods you should fill in are:
# __init__(self, text): Use the parent class constructor to make your code more concise.
# decrypt_message(self): You may find the helper function is_word(wordlist, word) and the string method split() useful.
# Note that is_word will ignore punctuation and other special characters when considering whether a word is valid.


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        word_list = load_words(WORDLIST_FILENAME)

        max_count = 0
        decryptedText = ''
        bestShift = None

        for s in range(1, 27):
            text = self.apply_shift(26 - s)
            textList = text.split(' ')
            count = 0
            for word in textList:
                if is_word(word_list, word):
                    count += 1
            if count > max_count:
                max_count = count
                bestShift = 26 - s
                decryptedText = text
        return (bestShift, decryptedText)