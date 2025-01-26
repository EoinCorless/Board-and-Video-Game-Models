#TO DO
#Add ability for user to change ships without having to change code
#Add progress meter while running
#Add other race/empire abilities
#Add functionality for Sardakk N'orr self destructing ships
#Add cost variable (so you can find the most cost effective fleets)

import time
import random
start = time.time()
SimulatedGames = 100000
PrintRule = False
#PrintRule = False

class Fleet:
    #Fig=Fighter, Car=Carrier, Cru=Crusier, Des=Destroyer, Dre=DreadNought, Fla=Flagship, War=Warsun
    #2/1 shows whether a ship has 1 or 2 hp remaining (Applies only to Dreadnoughts, Flagships and Warsuns)
    #DesAFBNum is the amount of Anti-Fighter Barrages a destroyer can do (Applies only to Destroyers, and only once per combat)
    #DesAFBHit is the hit chance of a Destroyer's Anti-Fighter Barrage (Applies only to Destroyers, and only once per combat)

    def __init__(self, FigNum, FigHit,
                 CarNum, CarHit, CarCap,
                 CruNum, CruHit, CruCap,
                 DesNum, DesHit, DesAFBNum, DesAFBHit,
                 Dre2Num, Dre1Num, DreHit, DreCap,
                 Fla2Num, Fla1Num, FlaHit, FlaCap,
                 War2Num, War1Num, WarHit, WarCap):
        self.FigNum = FigNum
        self.FigHit = FigHit

        self.CarNum = CarNum
        self.CarHit = CarHit
        self.CarCap = CarCap

        self.CruNum = CruNum
        self.CruHit = CruHit
        self.CruCap = CruCap

        self.DesNum = DesNum
        self.DesHit = DesHit
        self.DesAFBNum = DesAFBNum
        self.DesAFBHit = DesAFBHit

        self.Dre2Num = Dre2Num
        self.Dre1Num = Dre1Num
        self.DreHit = DreHit
        self.DreCap = DreCap

        self.Fla2Num = Fla2Num
        self.Fla1Num = Fla1Num
        self.FlaHit = FlaHit
        self.FlaCap = FlaCap

        self.War2Num = War2Num
        self.War1Num = War1Num
        self.WarHit = WarHit
        self.WarCap = WarCap
###################################################################
Fleet1 = Fleet(8, 9,
                   2, 9, 4,
                   0, 7, 0,
                   0, 9, 2, 9,
                   0, 0, 5, 1,
                   0, 0, 6, 3,
                   0, 0, 3, 6)

Fleet2 = Fleet(0, 9,
                   0, 9, 4,
                   1, 7, 0,
                   8, 9, 2, 9,
                   0, 0, 5, 1,
                   0, 0, 6, 3,
                   0, 0, 3, 6)
###################################################################

CompletedGames = 0


F1afbHits = 0
F2afbHits = 0
Draws = 0
Fleet1Wins = 0
Fleet2Wins = 0

