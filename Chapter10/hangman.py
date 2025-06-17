def hangman(word):
    wrong=0
    stages=["",
            "_______      ",
            "|     |      ",
            "|     o      ",
            "|    /|\\    ",
            "|    / \\    ",
            "|            "
            ]
    rletters=list(word)
    board=["__"]*len(word)

    while wrong <len(stages)-1:
        print(" ".join(board))
        char=input("1文字を予想してね")

        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print(" ".join(board))
        print("\n".join(stages[0:wrong+1]))
        if "__" not in board:
            print("あなたの勝ち!")
            break
        if wrong==len(stages)-1:
            print(f"あなたの負け!正解は{word}")

print("ハングマンへようこそ")
hangman("cat")






