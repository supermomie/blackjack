import random
import socketio
from termcolor import colored


NUM_CARD = 52 #TODO RENAME THAT

def command():
    print(colored("tu veux jouer ?".upper(), 'green', attrs=['bold', 'blink']), colored("oui", 'green', attrs=['bold']), colored('non','red', attrs=['bold']))
    incommand = input()
    if incommand == "oui" or incommand == "o" or incommand == "yes" or incommand == "y":
        game()
    quitGame = print(colored('QUIT', 'red', attrs=['reverse','bold']))
    quitGame, exit() if incommand == "" else quitGame

#TODO implement multi SOCKETIO
def implement_players():
    command()

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
    if numeroC == 11 or numeroC == 12 or numeroC == 13 or numeroJ == 11 or numeroJ == 12 or numeroJ == 13:
        numeroC, numeroJ = 10, 10
    allElemC, allElemJ, detailElemC, detailElemJ = a_c, a_j, d_c, d_j
    detailElemC.append(_elem[0]) if sum(allElemC) < 16 else numeroC
    detailElemJ.append(_elem[1]) #if _input == "o" else numeroJ
    allElemC.append(numeroC) if sum(allElemC) < 16 else numeroC
    allElemJ.append(numeroJ) #if _input == "o" else numeroJ
    _sumC, _sumJ = sum(allElemC), sum(allElemJ)
    print(colored(_player[0][0], 'magenta'), detailElemC, colored(allElemC, 'blue'),"=", colored(_sumC, 'cyan', attrs=['bold', 'blink']))
    print(colored(_player[1][0], 'magenta'), detailElemJ, colored(allElemJ, 'blue'),"=", colored(_sumJ, 'cyan', attrs=['bold', 'blink']))
    print("\n\n"+colored('CONTINUE ??', 'yellow')+"\n\n")
    stateGame = "BLACKJACKJ" if _sumJ == 21 else "BLACKJACKC" if _sumC == 21 else "J" if _sumJ > 21 else "C" if _sumC > 21 else False
    playerStatement = _player[1][0] if stateGame == "J" or stateGame == "BLACKJACKJ" else _player[0][0]
    winMessage = colored("LE "+ playerStatement.upper() +" A WIN LA GAME", 'green', attrs=['reverse', 'bold', 'blink'])
    gameOverMessage = colored("GAME OVER POUR "+ playerStatement.upper(), 'red', attrs=['reverse', 'bold'])
    result = winMessage if stateGame == False or stateGame == "BLACKJACKJ" or stateGame == "BLACKJACKC" else gameOverMessage
    print(result) if stateGame else ""
    exit() if stateGame == "J" or stateGame == "C" or stateGame == "BLACKJACKJ" or stateGame == "BLACKJACKC" else ""
    incommand = input()
    if incommand == "o" or incommand == "oui" or incommand == "y" or incommand == "yes":
        t += 1
        game(t, a_c, a_j, d_c, d_j)


if __name__ == "__main__":
    command()
    #print(get_card(NUM_CARD))
