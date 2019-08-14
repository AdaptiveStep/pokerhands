#!/usr/bin/env python
# -*- coding: utf8 -*-

import random
from collections import OrderedDict

#Skapar en ordnad kortlek
class Cards(list):
    
    def __init__(self,shuffled="no",empty=False,startcards=[]):
        if len(startcards) >0:      #Om man vil skapa en hand artificiellt vid initiering
            for startcard in startcards:
                self.append(startcard)
            return
        elif empty:
            return   #Om en tom kortlek söks

        #Skapar annars en hel kortlek

        #1 representerar Ess, .., 13 representerar kung
        siffror = range(1,14)

        # H = hjärter, R=Ruter, S=spader, T= treklöver
        symboler =["♥","♦","♠","♣"]

        for r in symboler:
            for s in siffror:
                self.append(str(r)+str(s))

        if shuffled == "shuffled":
            self.shuffle()

    def shuffle(self):
        random.shuffle(self)
    def tsortByNumber(self):
        #Tar emot en kortlek, ger en siffer-sorterad kortlek.

        lista = self.copy()
        #En lista med med formen ['♥2', '♠5', '♣6'] matas in som parameter
        lista.sort(key=lambda k: int(k[1:]))
        return lista

    #denna kan tillhöra game klassen
    def deckDifference(self,deck2=[]):
        """
            Man skall alltså ta bort elementen som finns i deck1 från self. self ska reduceras.
            Kan ta emot både lista av kort, eller Card objekt
            Returnerar ett Card object
        """

        #om det finns något i deck, så skall nedanstående göras
        if len(deck2) !=0:
            templist1 = Cards(startcards=self.copy())
            templist2 = Cards(startcards=deck2.copy())
            for card2 in templist2:
                templist1.remove(card2)
            return templist1

        #Annars gör inget
        else: return Cards(empty=True)
    def getLadder(self, steps=5, startnumber=0):
        """

        Returnerar formen (True, ['♦5', '♣6', '♣7', '♣8', '♠9']*) ,     *detta är dock ett Cards object
        """

        #sorterar (en kopia) för given kortlek ['♠5', '♥2', '♣6'] enligt siffror
        deck = self.tsortByNumber()

        #Skapar en extra ordnad dictionary och minimerad lista
        j = OrderedDict((value[1:], str(value)) for value in deck)
        u = []   #Denna kommer användas främst, det är en sorterad lista med ickeduplikat siffror = steps       #är som standard 5, kan dock vara större för större händer.
        stegesstorlek = steps

        #Skapar en ordnad lista u, av handen
        for value in j:
            u.append(value)

        #För varje förflyttningsenhet, gör följande.
        for i in range(len(j) - stegesstorlek + 1):
            templista1 = []


            #bygger upp minilista (förflyttningsenhet)
            for X in range(stegesstorlek):

                if startnumber >0:
                    if int(u[i+X]) == startnumber and len(templista1)==0:
                        templista1.append(u[i + X])

                    elif len(templista1) != 0:
                        templista1.append(u[i + X])


                else: templista1.append(u[i+X])

            stepcounter = 1
            if len(templista1)!=5:      #Om minilistan blev tom, så kör nästa förflyttningsenhet
                continue


            #Undersöker flyttningsenheten nu
            counter3 = 0
            for L in templista1:

                #prövar om det går att flytta minilistan mer åt höger
                try:
                    shifter = int(templista1[counter3 + 1]) - 1
                except IndexError:
                    continue

                #Är talet 1 mindre än nästa tal?
                if int(L) == shifter:
                    stepcounter += 1

                    #Om den är det, och vi har rört oss 5 steg framåt.
                    if int(L) == shifter and stegesstorlek == stepcounter:

                        #Rebuild ladder
                        templista2 = Cards(empty=True)
                        for b in templista1:
                            templista2.append(j[str(b)])
                        return (True, templista2)
                else:
                    stepcounter = 0

                counter3 += 1

        #Om inget
        return (False, Cards(empty=True))
    def allLadders(self,steps=5,):
        """
        Tar emot lista eller Cards objekt
        Returnerar Cards objekt
        """
        bigtemplist = Cards(startcards=self.copy())
        #Om den är av formen (TRUE, ['♦12', '♥6', '♥7']) , gör om till enkel ['♦12', '♥6', '♥7']
        if bigtemplist.__repr__()[0] == "(":
            bigtemplist = bigtemplist[1]
        ##skapa en 1/3's clon av bigtemplist, för att sedan reducera bigtemplist lite. Används för att visa att deckDifference funkar
        #thirdlist = []
        #reductioncounter = 0
        #for i in bigtemplist:
        #    thirdlist.append(i)
        #    reductioncounter+=1
        #    if reductioncounter >= int(len(bigtemplist)/3):
        #        break

        ladderslist = []

        while len(bigtemplist.getLadder(steps=steps)[1]) >0:
            ladderslist.append(bigtemplist.getLadder(steps=steps)[1])
            bigtemplist = bigtemplist.deckDifference(deck2=bigtemplist.getLadder(steps=steps)[1])


        return ladderslist

    def Ntipples(self, N=2):
        """
        Returnerar en lista med Ntippler tex [ ['♥9', '♠9', '♦9'],['♥8', '♦8', '♣8'] ]
        """
    #check for pairs:
        counter = 1
        cards = self.copy()
        templist = []
        for i in cards[:]:
            minilist = []
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

            if totalt >= 2 and totalt >= N and minilist not in templist:

                if N == 2 and totalt == 2 or N == 2 and totalt == 3:
                    templist.append(minilist)

                elif N == 2 and totalt == 4:
                    templist.append([minilist[0], minilist[1]])
                    templist.append([minilist[2], minilist[3]])

                elif N >= 3 and totalt >= 3:
                    templist.append(minilist)

        return templist

    def hasPairs(self):
        #check for pairs:
        return len(self.Ntipples(2)) > 0
    def hasTripples(self):
        return len(self.Ntipples(3)) > 0
    def hasQuads(self):
        return len(self.Ntipples(4)) > 0
    def hasKauk(self):
        if self.hasPairs() and self.hasTripples():
            return True
        else:
            return False
    def hasLadder(self, n=5):
        counter = 0
        cardsremaining = len(self.copy())
        templist = []
        tempcards = self.copy()

        tempcards.sort()
        while cardsremaining > n:
            if tempcards[counter] == tempcards[counter + 1] - 1:
                counter += 1
    def hasColors(self, n=5, interval="atleast"):

        """
        n representerar hur många av en symbol man söker minst/mest/exakt av.
        Interval kan vara någon av atleast, atmost, exact
        """
        interval = str(interval)
        colors = self.Colors(n, interval)
        return len(colors) > 0

    def Colors(self,N=5, interval="atleast"):
        """
       N representerar hur många av en symbol man söker minst/mest/exakt av.
        Interval kan varaNågon av atleast, atmost, exact
        """
        counter = 1
        cards = self.copy()
        templist = []
        interval = str(interval)
        tcounter, scounter, hcounter, rcounter = 0, 0, 0, 0

        #rakna hjartan
        for i in cards:
            if "♣" in i:
                tcounter += 1
            elif "♠" in i:
                scounter += 1
            elif "♥" in i:
                hcounter += 1
            elif "♦" in i:
                rcounter += 1

        if interval == "atleast":
            if tcounter >=N:
                templist.append((tcounter, "♣"))
            if scounter >=N:
                templist.append((scounter, "♠"))
            if hcounter >=N:
                templist.append((hcounter, "♥"))
            if rcounter >=N:
                templist.append((rcounter, "♦"))
        elif interval == "atmost":
            if tcounter <=N:
                templist.append((tcounter, "♣"))
            if scounter <=N:
                templist.append((scounter, "♠"))
            if hcounter <=N:
                templist.append((hcounter, "♥"))
            if rcounter <=N:
                templist.append((rcounter, "♦"))
        elif interval == "exact":
            if tcounter ==N:
                templist.append((tcounter, "♣"))
            if scounter ==N:
                templist.append((scounter, "♠"))
            if hcounter ==N:
                templist.append((hcounter, "♥"))
            if rcounter ==N:
                templist.append((rcounter, "♦"))

        #Skickar dock tom lista om inget har fyllts in.
        return templist

