from collections import deque
import random

#Sksapar en ordnad kortlek
class Cards(deque):
    
    def __init__(self,shuffled="no"):
        #1 representerar Ess, .., 13 representerar kung
        siffror = range(1,14) 

        # H = hjärter, R=Ruter, S=spader, T= treklöver
        symboler =["♥","♦","♠","♣"]

        
        for r in siffror:
            for s in symboler:
                self.append(str(s)+str(r))

        
        if shuffled == "shuffled":
            self.shuffle()

    def shuffle(self):
        random.shuffle(self)

class Hand():
    def __init__(self):
        self.cards = []

class Table():
    def __init__(self, k=[Cards("yes")]):
        self.decks = k              #Kortlekarna som skall finnas på bordet, en kortlek som standard
    
    def prettyShow(self, C=[]):     #printar fint kort ur k-listan
        #Print top borders
        if len(C) ==0: k=1
        else: k=len(C)
        
        print(" _____ "*k + "\n" +"|     |"*k)

        #print cards
        for i in range(k):

            if i == 0:
                print("|"+ "NULL |", end="")
            elif i ==2:
                print("| "+str(i)+ "  |", end="")
            else:
                print("| "+str(i)+ " |", end="")

        #print bottom borders
        print("\n"+ "|_____|"*k, end="")


#SAMPLE Runs
d = Cards()
print(d)
t = Table()
d.shuffle()

print("HELLLLLLLLOOOOOOOOOOOOOO")
t.prettyShow()

d
