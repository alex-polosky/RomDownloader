# This is the console version
# I hope to create a version with a GUI
# It would make it more pleasent
import os
from sys import exit as Exit
#import threading

from engine import DownloadLink
#from menu import Essential
from searcher import Crawler

#class Menu(Essential):
class Menu():

    def cls(self):
        if (os.name in ['nt', 'dos', 'ce']):
            os.system('cls')
        if (os.name in ['posix', 'mac']):
            os.system('clear')

    def getnum(self):
        while True:
            try:
                return int(raw_input("=> "))
            except:
                print("Invalid number")

    def getchoice(self, start, stop):
        choice = None
        while True:
            choice = self.getnum()
            if choice in range(start, stop+1):
                return choice
            else:
                print("Choice not in range")

    def header(self):
        self.cls()
        print("ROM Downloader\nV 1.0\n~ Hondros")

    def enter(self):
        raw_input("Please press 'Enter' to continue")
        print("")

    def notifier(self):
        print("To navigate menus, enter the number, and press 'Enter'")
        self.enter()

    def copyright(self):
        self.header()
        print("""\

Copyright
=========
The site 'Rom Hustler' (http://romhustler.net)
has no affliation with me as a programmer, or in general
I do not believe that the owner of this website enjoys
this program, nor do I believe that he supports piracy


I do not accept any penalties that may arise as of you
using this program to download roms that you may or may
not have. It might be illegal, I am not completely sure
Use this program at your own risk.

I grant anyone using this program the ability to
redistribute this program or it's source code, so long
as it is distributed in full

C 2010
""")
        self.enter()
        self.menu1()

    def help(self):
        self.header()
        print("Not available yet")
        self.enter()
        self.menu1()

    def menu1(self):
        self.header()
        print("""\
1) Search for roms
2) Catalog games
3) Copyright
4) Help
5) Quit
""")
        choice = self.getchoice(1, 5)
        if choice == 1:
            self.menu2()
        elif choice == 2:
            self.catalog()
        elif choice == 3:
            self.copyright()
        elif choice == 4:
            self.help()
        elif choice == 5:
            Exit()

    def menu2(self):
        self.header()
        print("""\
1) Input System
2) Choose System
3) Back
""")
        choice = self.getchoice(1, 3)
        if choice == 1:
            self.menuinput()
        elif choice == 2:
            self.menuchoose()
        elif choice == 3:
            self.menu1()

    def menuinput(self):
        self.header()
        print("Not available yet")
        self.enter()
        self.menu2()

    def menuchoose(self):
        sort = []
        for x in DownloadLink.abbrs2:
            sort.append(x)
        sort.sort()
        self.header()
        counter = 1
        for x in sort:
            if x == 'Sony PSP':
                print("%d) Sony PSP [NOT WORKING]" %(counter))
            else:
                print("%d) %s" %(counter, x))
            counter += 1
        print("%d) Back" %(counter))
        choice = self.getchoice(1, counter)
        counter = 1
        for x in sort:
            if choice == counter:
                self.menuchoose2(x)
            counter += 1
        if choice == counter:
            self.menu2()

    def menuchoose2(self, system):
        self.header()
        print("")
        print(system)
        print("""\
1) Search for game
2) Save catalog of games
3) Download all games [EXPERIMENTAL]
4) Back
""")
        choice = self.getchoice(1, 4)
        if choice == 1:
            self.menuchoose3(system)
        elif choice == 2:
            self.menuchoose4(system)
        elif choice == 3:
            self.menuchoose5(system)
        elif choice == 4:
            self.menuchoose()

    def menuchoose3(self, system):
        self.header()
        print("")
        print(system)
        print("Type ctrl+c to go back")
        print("Please enter the name of the game")
        while True:
            try:
                game = raw_input("=> ")
                break
            except KeyboardInterrupt:
                self.menuchoose2(system)
            except:
                print("Invalid data")
        print("")
        #C = Crawler(game, system)
        try:
            C = Crawler(game, system)
        except:
            print("Unknown error")
            self.enter()
            Exit()
        if len(C.games) <= 75:
            counter = 1
            for x in C.games:
                print("%s) %s" %(counter, x[1]))
                counter += 1
            print("%s) Back" %(counter))
        elif len(C.games) > 75:
            print("Too many listings, try to refine your search")
            self.menuchoose3(system)
            self.enter()
            Exit()
        choice = self.getchoice(1, counter)
        counter = 1
