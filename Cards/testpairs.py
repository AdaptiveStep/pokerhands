#!/usr/bin/env python
# -*- coding: utf8 -*-


import random

#Skapar en ordnad kortlek
class Cards(list):

    def __init__(self,shuffled="no"):
        self.pointer = 0 #used in check for wins.

        #1 representerar Ess, .., 13 representerar kung
        siffror = range(1,14)

        # H = hjärter, R=Ruter, S=spader, T= treklöver
        symboler =["♥","♦","♠","♣"] # 0,1,2,3

        for r in symboler:
            for s in siffror:
                self.append(str(r)+str(s))

        if shuffled == "shuffled":
            self.shuffle()

    def shuffle(self):
        random.shuffle(self)
    def Ntipples(self, N=2):
    #check for pairs:
        counter = 1
        cards = self.copy()
        templist =[]
        for i in cards:
            minilist =[]

            h = cards.count("♥" + i[1:])
            if h == 1:
                minilist.append("♥" + i[1:])
                cards.remove("♥" + i[1:])

            s = cards.count("♠" + i[1:])
            if s == 1:
                minilist.append("♠" + i[1:])
                cards.remove("♠" + i[1:])

            r = cards.count("♦" + i[1:])
            if r == 1:
                minilist.append("♦" + i[1:])
                cards.remove("♦" + i[1:])

            k = cards.count("♣" + i[1:])
            if k == 1:
                minilist.append("♣" + i[1:])
                cards.remove("♣" + i[1:])

            totalt = int(h + s + r + k)

            if totalt >= 2 and totalt >=N:

                if N == 2 and totalt ==2 or N == 2 and totalt == 3:
                    templist.append(minilist)

                elif N==2 and totalt ==4:
                    templist.append([minilist[0],minilist[1]])
                    templist.append([minilist[2],minilist[3]])

                elif N >=3 and totalt >=3:
                    templist.append(minilist)

        return templist
    def hasPairs(self):
        #check for pairs:
        return len(self.Ntipples(2))>0
    def hasTripples(self):
        return len(self.Ntipples(3))>0
    def hasQuads(self):
        return len(self.Ntipples(4))>0
    def hasKauk(self):
        if self.hasPairs() and self.hasTripples():
            return True
        else:
            return False
    def hasLadder(self,n=5):
        counter=0
        cardsremaining = len(self.copy())
        templist=[]
        tempcards = self.copy()

        tempcards.sort()
        while cardsremaining > n:
            if tempcards[counter] == tempcards[counter+1]-1:
                counter+=1
    def hasColors(self,n=5,interval="atleast"):

        """
        n representerar hur många av en symbol man söker minst/mest/exakt av.
        Interval kan vara någon av atleast, atmost, exact
        """
        interval = str(interval)
        colors = self.Colors(n,interval)
        return len(colors)>0

    def Colors(self,n=5,interval="atleast"):
        """
        n representerar hur många av en symbol man söker minst/mest/exakt av.
        Interval kan vara någon av atleast, atmost, exact
        """
        counter = 1
        cards = self.copy()
        templist = []
        interval = str(interval)
        tcounter,scounter, hcounter,rcounter = 0,0,0,0

        #rakna hjartan
        for i in kortlek:
            if "♣" in i: tcounter += 1
            elif "♠" in i: scounter += 1
            elif "♥" in i: hcounter += 1
            elif "♦" in i: rcounter += 1

        if interval == "atleast":
            if tcounter >= n:
                templist.append((tcounter, "♣"))
            if scounter >= n:
                templist.append((scounter, "♠"))
            if hcounter >= n:
                templist.append((hcounter, "♥"))
            if rcounter >= n:
                templist.append((rcounter, "♦"))
        elif interval =="atmost":
            if tcounter <= n:
                templist.append((tcounter, "♣"))
            if scounter <= n:
                templist.append((scounter, "♠"))
            if hcounter <= n:
                templist.append((hcounter, "♥"))
            if rcounter <= n:
                templist.append((rcounter, "♦"))
        elif interval =="exact":
            if tcounter == n:
                templist.append((tcounter, "♣"))
            if scounter == n:
                templist.append((scounter, "♠"))
            if hcounter == n:
                templist.append((hcounter, "♥"))
            if rcounter == n:
                templist.append((rcounter, "♦"))

        #Skickar dock tom lista om inget har fyllts in.
        return templist


## Vinster som räknas:
## Par (P), Triss (T), kåk(K),Fyrtal (F), stege (S), färg (C)
## [P,T,F,K,S,C]

## (hur många finns det av varje?)



#
#print()
#print("Pairs: ", kortlek.Pairs())

# ############ ####### SAMPLE DATA ######### ##########
loopcounter = 0
while 1:

    kortlek = Cards("shuffled")
    for i in range(40):
        kortlek.pop()

    print(kortlek)
    print()

    #print("Tripples: ", kortlek.Tripples())
    k = 4
    print("HAR,",k,"tippler: ", kortlek.Ntipples(k))
    print()

    q = 4

    print("Dessa symboler förekommer minst", q,"antal gånger: ", kortlek.Colors(q))
    print("Har",q ," färger: ", kortlek.hasColors(q))
    print("HAR PAR: ", kortlek.hasPairs(), kortlek.Ntipples())
    print("HAR TRISS: ", kortlek.hasTripples())
    print("HAR FYRTAL: ", kortlek.hasQuads())
    print("HAR FÄRG: ", kortlek.hasColors(5))
    print("HAR KÅK: ", kortlek.hasKauk())

    #print("This is kortlek tripples: ",kortlek.Tripples())


    print(" ")
    print(" ")
    loopcounter +=1
    print("ANTAL UTDELNINGAR: ",loopcounter,"\n -------------------")

    if kortlek.hasColors(5):
        break