while(CompletedGames<SimulatedGames):
    F1afbHits = 0
    F2afbHits = 0
    Fleet1SardakkNorr = True
    Fleet1 = Fleet(8,              9,
                   2,              9, 4,
                   2,              7, 0,
                   2,              8,           3, 6,
                   2, 0, 5,  1,
                   1,  0, 6,  3,
                   0, 0, 3, 6)

    Fleet2 = Fleet(8,              9,
                   2,              9, 4,
                   2,              7, 0,
                   2,              9,           2, 9,
                   2, 0, 5,  1,
                   1,  0, 6,  3,
                   0, 0, 3, 6)

    Fleet1Capacity = (((Fleet1.War2Num+Fleet1.War1Num)*Fleet1.WarCap) +
                      ((Fleet1.Fla2Num+Fleet1.Fla1Num)*Fleet1.FlaCap) +
                      ((Fleet1.Dre2Num+Fleet1.Dre1Num)*Fleet1.DreCap) +
                      ((Fleet1.CruNum)*Fleet1.CruCap) +
                      ((Fleet1.CarNum)*Fleet1.CarCap))

    Fleet2Capacity = (((Fleet1.War2Num+Fleet1.War1Num) * Fleet1.WarCap) +
                     ((Fleet1.Fla2Num + Fleet1.Fla1Num) * Fleet1.FlaCap) +
                     ((Fleet1.Dre2Num + Fleet1.Dre1Num) * Fleet1.DreCap) +
                     ((Fleet1.CruNum) * Fleet1.CruCap) +
                     ((Fleet1.CarNum) * Fleet1.CarCap))

    if(Fleet1SardakkNorr == True):
        Fleet1.WarHit = Fleet1.WarHit - 2
        Fleet1.FlaHit = Fleet1.FlaHit - 1
        Fleet1.DreHit = Fleet1.DreHit - 2
        Fleet1.CruHit = Fleet1.CruHit - 2
        Fleet1.DesHit = Fleet1.DesHit - 2
        Fleet1.CarHit = Fleet1.CarHit - 2
        Fleet1.FigHit = Fleet1.FigHit - 2

    #AntiFighterBarrage Fleet 1 -> Fleet 2
    AFBexit = False
    while(AFBexit == False):
        TotalShots = (Fleet1.DesNum * Fleet1.DesAFBNum)
        CompletedShots = 0
        while(CompletedShots < TotalShots):
            GeneratedShot = random.randint(1,10)
            if(PrintRule == True):
                print("Anti Fighter Barrage Roll (F1)", GeneratedShot)
            if(GeneratedShot >= Fleet1.DesAFBHit):
                F1afbHits = F1afbHits + 1
            CompletedShots = CompletedShots + 1
        AFBexit = True

    # AntiFighterBarrage Fleet 2 -> Fleet 1
    AFBexit = False
    while (AFBexit == False):
        TotalShots = (Fleet2.DesNum * Fleet2.DesAFBNum)
        CompletedShots = 0
        while (CompletedShots < TotalShots):
            GeneratedShot = random.randint(1, 10)
            if (PrintRule == True):
                print("Anti Fighter Barrage Roll (F2)", GeneratedShot)
            if (GeneratedShot >= Fleet2.DesAFBHit):
                F2afbHits = F2afbHits + 1
            CompletedShots = CompletedShots + 1
        AFBexit = True

    if (PrintRule == True):
        print("F1afbHits",F1afbHits,"\nF2afbHits",F2afbHits,"\n")
    Fleet1.FigNum = Fleet1.FigNum - F2afbHits
    Fleet2.FigNum = Fleet2.FigNum - F1afbHits

    if(Fleet1.FigNum < 0):
        Fleet1.FigNum = 0

    if (Fleet2.FigNum < 0):
        Fleet2.FigNum = 0


    #CombatPhase
    CombatEnd = False
    LostFlagShip = False

    Fleet1TotalShips = (Fleet1.War2Num + Fleet1.War1Num +
                        Fleet1.Fla2Num + Fleet1.Fla1Num +
                        Fleet1.Dre2Num + Fleet1.Dre1Num +
                        Fleet1.CruNum +
                        Fleet1.CarNum +
                        Fleet1.DesNum +
                        Fleet1.FigNum)

    Fleet2TotalShips = (Fleet2.War2Num + Fleet2.War1Num +
                        Fleet2.Fla2Num + Fleet2.Fla1Num +
                        Fleet2.Dre2Num + Fleet2.Dre1Num +
                        Fleet2.CruNum +
                        Fleet2.CarNum +
                        Fleet2.DesNum +
                        Fleet2.FigNum)
    CombatCounter = 0
    while(CombatEnd == False):
        CombatCounter = CombatCounter + 1
        if (PrintRule == True):
            print("------------------------------------------------------------------->", CombatCounter,"<--------------------------------------------------------------------")
        Fleet1Hits = 0
        Fleet2Hits = 0

        if (Fleet1SardakkNorr == True):
            if(LostFlagShip == False):
                FlagShipNumber = Fleet1.Fla2Num + Fleet1.Fla1Num
                if (FlagShipNumber <= 0):
                    Fleet1.WarHit = Fleet1.WarHit + 1
                    Fleet1.DreHit = Fleet1.DreHit + 1
                    Fleet1.CruHit = Fleet1.CruHit + 1
                    Fleet1.DesHit = Fleet1.DesHit + 1
                    Fleet1.CarHit = Fleet1.CarHit + 1
                    Fleet1.FigHit = Fleet1.FigHit + 1
                    LostFlagShip = True

        Fleet1End = False
        Fleet2End = False

        while(Fleet1End == False):
            if (PrintRule == True):
                print("--->FLEET 1 SHOOTS<---")
            #Warsun Shots
            CompletedShots = 0
            TotalShots = (Fleet1.War2Num+Fleet1.War1Num)*3
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("WarSun Shot (F1)", GeneratedShot)
                if (GeneratedShot >= Fleet1.WarHit):
                    Fleet1Hits = Fleet1Hits + 1
                CompletedShots = CompletedShots + 1

            #Flagship Shots
            CompletedShots = 0
            TotalShots = (Fleet1.Fla2Num + Fleet1.Fla1Num)*2
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Flagship Shot (F1)", GeneratedShot)
                if (GeneratedShot >= Fleet1.FlaHit):
                    Fleet1Hits = Fleet1Hits + 1
                CompletedShots = CompletedShots + 1

            #Dreadnought Shots
            CompletedShots = 0
            TotalShots = (Fleet1.Dre2Num + Fleet1.Dre1Num)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Dreadnought Shot (F1)", GeneratedShot)
                if (GeneratedShot >= Fleet1.DreHit):
                    Fleet1Hits = Fleet1Hits + 1
                CompletedShots = CompletedShots + 1

            #Cruiser Shots
            CompletedShots = 0
            TotalShots = (Fleet1.CruNum)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Cruiser Shot (F1)", GeneratedShot)
                if (GeneratedShot >= Fleet1.CruHit):
                    Fleet1Hits = Fleet1Hits + 1
                CompletedShots = CompletedShots + 1

            #Destroyer Shots
            CompletedShots = 0
            TotalShots = (Fleet1.DesNum)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Destroyer Shot (F1)", GeneratedShot)
                if (GeneratedShot >= Fleet1.DesHit):
                    Fleet1Hits = Fleet1Hits + 1
                CompletedShots = CompletedShots + 1

            #Carrier Shots
            CompletedShots = 0
            TotalShots = (Fleet1.CarNum)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Carrier Shot (F1)", GeneratedShot)
                if (GeneratedShot >= Fleet1.CarHit):
                    Fleet1Hits = Fleet1Hits + 1
                CompletedShots = CompletedShots + 1

            #Fighter Shots
            CompletedShots = 0
            TotalShots = (Fleet1.FigNum)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Fighter Shot (F1)", GeneratedShot)
                if (GeneratedShot >= Fleet1.FigHit):
                    Fleet1Hits = Fleet1Hits + 1
                CompletedShots = CompletedShots + 1

            if (PrintRule == True):
                print(" ")
            Fleet1End = True

        while (Fleet2End == False):
            if (PrintRule == True):
                print("--->FLEET 2 SHOOTS<---")
            #Warsun Shots
            CompletedShots = 0
            TotalShots = (Fleet2.War2Num + Fleet2.War1Num) * 3
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("WarSun Shot (F2)", GeneratedShot)
                if (GeneratedShot >= Fleet2.WarHit):
                    Fleet2Hits = Fleet2Hits + 1
                CompletedShots = CompletedShots + 1

            #Flagship Shots
            CompletedShots = 0
            TotalShots = (Fleet2.Fla2Num + Fleet2.Fla1Num) * 2
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Flagship Shot (F2)", GeneratedShot)
                if (GeneratedShot >= Fleet2.FlaHit):
                    Fleet2Hits = Fleet2Hits + 1
                CompletedShots = CompletedShots + 1

            #Dreadnought Shots
            CompletedShots = 0
            TotalShots = (Fleet2.Dre2Num + Fleet2.Dre1Num)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Dreadnought Shot (F2)", GeneratedShot)
                if (GeneratedShot >= Fleet2.DreHit):
                    Fleet2Hits = Fleet2Hits + 1
                CompletedShots = CompletedShots + 1

            #Cruiser Shots
            CompletedShots = 0
            TotalShots = (Fleet2.CruNum)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Cruiser Shot (F2)", GeneratedShot)
                if (GeneratedShot >= Fleet2.CruHit):
                    Fleet2Hits = Fleet2Hits + 1
                CompletedShots = CompletedShots + 1

            #Destroyer Shots
            CompletedShots = 0
            TotalShots = (Fleet2.DesNum)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Destroyer Shot (F2)", GeneratedShot)
                if (GeneratedShot >= Fleet2.DesHit):
                    Fleet2Hits = Fleet2Hits + 1
                CompletedShots = CompletedShots + 1

            #Carrier Shots
            CompletedShots = 0
            TotalShots = (Fleet2.CarNum)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Carrier Shot (F2)", GeneratedShot)
                if (GeneratedShot >= Fleet2.CarHit):
                    Fleet2Hits = Fleet2Hits + 1
                CompletedShots = CompletedShots + 1

            #Fighter Shots
            CompletedShots = 0
            TotalShots = (Fleet2.FigNum)
            while (CompletedShots < TotalShots):
                GeneratedShot = random.randint(1, 10)
                if (PrintRule == True):
                    print("Fighter Shot (F2)", GeneratedShot)
                if (GeneratedShot >= Fleet2.FigHit):
                    Fleet2Hits = Fleet2Hits + 1
                CompletedShots = CompletedShots + 1

            if (PrintRule == True):
                print(" ")
            Fleet2End = True

        if (PrintRule == True):
            print("Fleet1 Hits", Fleet1Hits)
            print("Fleet2 Hits", Fleet2Hits)
            print("")

