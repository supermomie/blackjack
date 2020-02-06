import random
from random import randint
from termcolor import colored


CARDNUM = 52


def command():
    print("tu joue ?")
    incommand = input()
    if incommand == "oui" or incommand == "o" or incommand == "yes" or incommand == "y":
        start_game()
    if incommand == "":
        print(colored('QUIT', 'red'))
    else: 
        print(colored('QUIT', 'red'))



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
    card = get_card(CARDNUM)
    _elem = [elem for elem in list(card.values())]
    _player = [player for player in list(card.items())]
    numeroC = _elem[0][0]
    numeroJ = _elem[1][0]
    if numeroC == 11 or numeroC == 12 or numeroC == 13 or numeroJ == 11 or numeroJ == 12 or numeroJ == 13:
        numeroC = 10
        numeroJ = 10
    allElemC = a_c
    allElemJ = a_j
    allElemC.append(numeroC) if sum(allElemC) < 16 else numeroC
    allElemJ.append(numeroJ)
    _sumC = sum(allElemC)
    _sumJ = sum(allElemJ)
    print(_player[0][0], allElemC,"=", _sumC)
    print(_player[1][0], allElemJ,"=", _sumJ)
    print("\n\n"+colored('CONTINUE ??', 'green')+"\n\n")
    stateGame = False if _sumJ > 21 or _sumC > 21 else True
    stateUser = _player[0][0] if _player[0][0] == True  else _player[1][0]
    if _sumJ == 21:
        print(colored("BLACKJACK POUR "+_player[1][0].upper()+" A WIN LA GAME", 'green'))
        exit()
    if _sumC == 21:
        print(colored("BLACKJACK POUR "+_player[0][0].upper()+" A WIN LA GAME", 'green'))
        exit()
    if _sumC > 21:
        print(colored("GAME OVER POUR "+ _player[0][0].upper(), 'red'))
        exit()
    if _sumJ > 21:
        print(colored("GAME OVER POUR "+ _player[1][0].upper(), 'red'))
        exit()
    incommand = input()
    if incommand == "o" or incommand == "oui" or incommand == "y" or incommand == "yes":
        t += 1
        sum_values(t, a_c, a_j)

def rules():
    sum_values(t, a_c, a_j)




if __name__ == "__main__":
    command()
