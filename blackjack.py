import os
import random
import socketio
import numpy as np
from termcolor import colored

NUM_CARD = 52
NUMBERFAMILLY = 4
FAMILLYNAME = ['carreau', 'pic', 'coeur', 'trefle']


class multi:

    def __init__(self):
        self.player = 5

    def implement_players():
        #TODO implement multi player
        print("Starting multi")


class blackjack:

    def __init__(self, num_card, numberFamilly, famillyName):
        self.num_card = NUM_CARD
        self.numberFamilly = NUMBERFAMILLY
        self.famillyName = FAMILLYNAME
        self.command()


    def command(self):
        print(colored("tu veux jouer ?\n".upper(), 'green', attrs=['bold']), colored("oui/o/yes/y", 'green', attrs=['bold']),"|", colored('non/enter','red', attrs=['bold']))
        incommand = input(">> ")
        if incommand == "oui" or incommand == "o" or incommand == "yes" or incommand == "y":
            self.game()
        quitGame = print(colored('QUIT', 'red', attrs=['reverse','bold']))
        quitGame, exit() if incommand == "" else quitGame

    def get_card(self, cardnum, starting = True):
        numberFamilly = self.numberFamilly
        famillyName = ['carreau', 'pic', 'coeur', 'trefle']
        getOneCard = {"Croupier" : [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)],
                        "Joueur" : [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)]
                    }
        getTwoCard = {"Croupier" : [[random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)],
                                    [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)]],
                        "Joueur" : [[random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)],
                                    [random.randint((cardnum - cardnum) + 1, cardnum//numberFamilly), random.choice(famillyName)]]
                    }
        return getOneCard if starting == False else getTwoCard


    def game(self, t = 1, l = 21, a_c = [], a_j = [], d_c = [], d_j = [], starting = True):
        card = self.get_card(self.num_card, starting)
        _elem = [elem for elem in list(card.values())]
        _player = [player for player in list(card.items())]
        ten = 10
        numeroC = _elem[0][0] if starting == False else _elem[0][0][0]+_elem[0][1][0] #if over 10
        numeroJ = _elem[1][0] if starting == False else _elem[1][0][0]+_elem[1][1][0] #if over 10
        numeroC = ten if numeroC == 11 or numeroC == 12 or numeroC == 13 else numeroC
        numeroJ = ten if numeroJ == 11 or numeroJ == 12 or numeroJ == 13 else numeroJ
        allElemC, allElemJ, detailElemC, detailElemJ = a_c, a_j, d_c, d_j
        detailElemC.append(_elem[0]) if sum(allElemC) < 16 else numeroC
        detailElemJ.append(_elem[1]) #if _input == "o" else numeroJ
        allElemC.append(numeroC) if sum(allElemC) < 16 else numeroC
        allElemJ.append(numeroJ) #if _input == "o" else numeroJ
        _sumC, _sumJ = sum(allElemC), sum(allElemJ)
        print(colored(_player[0][0], 'magenta'), detailElemC, colored(allElemC, 'blue'),"=", colored(_sumC, 'cyan', attrs=['bold', 'blink']))
        print(colored(_player[1][0], 'magenta'), detailElemJ, colored(allElemJ, 'blue'),"=", colored(_sumJ, 'cyan', attrs=['bold', 'blink']))
        print("\n\n"+colored('CONTINUE ??', 'yellow')+"\n\n")
        stateGame = "PUREBJ" if _sumJ == l else "PUREBC" if _sumC == l else "BLACKJACKJ" if _sumJ == l else "BLACKJACKC" if _sumC == l else "J" if _sumJ > l else "C" if _sumC > l else False
        print(stateGame)
        print("Tour numero",t)
        playerStatement = _player[1][0] if stateGame == "J" or stateGame == "BLACKJACKJ" else _player[0][0]
        absoluteWin = colored("LE "+ playerStatement.upper()+" A BLACKJACK", 'green' , attrs=['reverse', 'bold', 'blink'])
        winMessage = colored("LE "+ playerStatement.upper() +" A WIN LA GAME", 'green', attrs=['reverse', 'bold', 'blink'])
        gameOverMessage = colored("GAME OVER POUR "+ playerStatement.upper(), 'red', attrs=['reverse', 'bold'])
        result = absoluteWin if stateGame == "PUREBJ" or stateGame == "PUREBC" else winMessage if stateGame == False or stateGame == "BLACKJACKJ" or stateGame == "BLACKJACKC" else gameOverMessage
        print(result) if stateGame else ""
        exit() if stateGame == "PUREBJ" or stateGame == "PUREBC" or stateGame == "J" or stateGame == "C" or stateGame == "BLACKJACKJ" or stateGame == "BLACKJACKC" else ""
        incommand = input(">> ")
        #os.system('clear')
        if incommand == "o" or incommand == "oui" or incommand == "y" or incommand == "yes":
            t += 1
            self.game(t, l, a_c, a_j, d_c, d_j, starting = False)


if __name__ == "__main__":
    blackjack(NUM_CARD, NUMBERFAMILLY, FAMILLYNAME)