########################################################################################################################
########################################################################################################################
########################################################################################################################
        if (PrintRule == True):
            print("\nFLEET 2 PRE HITS:"
                  "\n----->FLEET SIZE:",Fleet2TotalShips,
                  "\nWarSuns (2hp)",Fleet2.War2Num,
                  "\nWarSuns (1hp)",Fleet2.War1Num,
                  "\nFlagships (2hp)", Fleet2.Fla2Num,
                  "\nFlagships (1hp)", Fleet2.Fla1Num,
                  "\nDreadnoughts (2hp)", Fleet2.Dre2Num,
                  "\nDreadnoughts (1hp)", Fleet2.Dre1Num,
                  "\nCruisers", Fleet2.CruNum,
                  "\nDestroyers", Fleet2.DesNum,
                  "\nCarriers", Fleet2.CarNum,
                  "\nFighters", Fleet2.FigNum,
                  "\n")

        #Handling Fleet 1 Hits
        #Current System is dumb, update later
        while(Fleet1Hits >= 0):

            if (Fleet1Hits <= 0):
                break
            while(Fleet2.Dre2Num > 0):
                Fleet2.Dre2Num = Fleet2.Dre2Num - 1
                Fleet2.Dre1Num = Fleet2.Dre1Num + 1
                if(PrintRule == True):
                    print("Fleet 2 took damage on a Dreadnought")
                Fleet1Hits = Fleet1Hits - 1
                if(Fleet1Hits <= 0):
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.Fla2Num > 0):
                Fleet2.Fla2Num = Fleet2.Fla2Num - 1
                Fleet2.Fla1Num = Fleet2.Fla1Num + 1
                if (PrintRule == True):
                    print("Fleet 2 took damage on their Flagship")
                Fleet1Hits = Fleet1Hits - 1
                if (Fleet1Hits <= 0):
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.War2Num > 0):
                Fleet2.War2Num = Fleet2.War2Num - 1
                Fleet2.War1Num = Fleet2.War1Num + 1
                if (PrintRule == True):
                    print("Fleet 2 took damage on a Warsun")
                Fleet1Hits = Fleet1Hits - 1
                if (Fleet1Hits <= 0):
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.FigNum > 0):
                Fleet2.FigNum = Fleet2.FigNum - 1
                if (PrintRule == True):
                    print("Fleet 2 lost a Fighter")
                Fleet1Hits = Fleet1Hits - 1
                if (Fleet1Hits <= 0):
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.DesNum > 0):
                Fleet2.DesNum = Fleet2.DesNum - 1
                if (PrintRule == True):
                    print("Fleet 2 lost a Destroyer")
                Fleet1Hits = Fleet1Hits - 1
                if (Fleet1Hits <= 0):
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.CarNum > 0):
                if (Fleet2Capacity >= Fleet2.FigNum+4):
                    Fleet2.CarNum = Fleet2.CarNum - 1
                    if (PrintRule == True):
                        print("Fleet 2 lost a Carrier")
                    Fleet1Hits = Fleet1Hits - 1
                    if (Fleet1Hits <= 0):
                        break
                else:
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.CruNum > 0):
                Fleet2.CruNum = Fleet2.CruNum - 1
                if (PrintRule == True):
                    print("Fleet 2 lost a Cruiser")
                Fleet1Hits = Fleet1Hits - 1
                if (Fleet1Hits <= 0):
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.Dre1Num > 0):
                Fleet2.Dre1Num = Fleet2.Dre1Num - 1
                if (PrintRule == True):
                    print("Fleet 2 lost a Dreadnought")
                Fleet1Hits = Fleet1Hits - 1
                if (Fleet1Hits <= 0):
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.CarNum > 0):
                Fleet2.CarNum = Fleet2.CarNum - 1
                if (PrintRule == True):
                    print("Fleet 2 lost a Carrier")
                Fleet1Hits = Fleet1Hits - 1
                if (Fleet1Hits <= 0):
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.Fla1Num > 0):
                Fleet2.Fla1Num = Fleet2.Fla1Num - 1
                if (PrintRule == True):
                    print("Fleet 2 lost their Flagship")
                Fleet1Hits = Fleet1Hits - 1
                if (Fleet1Hits <= 0):
                    break

            if (Fleet1Hits <= 0):
                break
            while (Fleet2.War1Num > 0):
                Fleet2.War1Num = Fleet2.War1Num - 1
                if (PrintRule == True):
                    print("Fleet 2 lost a Warsun")
                Fleet1Hits = Fleet1Hits - 1
                if (Fleet1Hits <= 0):
                    break

            break

        Fleet2TotalShips = (Fleet2.War2Num + Fleet2.War1Num +
                            Fleet2.Fla2Num + Fleet2.Fla1Num +
                            Fleet2.Dre2Num + Fleet2.Dre1Num +
                            Fleet2.CruNum +
                            Fleet2.CarNum +
                            Fleet2.DesNum +
                            Fleet2.FigNum)
        if (PrintRule == True):
            print("\nFLEET 2 POST HITS:"
                  "\n----->FLEET SIZE:",Fleet2TotalShips,
                  "\nWarSuns (2hp)", Fleet2.War2Num,
                  "\nWarSuns (1hp)", Fleet2.War1Num,
                  "\nFlagships (2hp)", Fleet2.Fla2Num,
                  "\nFlagships (1hp)", Fleet2.Fla1Num,
                  "\nDreadnoughts (2hp)", Fleet2.Dre2Num,
                  "\nDreadnoughts (1hp)", Fleet2.Dre1Num,
                  "\nCruisers", Fleet2.CruNum,
                  "\nDestroyers", Fleet2.DesNum,
                  "\nCarriers", Fleet2.CarNum,
                  "\nFighters", Fleet2.FigNum,
                  "\n")
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
        if (PrintRule == True):
            print("\nFLEET 1 PRE HITS:"
                  "\n----->FLEET SIZE:",Fleet1TotalShips,
                  "\nWarSuns (2hp)", Fleet1.War2Num,
                  "\nWarSuns (1hp)", Fleet1.War1Num,
                  "\nFlagships (2hp)", Fleet1.Fla2Num,
                  "\nFlagships (1hp)", Fleet1.Fla1Num,
                  "\nDreadnoughts (2hp)", Fleet1.Dre2Num,
                  "\nDreadnoughts (1hp)", Fleet1.Dre1Num,
                  "\nCruisers", Fleet1.CruNum,
                  "\nDestroyers", Fleet1.DesNum,
                  "\nCarriers", Fleet1.CarNum,
                  "\nFighters", Fleet1.FigNum,
                  "\n")

        # Handling Fleet 2 Hits
        # Current System is dumb, update later
        while (Fleet2Hits >= 0):

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.Dre2Num > 0):
                Fleet1.Dre2Num = Fleet1.Dre2Num - 1
                Fleet1.Dre1Num = Fleet1.Dre1Num + 1
                if (PrintRule == True):
                    print("Fleet 1 took damage on a Dreadnought")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.Fla2Num > 0):
                Fleet1.Fla2Num = Fleet1.Fla2Num - 1
                Fleet1.Fla1Num = Fleet1.Fla1Num + 1
                if (PrintRule == True):
                    print("Fleet 1 took damage on their Flagship")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.War2Num > 0):
                Fleet1.War2Num = Fleet1.War2Num - 1
                Fleet1.War1Num = Fleet1.War1Num + 1
                if (PrintRule == True):
                    print("Fleet 1 took damage on their Warsun")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.FigNum > 0):
                Fleet1.FigNum = Fleet1.FigNum - 1
                if (PrintRule == True):
                    print("Fleet 1 lost a Fighter")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.DesNum > 0):
                Fleet1.DesNum = Fleet1.DesNum - 1
                if (PrintRule == True):
                    print("Fleet 1 lost a Destroyer")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.CarNum > 0):
                if (Fleet1Capacity >= Fleet1.FigNum + 4):
                    Fleet1.CarNum = Fleet1.CarNum - 1
                    if (PrintRule == True):
                        print("Fleet 1 lost a Carrier")
                    Fleet2Hits = Fleet2Hits - 1
                    if (Fleet2Hits <= 0):
                        break
                else:
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.CruNum > 0):
                Fleet1.CruNum = Fleet1.CruNum - 1
                if (PrintRule == True):
                    print("Fleet 1 lost a Cruiser")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.Dre1Num > 0):
                Fleet1.Dre1Num = Fleet1.Dre1Num - 1
                if (PrintRule == True):
                    print("Fleet 1 lost a Dreadnought")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.CarNum > 0):
                Fleet1.CarNum = Fleet1.CarNum - 1
                if (PrintRule == True):
                    print("Fleet 1 lost a Carrier")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.Fla1Num > 0):
                Fleet1.Fla1Num = Fleet1.Fla1Num - 1
                if (PrintRule == True):
                    print("Fleet 1 lost their Flagship")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            if (Fleet2Hits <= 0):
                break
            while (Fleet1.War1Num > 0):
                Fleet1.War1Num = Fleet1.War1Num - 1
                if (PrintRule == True):
                    print("Fleet 1 lost a Warsun")
                Fleet2Hits = Fleet2Hits - 1
                if (Fleet2Hits <= 0):
                    break

            break

        Fleet1TotalShips = (Fleet1.War2Num + Fleet1.War1Num +
                            Fleet1.Fla2Num + Fleet1.Fla1Num +
                            Fleet1.Dre2Num + Fleet1.Dre1Num +
                            Fleet1.CruNum +
                            Fleet1.CarNum +
                            Fleet1.DesNum +
                            Fleet1.FigNum)
        if (PrintRule == True):
            print("\nFLEET 1 POST HITS:"
                  "\n----->FLEET SIZE:",Fleet1TotalShips,
                  "\nWarSuns (2hp)", Fleet1.War2Num,
                  "\nWarSuns (1hp)", Fleet1.War1Num,
                  "\nFlagships (2hp)", Fleet1.Fla2Num,
                  "\nFlagships (1hp)", Fleet1.Fla1Num,
                  "\nDreadnoughts (2hp)", Fleet1.Dre2Num,
                  "\nDreadnoughts (1hp)", Fleet1.Dre1Num,
                  "\nCruisers", Fleet1.CruNum,
                  "\nDestroyers", Fleet1.DesNum,
                  "\nCarriers", Fleet1.CarNum,
                  "\nFighters", Fleet1.FigNum,
                  "\n")