##        if C.multi == 0:
##            for x in C.games:
##                if choice == counter:
##                    self.menudownload(x, system)
##                counter += 1
##        elif C.multi == 1:
##            for x in C.games:
##                if choice == counter:
##                    self.menumultidownload(x, system)
##                counter += 1
        for x in C.games:
            if choice == counter:
                self.menumultidownload(x, system)
            counter += 1
        if choice == counter:
            self.menuchoose2(system)

    def menudownload(self, game, system):
        self.header()
        print("")
        print("Downloading %s for the %s" %(game[1], system))
        print("Note, depending on the size of the game, it may take a while")
        print("Please be patient")
        DL = DownloadLink(game[0], system)
        print("Download complete, it should be a .rar or a .7z")
        print("Have fun!")
        self.enter()
        Exit()

    def menumultidownload(self, game, system):
        self.menumulti_dl_no_thread(game, system)

    def menumulti_dl_no_thread(self, game, system):
        self.header()
        print("")
        print("Downloading %s for the %s" %(game[1], system))
        print("Note, depending on the size of the game, it may take a while")
        print("Please be patient")
        print("")
        print("There are %d parts for this game" %(len(game[0])))
        part = 1
        print("")
        while True:
            print("Working on %d of %d" %(part, len(game[0])))
            print(game[0][part-1])
            DL = DownloadLink(game[0][part-1])
            if part == len(game[0]):
                break
            part += 1
        print("")
        print("Download complete, there should be %d files" %(part))
        print("Open the first one, and extract whatever is in it")
        print("Have fun!")
        self.enter()
        self.menu1()

    def catalog(self):
        self.header()
        print("1) All systems")
        sort = []
        for x in DownloadLink.abbrs2:
            sort.append(x)
        sort.sort()
        counter = 2
        for x in sort:
            print("%d) %s" %(counter, x))
            counter += 1
        print("%d) Back" %(counter))
        choice = self.getchoice(1, counter)
        counter = 1
        if choice == 1:
            self.catall()
        for x in sort:
            if choice == counter:
                self.menuchoose4(x)
            counter += 1
        if choice == counter:
            self.menu1()

    def catall(self):
        self.header()
        print("")
        print("Saving All")
        print("The list of files will be saved to 'All Systems.txt'")
        self.enter()
        print("Please wait")
        f2 = open("All Systems.txt", 'w')
        sort = []
        for x in DownloadLink.abbrs2:
            sort.append(x)
        sort.sort()
        for y in sort:
            f2.write('\n')
            f2.write(y)
            f2.write('\n====================================\n')
            for x in 'abcdefghijklmnopqrstuvwyz':
                C = Crawler(x, y)
                for x in C.games:
                    f2.write(x[1])
                    f2.write('\n')
        f2.close()
        print("Finished")
        self.enter()
        self.menu1()

    def menuchoose4(self, system):
        self.header()
        print("")
        print(system)
        print("The list of files will be saved to %s.txt" %(system))
        self.enter()
        print("Please wait")
        f2 = open(system+'.txt', 'w')
        for x in 'abcdefghijklmnopqrstuvwyz':
            C = Crawler(x, system)
            for x in C.games:
                f2.write(x[1])
                f2.write('\n')
        f2.close()
        print("Finished")
        self.enter()
        self.menu1()

    def menuchoose5(self, system):
        self.header()
        print("")
        print(system)
        print("This feature has been temporarily disabled to prevent headaches for the end-user")
        self.enter()
        self.menuchoose3()

    def __init__(self):
        self.notifier()
        self.menu1()
        

Menu().menu1()
