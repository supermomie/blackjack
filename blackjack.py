import random
from termcolor import colored


NUM_CARD = 52

def command():
    print("tu veux jouer ?")
    incommand = input()
    if incommand == "oui" or incommand == "o" or incommand == "yes" or incommand == "y":
        game()
    quitGame = print(colored('QUIT', 'red'))
    quitGame, exit() if incommand == "" else quitGame

def get_card(cardnum):
    numberFamilly = 4
    famillyName = ['carreau', 'pic', 'coeur', 'trefle']
    getOneCard = {"Croupier" : [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)],
                    "Joueur" : [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)]
                }
    return getOneCard


def game(t = 1, a_c = [], a_j = [], d_c = [], d_j = []):
    card = get_card(NUM_CARD)
    _elem = [elem for elem in list(card.values())]
    _player = [player for player in list(card.items())]
    numeroC, numeroJ = _elem[0][0], _elem[1][0]
    numeroC == 10 if numeroC == 11 or numeroC == 12 or numeroC == 13 else ""
    numeroJ == 10 if numeroJ == 11 or numeroJ == 12 or numeroJ == 13 else ""
    allElemC, allElemJ, detailElemC, detailElemJ = a_c, a_j, d_c, d_j
    allElemC.append(numeroC) if sum(allElemC) < 16 else numeroC
    allElemJ.append(numeroJ) #if _input == "o" else numeroJ
    detailElemC.append(_elem[0]) if sum(allElemC) < 16 else numeroC
    detailElemJ.append(_elem[1]) #if _input == "o" else numeroJ
    _sumC, _sumJ = sum(allElemC), sum(allElemJ)
    print(_player[0][0], detailElemC, allElemC,"=", _sumC)
    print(_player[1][0], detailElemJ, allElemJ,"=", _sumJ)
    print("\n\n"+colored('CONTINUE ??', 'yellow')+"\n\n")
    stateGame = "BLACKJACKJ" if _sumJ == 21 else "BLACKJACKC" if _sumC == 21 else True if _sumJ > 21 else False if _sumC > 21 else False
    playerStatement = _player[1][0] if stateGame == True or stateGame == "BLACKJACKJ" else _player[0][0]
    winMessage = colored("LE "+ playerStatement.upper() +" A WIN LA GAME", 'green')
    gameOverMessage = colored("GAME OVER POUR "+ playerStatement.upper(), 'red')
    result = winMessage if stateGame == False or stateGame == "BLACKJACKJ" or stateGame == "BLACKJACKC" else gameOverMessage
    print(result) if stateGame else ""
    exit() if stateGame == True or stateGame == "BLACKJACKJ" or stateGame == "BLACKJACKC" else ""
    incommand = input()
    if incommand == "o" or incommand == "oui" or incommand == "y" or incommand == "yes":
        t += 1
        game(t, a_c, a_j, d_c, d_j)


if __name__ == "__main__":
    command()