########################################################################################################################
########################################################################################################################
########################################################################################################################

        if(Fleet1TotalShips + Fleet2TotalShips == 0):
            if (PrintRule == True):
                print("----------------------------------------------------------------> D R A W <-----------------------------------------------------------------")
                print("Fleet 1 Size:",Fleet1TotalShips,
                      "\nFleet 2 Size:",Fleet2TotalShips)
            Draws = Draws + 1
            AFBexit = True
            CombatEnd = True
            CompletedGames = CompletedGames + 1
            break

        elif (Fleet2TotalShips == 0):
            if (PrintRule == True):
                print("---------------------------------------------------------> F L E E T  1  W I N S <----------------------------------------------------------")
                print("Fleet 1 Size:", Fleet1TotalShips,
                      "\nFleet 2 Size:", Fleet2TotalShips)
            Fleet1Wins = Fleet1Wins + 1
            AFBexit = True
            CombatEnd = True
            CompletedGames = CompletedGames + 1
            break

        elif (Fleet1TotalShips == 0):
            if (PrintRule == True):
                print("---------------------------------------------------------> F L E E T  2  W I N S <----------------------------------------------------------")
                print("Fleet 1 Size:", Fleet1TotalShips,
                      "\nFleet 2 Size:", Fleet2TotalShips)
            Fleet2Wins = Fleet2Wins + 1
            AFBexit = True
            CombatEnd = True
            CompletedGames = CompletedGames + 1
            break

