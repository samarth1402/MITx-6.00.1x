# Problem 6 - Playing a Game

# A game consists of playing multiple hands.
# We need to implement one final function to complete our word-game program.
# Write the code that implements the playGame function.

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    hand = {}
    while True:
        opt = input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
        if opt == "n":
            hand = dealHand(HAND_SIZE)
            playHand(hand,wordList,HAND_SIZE)
        elif opt == "r":
            try:
                playHand(hand,wordList,HAND_SIZE)
            except:
                print("You have not played a hand yet. Please play a new hand first!")
        elif opt == "e":
            break
        else:
            print("Invalid command")