class Table():
    symbolnamn = {}
    symbolnamn["♥"] = "Hjärter"
    symbolnamn["♦"] = "Ruter"
    symbolnamn["♠"] = "Spader"
    symbolnamn["♣"] = "Klöver"

    symbolnamn[1]  = "Esset"
    symbolnamn[2]  = "Tvåan"
    symbolnamn[3]  = "Trean"
    symbolnamn[4]  = "Fyran"
    symbolnamn[5]  = "Femma"
    symbolnamn[6]  = "Sexan"
    symbolnamn[7]  = "Sjuan"
    symbolnamn[8]  = "Åttan"
    symbolnamn[9]  = "Niand"
    symbolnamn[10] = "Tiand"
    symbolnamn[11] = "Knekt"
    symbolnamn[12] = "Damen"
    symbolnamn[13] = "Kunge"

    def __init__(self, k=[Cards("no")]):
        self.decks = k              #Kortlekarna som skall finnas på bordet, en kortlek som standard

    def printRow(self,card=""):
        """
        Används för att printa en rad med symboler korrekt
        """
        if len(card) == 1:
            print("║  " + str(card) + "  ║", end="")
        elif len(card) == 2:
            print("║ " + str(card) + "  ║", end="")
        elif len(card) == 3:
            print("║ " + str(card) + " ║", end="")

    def prettyShow(self, C=[],perrow=5):

    #printar fint len([]) antal kort, ur en kortlek C
    #OBS OBS Printar ut dom i omvänd ordning!! (så att poppning sker på "första" elementet)
    #Om inga kort skickas in visas null kortet.

        if len(C)==0:
            print("Player has no card")
            return
        if perrow ==0 or perrow < 0 or perrow > len(C):
            perrow = len(C)

        if len(C)%perrow !=0:
            extra = 1
        else: extra=0


        rows = (len(C)-len(C)%perrow)/(perrow) + 1
        #Used for top borders
        if len(C) == 0:
            k = 1
        else:
            k = len(C)

        #Används för att skapa en nya rader, fungerar som bjällror
        totalcards = len(C)
        cardcounter1 = 0
        cardcounter2 = 0
        cardcounter3 = 0
        rowcounter = 0

        cardcounter4 = 0        #Counts the numbers below the cards

        while cardcounter3 < totalcards:
            rowcounter += 1

        #Print top borders
            if cardcounter1 != totalcards:
                if rowcounter != rows:
                    print("\n"+"╔═════╗" *perrow)
                else:
                    print("\n"+"╔═════╗" *(totalcards%perrow))

            #printar första raden av symbolnamn
            for i in range(perrow):
                if cardcounter1 ==totalcards:
                    break
                diff1 = totalcards-cardcounter1-1
                if diff1==-1: diff1=0

                print("║"+Table.symbolnamn[C[diff1][0]][0:5].upper()+"║", end="")
                cardcounter1 +=1
                #print cards
            print()

            for i in range(perrow):
                if cardcounter2 ==totalcards:
                    break
                diff2 = totalcards - cardcounter2 - 1
                if diff2 == -1: diff2 = 0
                self.printRow(C[diff2])
                cardcounter2 += 1

            print()
            for i in range(perrow):
                if cardcounter3 ==totalcards:
                    break
                diff3 = totalcards - cardcounter3 - 1
                if diff3 == -1: diff3 = 0
                print("║"+Table.symbolnamn[int(C[diff3][1:3])][0:5].upper()+"║", end="")
                cardcounter3 +=1

            if cardcounter3 != totalcards:
                if rowcounter != rows:
                    print("\n" + "╚═════╝" * perrow)

                    for i in range(perrow):
                        cardcounter4 +=1
                        buildstring= str(cardcounter4)+"   "
                        buildstring = buildstring[0:2]
                        print("  ",buildstring+"  ",end="")

                    #print("\n" + "   1   " * perrow,end="")

            else:
                if totalcards%perrow != 0:
                    print("\n" + "╚═════╝" * (totalcards % perrow),end="")
                    print()

                    for i in range(totalcards % perrow):
                        cardcounter4 += 1
                        buildstring = str(cardcounter4) + "   "
                        buildstring = buildstring[0:2]
                        print("  ", buildstring + "  ", end="")
                        #print("   2   ",end="")
                else:
                    print("\n" + "╚═════╝" * (perrow))

                    for i in range(perrow):
                        cardcounter4 += 1
                        buildstring = str(cardcounter4) + "   "
                        buildstring = buildstring[0:2]
                        print("  ", buildstring + "  ", end="")

                        #print("   3   ",end="")

    def shuffle(self,deck=0):
        self.decks[deck].shuffle()

    def give(self,deck=0,player=None,amount=5):   #Kortlekarna heter deck=1, deck=2 osv, dvs de har siffror som namn
        if player is not None:
            if amount > len(self.decks[deck]):
                amount = len(self.decks[deck])
                print("\nCards missing, only",amount,"left.")
            for i in range(amount):
                player.recieve(self.decks[deck].pop())
        else:
            return

    def fixnumber(self,C=[],n=0):
        if len(C)==0 or n==0:
            pass
        else:
            return len(C)-n

