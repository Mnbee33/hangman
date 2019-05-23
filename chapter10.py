import random

def hangman():
    words = ["cat",
             "dog",
             "apple",
             "orange"]

    targetIndex = random.randint(0, len(words)-1)
    word = words[targetIndex]
    
    wrong = 0
    stages = ["",
              "______      ",
              "|           ",
              "|     |     ",
              "|     0     ",
              "|    /|\    ",
              "|    / \    ",
              "|           "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welecome to Hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The answer is {}.".format(word))

hangman()
