import random
from random import randint


CARDNUM = 52


def command():
    print("tu joue ?")
    incommand = input()
    if incommand == "oui" or incommand == "o" or incommand == "yes" or incommand == "y":
        start_game()
    else :
        print("QUIT")



def start_game():
    sum_values()


def get_card(cardnum):
    numberFamilly = 4
    famillyName = ['carreau', 'pic', 'coeur', 'trefle']
    getOneCard = {"Croupier" : [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)],
                    "Joueur" : [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)]
                }

    return getOneCard


def sum_values():
    card = get_card(CARDNUM)
    print(card)
    values = card.values()
    
    _sum = []

if __name__ == "__main__":
    command()