class Player():
    def __init__(self):
        self.cards = Cards(empty=True)
    def recieve(self,card=None):
        if card is not None:
            self.cards.append(card)
        else:
            pass
    def shuffle(self):
        for i in range(17%len(self.cards)): #Lite mer slumpkänsla
            random.shuffle(self.cards)
    def cardSelect(self, select=[]):            #Gör ett korrekt urval av korten tex [1,9,4] som finns på display
        return Game().cardSelect(self.cards,select)

class Game():
    def __init__(self,shuffle="unshuffled"):
        self.table = Table([Cards(shuffle)])  #Skapa ett bord med en blandad kortlek
        self.player = []
        self.player.append(Player())
    def newgame(self):      #Vid varje game finns det en lista av spelare
        self.table = Table([Cards("unshuffled")])
        self.player =[]
        self.player.append(Player())
    def cardSelect(self, C=[], select=[]):  # C är kortlek, select är lista av val (från pretty printen), tex [2,4,5]
        # 5, 6,7 väljs, då ska egentligen lenC-5-1, lenC-6-1 och lenC-7-1 väljas

        if len(C) == 0:       #om ingen kortlek skickas in
            return
        else:
            templist = []
            for i in select:
                templist.append(C[len(C) - int(i)])
            templist.reverse()
            return templist
    def greatLoop(self,handcards=5):
        counter = 0

        #Vinst kan vara par ,"triss", "kåk", "fyrtal", "färg", "stege", "färg13" (obs fyra färger), "superkåk" (triss och fyrtal)

        #----- Ändra endast dessa ----#
        winningCondition1 = "stege"
        winningCondition2 = "triss"
        winningCondition3 = "färg"
        amountCards = handcards
        newDeckEachTime = True

        #----------------------------#
        while 1:
            if newDeckEachTime:
                self.table.decks[0] = Cards("shuffled")

            self.player[0].cards=Cards(empty=True)
            counter += 1

            #self.table.prettyShow(self.player[0].cards,perrow=13)
            maindeck = self.table.decks[0]
            maintable = self.table
            cardstogive = amountCards
            if len(maindeck) ==0:
                print("\n\n\tSlut på kort, avbryter.")
                break
            maintable.give(0, self.player[0], cardstogive)


            maindeck2 = self.player[0].cards
            winningDict = {"kåk": maindeck2.hasKauk(),
                                "par": maindeck2.hasPairs(),
                                "stege": maindeck2.getLadder()[0],
                                "färg": maindeck2.hasColors(),
                                "fyrtal": maindeck2.hasQuads(),
                                "triss": maindeck2.hasTripples(),
                                "färg13": maindeck2.Colors(N=13)!=[],
                                "superkåk": maindeck2.hasTripples() and maindeck2.hasQuads(),
                                "": True
            }

            #Lägger in allt i en lista så att anropen mot dictionary bara behöver ske en gång
            winningregistry = [winningDict[winningCondition1],winningDict[winningCondition2],winningDict[winningCondition3]]
            if winningregistry[0] and winningregistry[1] and winningregistry[2]:
                print("\n Tar Nya kort för ", counter, "gången.", end="")

                self.table.prettyShow(self.player[0].cards, perrow=13)

                print("\nEfter att ha tagit kort", counter, "gånger fås: \n")
                print("STEGE fås:", maindeck2.getLadder())

                pairs = maindeck2.Ntipples(2)
                print(len(pairs),"PAR fås: ", maindeck2.hasPairs(), pairs)
                print("TRISS fås: ", maindeck2.hasTripples() , maindeck2.Ntipples(3))
                print("FYRTAL fås: ", maindeck2.hasQuads(), maindeck2.Ntipples(4))
                print("FÄRG fås: ", maindeck2.hasColors(), maindeck2.Colors())
                print("KÅK FÅS: ", maindeck2.hasKauk())

                print("-------------------------")
                print("FÄRG13: ", maindeck2.Colors(N=13)!=[])
                print("SuperKåk:",maindeck2.hasTripples() and maindeck2.hasQuads())

                allladders= maindeck2.allLadders()
                print("All Ladders: ",len(allladders), allladders)
                input("Press anykey to rerun!")
                counter = 0
def main():
    #SAMPLE Run
    newgame = Game("shuffled")      #Creates new game object, with a table, with a shuffled deck
    newgame.greatLoop(15)
main()