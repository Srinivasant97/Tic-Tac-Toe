
a=["_","_","_",
   "_","_","_",
   "_","_","_"]

Xpoint=0
Turn ="X"
visited = 1


def displayboard():
    print(a[0]+"|"+a[1]+"|"+a[2] + "           1|2|3")
    print(a[3] + "|" + a[4] + "|" + a[5] + "           4|5|6")
    print(a[6] + "|" + a[7] + "|" + a[8] + "           7|8|9")

displayboard()

def Xturn():
    global Turn
    global visited
    print(f"Turn of {Turn} :")
    x=input("Choose the location from 1 to 9: ")
    while x not in ("1","2","3","4","5","6","7","8","9"):
        print("Position is not avaliable, Try again:")
        x = input("Choose the location from 1 to 9: ")
    x=int(x)-1

    while a[x] != "_":
        print("Mentioned location is already located")
        x = input("Choose the location from 1 to 9: ")
        x = int(x) - 1


    a[x] = Turn
    if Turn == "X":
        Turn = "O"
    else:
        Turn = "X"

    displayboard()


def rowcompare():
    global Xpoint
    if (a[0]==a[1]==a[2]=="X") | (a[3]==a[4]==a[5]=="X") | (a[6]==a[7]==a[8]=="X") :
        print("X wins by row")
        Xpoint += 1
    elif (a[0]==a[1]==a[2]=="O") | (a[3]==a[4]==a[5]=="O") | (a[6]==a[7]==a[8]=="O"):
        print("O wins by row")
        Xpoint += 1


def columncompare():
    global Xpoint
    if (a[0]==a[3]==a[6]=="X") | (a[1]==a[4]==a[7]=="X") | (a[2]==a[5]==a[8]=="X") :
        print("X wins by column")
        Xpoint += 1
    elif (a[0]==a[3]==a[6]=="O") | (a[1]==a[4]==a[7]=="O") | (a[2]==a[5]==a[8]=="O"):
        print("O wins by column")
        Xpoint += 1

def diagonalcompare():
    global Xpoint
    if Xpoint == 0:
        if (a[0]==a[4]==a[8]=="X") | (a[2]==a[4]==a[6]=="X"):
            print("X wins Diagonally")
            Xpoint += 1
        elif (a[0]==a[4]==a[8]=="O") | (a[2]==a[4]==a[6]=="O"):
            print("O wins Diagonally")
            Xpoint += 1

def Draw():
    global Xpoint
    if Xpoint ==0:
        if "_" not in a:
            print("Match Draw")
            Xpoint += 1



while Xpoint ==0:
    Xturn()
    rowcompare()
    columncompare()
    diagonalcompare()
    Draw()

