# coding=utf-8

class GameEngine():


    def __init__(self):
        self.cash = 2000
        self.invest = 100
        self.givecards = 5

    def win(self):
        pass

    def loss(self):
        pass

    def printMenu(self, menu=1):
        print("""
        ╓─────────────────────────────────────────────╖
        ║              CARD MASTER SUITE              ║
        ╠═════════════════════╦═══════════════════════╣
        ║   Cards to give: 5  ║ Cash: 0000000000000000║
        ╚═════════════════════╩═══════════════════════╝""", end="")

        if menu == 1:
            print("""
        ╔═════════════════════════════════════════════╗
            Main menu

            Start new game
            Change investing power
            Change Cardsgive (5)


        ╚═════════════════════════════════════════════╝""")

#Last tester do it do it do it!

        elif menu == 2:
            pass

        return None


def main():
    pass

main()