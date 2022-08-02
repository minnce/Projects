#Created on 5/11/2022 by https://github.com/corgitofu
#Made for Python and scripted on Python 3.10
#Starts with 8 decks of 52 cards, automatic dealing with hit and stay options

import random as rand
import time

#initializes the decks for backjack
blackjack = []


def cardRefill(refill):
    for x in range (1,9):
        for y in range(0,4):
            for z in range(2,11):
                blackjack.append(z)
            blackjack.append("A")
            blackjack.append("J")
            blackjack.append("Q")
            blackjack.append("K")
    refill = len(blackjack)
    return refill

def cardDeal(handValue):
    soft = False
    while True:
        if len(blackjack) > 0:
            try:
                selected = rand.randrange(len(blackjack)-1)
                chosen = blackjack[selected]
                del blackjack[selected]
                if chosen == "J" or chosen == "Q" or chosen == "K":
                    cardValue = 10
                elif chosen == "A":
                        if handValue >= 11:
                            cardValue = 1
                        else: 
                            cardValue = 11
                            soft = True
                else:
                    cardValue = chosen
                return chosen, cardValue, soft
            except ValueError:
                print('no more cards, reshuffling')
                (cardRefill("yes"))
                selected = rand.randrange(len(blackjack)-1)
                chosen = blackjack[selected]
                del blackjack[selected]
                if chosen == "J" or chosen == "Q" or chosen == "K":
                    cardValue = 10
                elif chosen == "A":
                        if handValue >= 11:
                            cardValue = 1
                        else: 
                            cardValue = 11
                            soft = True
                else:
                    cardValue = chosen
                return chosen, cardValue, soft
        else:
            (cardRefill("yes"))
            selected = rand.randrange(len(blackjack)-1)
            chosen = blackjack[selected]
            del blackjack[selected]
            if chosen == "J" or chosen == "Q" or chosen == "K":
                cardValue = 10
            elif chosen == "A":
                if handValue >= 11:
                    cardValue = 1
                else: 
                    cardValue = 11
                    soft = True
            else:
                cardValue = chosen
            return chosen, cardValue, soft


while True:
    print("Welcome to blackjack, dealing cards")
    playerHand = []
    computerHand = []
    playerHandVal = 0
    computerHandVal = 0
    playerSoft = False
    computerSoft = False
    for x in range(0,2):
        selectedCard=cardDeal(playerHandVal)
        playerHand.append(selectedCard[0])
        playerHandVal+=int(selectedCard[1])
        if selectedCard[2] == True:
            playerSoft = True
    #compute computerHand
    for x in range(0,2):
        selectedCard=cardDeal(computerHandVal)
        computerHand.append(selectedCard[0])
        computerHandVal+=int(selectedCard[1])
        if selectedCard[2] == True:
            computerSoft = True
    if playerHandVal == 21:
        print("Winner")
    else:
        print("Your Hand:", playerHand, "Value:", str(playerHandVal), "Soft Number:", str(playerSoft))
        print("Computer Hand:", str(computerHand[0]), "X")
        print("Cards remaining:", str(len(blackjack)))
    ongoing = True
    while ongoing == True:
        if playerHandVal == 21:
            print("You win! Your Hand:", playerHand, "Value:", str(playerHandVal), "Soft Number:", str(playerSoft))
            print("Computer Hand:", computerHand, "Value:", str(computerHandVal), "Soft Number:", str(computerSoft))
            print("Cards remaining:", str(len(blackjack)))
            ongoing = False
        elif playerHandVal < 21:
            print("Hit or stay?")
            choice = str(input())
            choice = choice.lower()
            if choice == "stay":
                ongoing = False
                if playerHandVal <= 21:
                    while computerHandVal <= 16:
                        selectedCard=cardDeal(computerHandVal)
                        computerHand.append(selectedCard[0])
                        computerHandVal+=int(selectedCard[1])
                        if computerHandVal >= 21 and computerSoft == True:
                            computerHandVal -= 10
                            computerSoft = False
                if computerHandVal > 21:
                    print("You win! Your Hand:", playerHand, "Value:", str(playerHandVal), "Soft Number:", str(playerSoft))
                    print("Computer Hand:", computerHand, "Value:", str(computerHandVal), "(Bust)")
                    print("Cards remaining:", str(len(blackjack)))
                elif playerHandVal > computerHandVal:
                    print("You win! Your Hand:", playerHand, "Value:", str(playerHandVal), "Soft Number:", str(playerSoft))
                    print("Computer Hand:", computerHand, "Value:", str(computerHandVal), "Soft Number:", str(computerSoft))
                    print("Cards remaining:", str(len(blackjack)))
                elif playerHandVal < computerHandVal:
                    print("You lose! Your Hand:", playerHand, "Value:", str(playerHandVal), "Soft Number:", str(playerSoft))
                    print("Computer Hand:", computerHand, "Value:", str(computerHandVal), "Soft Number:", str(computerSoft))
                    print("Cards remaining:", str(len(blackjack)))
                elif playerHandVal == computerHandVal:
                    print("Draw. Your Hand:", playerHand, "Value:", str(playerHandVal), "Soft Number:", str(playerSoft))
                    print("Computer Hand:", computerHand, "Value:", str(computerHandVal), "Soft Number:", str(computerSoft))
                    print("Cards remaining:", str(len(blackjack)))
            elif choice == "hit":
                selectedCard=cardDeal(playerHandVal)
                playerHand.append(selectedCard[0])
                playerHandVal+=int(selectedCard[1])
                if playerHandVal > 21:
                    if playerSoft == True:
                        playerHandVal -= 10
                        print("You drew a", str(selectedCard[0])+". Your Hand:", playerHand, "Value:", str(playerHandVal), "Soft Number:", str(playerSoft))
                        print("Cards remaining:", str(len(blackjack)))
                        playerSoft = False
                    else:
                        ongoing = False
                        print("Busted! You Lose. Hand:", playerHand, "Value:", str(playerHandVal), "Soft Number:", str(playerSoft))
                        print("Computer Hand:", str(computerHand[0]), " X")
                        print("Cards remaining:", str(len(blackjack)))
                else:
                    print("You drew a", str(selectedCard[0])+". Your Hand:", playerHand, "Value:", str(playerHandVal), "Soft Number:", str(playerSoft))
                    print("Cards remaining:", str(len(blackjack)))
            else:
                while True:
                    print("Invalid choice, Quit? (yes/no)")
                    choice = str(input())
                    if choice == "yes":
                        ongoing = False
                        break
                    elif choice == "no":
                        print("Returning to hit/stay")
                        break
                    else:
                        print("Invalid choice")