import random
from random import randint
from termcolor import colored


NUM_CARD = 52
COMMAND = ["oui", "o", "yes", "y", "mise", "passe"]
MSG = ["win", "lose"]


def command():
    print("tu veux jouer ?")
    incommand = input()
    if incommand == "oui" or incommand == "o" or incommand == "yes" or incommand == "y":
        start_game()
    quitGame = print(colored('QUIT', 'red'))
    quitGame, exit() if incommand == "" else quitGame

def start_game():
    sum_values()


def get_card(cardnum):
    numberFamilly = 4
    famillyName = ['carreau', 'pic', 'coeur', 'trefle']
    getOneCard = {"Croupier" : [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)],
                    "Joueur" : [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)]
                }
    return getOneCard


def sum_values(t = 1, a_c = [], a_j = []):
    card = get_card(NUM_CARD)
    _elem = [elem for elem in list(card.values())]
    _player = [player for player in list(card.items())]
    numeroC, numeroJ = _elem[0][0], _elem[1][0]
    if numeroC == 11 or numeroC == 12 or numeroC == 13 or numeroJ == 11 or numeroJ == 12 or numeroJ == 13:
        numeroC, numeroJ = 10, 10
    allElemC, allElemJ = a_c, a_j
    allElemC.append(numeroC) #if sum(allElemC) < 16 else numeroC
    allElemJ.append(numeroJ) #if incommand == "o" else numeroJ
    _sumC, _sumJ = sum(allElemC), sum(allElemJ)
    print(_player[0][0], allElemC,"=", _sumC)
    print(_player[1][0], allElemJ,"=", _sumJ)
    print("\n\n"+colored('CONTINUE ??', 'green')+"\n\n")

    stateGame = True if _sumC > 21 else False if _sumJ > 21 else "B" if _sumC == 21 else "B" if _sumJ == 21 else False
    #TODO correct the stateGame variable
    print("S-G",stateGame)
    displayMessage = True if stateGame == True else False
    playerStatement = _player[1][0] if stateGame == True else _player[0][0]
    winMessage = colored("LE "+ playerStatement.upper() +" A WIN LA GAME", 'green')
    gameOverMessage = colored("gameover pour "+ playerStatement.upper(), 'red')
    result = winMessage if stateGame == False else gameOverMessage
    print(result) if displayMessage else ""
    exit() if stateGame == True else ""
    incommand = input()
    if incommand == "o" or incommand == "oui" or incommand == "y" or incommand == "yes":
        t += 1
        sum_values(t, a_c, a_j)


if __name__ == "__main__":
    command()
