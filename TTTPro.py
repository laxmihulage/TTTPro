slat=["-","-","-",
       "-","-","-",
       "-","-","-"]
player1="+"
gameisgoing=True
champ=None
def display_slat():
    print(slat[0] + " | " + slat[1] + " | " + slat[2])
    print(slat[3] + " | " + slat[4] + " | " + slat[5])
    print(slat[6] + " | " + slat[7] + " | " + slat[8])

def handle_turn():
    spot=int(input("Choose any random Spot or Position from 0 to 8:"))
    if spot<8:
        slat[spot] = player1


    if spot>8:
        spot = int(input("Choose any random Spot or Position from 0 to 8:"))

    slat[spot] = player1

def change_players():
    global player1
    if player1=="+":
        player1="*"
    elif player1=="*":
        player1="+"

def check_who_is_the_champion():
    global champ
    rowchamp=check_row()
    colchamp=check_column()
    diachamp=check_diagonal()
    check_tie()

    if rowchamp:
        champ=rowchamp
    elif colchamp:
        champ=colchamp
    else:
        champ=diachamp

def check_row():

    global gameisgoing
   
    row1 = slat[0] == slat[1] == slat[2] != "-"
    row2 = slat[3] == slat[4] == slat[5] != "-"
    row3 = slat[6] == slat[7] == slat[8] != "-"

    if row1 or row2 or row3:
        gameisgoing=False


    if row1:
     return slat[0]

    elif row2:
     return slat[5]

    elif row3:
     return slat[6]


def check_column():
    global gameisgoing
    
    col1 = slat[0] == slat[3] == slat[6] != "-"
    col2 = slat[1] == slat[4] == slat[7] != "-"
    col3 = slat[2] == slat[5] == slat[8] != "-"

    if col1 or col2 or col3:
        gameisgoing = False

    if col1:
        return slat[0]

    elif col2:
        return slat[1]

    elif col3:
        return slat[5]

def check_diagonal():
    global gameisgoing
    
    dia1 = slat[0] == slat[4] == slat[8] != "-" 
    dia2 = slat[2] == slat[4] == slat[6] != "-"


    if dia1 or dia2:
        gameisgoing = False

    if dia1:
        return slat[0]

    elif dia2:
        return slat[4]

def check_tie():
    global gameisgoing
    if "-" not in slat:
        gameisgoing=False
        print("OOO!!!!! Match is Tie.........")

def play_game():
    while gameisgoing:
        display_slat()

        handle_turn()

        change_players()

        check_who_is_the_champion()

    if champ=="+":
        print("Congratulations +  !!!!!!!!!.... You are the Champion of Tic Tac Toe game")
    elif champ=="*":
        print("Congratulations *  !!!!!!!!!.... You are the Champion of Tic Tac Toe game")

play_game()