print(CompletedGames)
TotalGames = Fleet1Wins+Fleet2Wins+Draws
Fleet1WinRate = Fleet1Wins/TotalGames
Fleet2WinRate = Fleet2Wins/TotalGames
DrawRate = Draws/TotalGames

Fleet1WinRate = Fleet1WinRate*100
Fleet2WinRate = Fleet2WinRate*100
DrawRate = DrawRate*100

Fleet1WinRate = round(Fleet1WinRate, 2)
Fleet2WinRate = round(Fleet2WinRate, 2)
DrawRate = round(DrawRate, 2)

Fleet1WinRate = str(Fleet1WinRate)
Fleet2WinRate = str(Fleet2WinRate)
DrawRate = str(DrawRate)

print("-------->RESULTS<--------"
      "\n     Total Games:",TotalGames,
      "\n    Fleet 1 Wins:",Fleet1Wins,
      "\n    Fleet 2 Wins:",Fleet2Wins,
      "\n           Draws:",Draws,
      "\nFleet 1 Win rate: "+Fleet1WinRate+"%",
      "\nFleet 2 Win rate: "+Fleet2WinRate+"%",
      "\n       Draw rate: "+DrawRate+"%",)


end = time.time()
taken = end - start
print("start",start)
print("end",end)
taken = round(taken,6)
print("taken",taken)