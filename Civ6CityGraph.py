##REQUIRES NUMPY AND MATPLOTLIB##
#Eoin Corless
#This models the growth of cities in Civilization 6 using different city growth methods, and which one provides the most production.
import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt
#Food growth thresholds seen in the Array below are hardcoded into Civ6, so this will have to do.
FoodGrowth=[0,15,24,33,44,55,66,77,89,101,114,126,139,152,165,179,193,207,221,235,249,264,279,294,309,324,340,355,371,387,403]#1->30
Turn=0
TurnArr=[]
PopulationFOOD=1
FoodBasketFOOD=0
TotalProductionFOOD=0
ProductionArrFOOD=[]
#Focus->Resource
FocusFoodProd=1
FocusFoodFood=3
FocusProdProd=3
FocusProdFood=1
BalancedFood=2
BalancedProd=2
TurnLimit=int(input("Turn limit?:"))
##
##MAKE SIM FOR SWAPPING FOCUS AT 1 POP, 2 POP, 3 POP ECT
print("~~~FOOD CITY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Food City
while(Turn<=TurnLimit):
    Turn = Turn + 1
    FoodProductionFOOD=FocusFoodFood*PopulationFOOD
    FoodProductionFOOD=FoodProductionFOOD+2
    ProductionProductionFOOD=FocusFoodProd*PopulationFOOD
    ProductionProductionFOOD=ProductionProductionFOOD+1
    FoodRequirementFOOD=2*PopulationFOOD
    FoodExcessFOOD=FoodProductionFOOD-FoodRequirementFOOD
    FoodBasketFOOD=FoodBasketFOOD+FoodExcessFOOD
    #print("FoodBasketFOOD",FoodBasketFOOD)
    TotalProductionFOOD = TotalProductionFOOD+ProductionProductionFOOD
    if(PopulationFOOD!=30):
        if(FoodBasketFOOD>=FoodGrowth[PopulationFOOD]):
            FoodBasketFOOD=FoodBasketFOOD-FoodGrowth[PopulationFOOD]
            PopulationFOOD=PopulationFOOD+1
            print("FOOD CITY GREW TO",PopulationFOOD,"POP IN",Turn,"TURNS")
    if (FoodBasketFOOD < 0 and PopulationFOOD>1):
        FoodBasketFOOD = 0
        PopulationFOOD = PopulationFOOD - 1
        print("FOOD CITY STARVED TO", PopulationFOOD, "POP IN", Turn, "TURNS")
    TurnArr.append(Turn)
    ProductionArrFOOD.append(TotalProductionFOOD)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

PopulationPROD=1
FoodBasketPROD=0
TotalProductionPROD=0
ProductionArrPROD=[]
print("~~~PRODUCTION CITY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Production City
Turn=0
while(Turn<=TurnLimit):
    Turn = Turn + 1
    FoodProductionPROD=FocusProdFood*PopulationPROD
    FoodProductionPROD=FoodProductionPROD+2
    ProductionProductionPROD=FocusProdProd*PopulationPROD
    ProductionProductionPROD=ProductionProductionPROD+1
    FoodRequirementPROD=2*PopulationPROD
    FoodExcessPROD=FoodProductionPROD-FoodRequirementPROD
    FoodBasketPROD=FoodBasketPROD+FoodExcessPROD
    #print("FoodBasketPROD", FoodBasketPROD)
    TotalProductionPROD = TotalProductionPROD+ProductionProductionPROD
    if(PopulationPROD!=30):
        if(FoodBasketPROD>=FoodGrowth[PopulationPROD]):
            FoodBasketPROD=FoodBasketPROD-FoodGrowth[PopulationPROD]
            PopulationPROD=PopulationPROD+1
            print("PRODUCTION CITY GREW TO", PopulationPROD, "POP IN", Turn, "TURNS")
    if (FoodBasketPROD < 0 and PopulationPROD>1):
        FoodBasketPROD = 0
        PopulationPROD = PopulationPROD - 1
        print("PRODUCTION CITY STARVED TO", PopulationPROD, "POP IN", Turn, "TURNS")
    ProductionArrPROD.append(TotalProductionPROD)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

PopulationEOIN=1
FoodBasketEOIN=0
TotalProductionEOIN=0
ProductionArrEOIN=[]
print("~~~EOIN CITY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Turn=0
while(Turn<=TurnLimit):
    Turn = Turn + 1
    if(PopulationEOIN<4):
        FoodProductionEOIN=FocusFoodFood*PopulationEOIN
        FoodProductionEOIN=FoodProductionEOIN+2
        ProductionProductionEOIN=FocusFoodProd*PopulationEOIN
        ProductionProductionEOIN=ProductionProductionEOIN+1
    elif(PopulationEOIN>=4):
        FoodProductionEOIN = FocusProdFood * PopulationEOIN
        FoodProductionEOIN=FoodProductionEOIN+2
        ProductionProductionEOIN = FocusProdProd * PopulationEOIN+1
        ProductionProductionEOIN=ProductionProductionEOIN+1
    FoodRequirementEOIN=2*PopulationEOIN
    FoodExcessEOIN=FoodProductionEOIN-FoodRequirementEOIN
    FoodBasketEOIN=FoodBasketEOIN+FoodExcessEOIN
    #print("FoodBasketEOIN", FoodBasketEOIN)
    TotalProductionEOIN = TotalProductionEOIN+ProductionProductionEOIN
    if(PopulationEOIN!=30):
        if(FoodBasketEOIN>=FoodGrowth[PopulationEOIN]):
            FoodBasketEOIN=FoodBasketEOIN-FoodGrowth[PopulationEOIN]
            PopulationEOIN=PopulationEOIN+1
            print("EOIN CITY GREW TO", PopulationEOIN, "POP IN", Turn, "TURNS")
    if (FoodBasketEOIN < 0 and PopulationEOIN>1):
        FoodBasketEOIN = 0
        PopulationEOIN = PopulationEOIN - 1
        print("EOIN CITY STARVED TO", PopulationEOIN, "POP IN", Turn, "TURNS")
    ProductionArrEOIN.append(TotalProductionEOIN)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

Population5=1
FoodBasket5=0
TotalProduction5=0
ProductionArr5=[]
print("~~~5 CITY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Turn=0
while(Turn<=TurnLimit):
    Turn = Turn + 1
    if(Population5<5):
        FoodProduction5=FocusFoodFood*Population5
        FoodProduction5=FoodProduction5+2
        ProductionProduction5=FocusFoodProd*Population5
        ProductionProduction5=ProductionProduction5+1
    elif(Population5>=5):
        FoodProduction5 = FocusProdFood * Population5
        FoodProduction5=FoodProduction5+2
        ProductionProduction5 = FocusProdProd * Population5+1
        ProductionProduction5=ProductionProduction5+1
    FoodRequirement5=2*Population5
    FoodExcess5=FoodProduction5-FoodRequirement5
    FoodBasket5=FoodBasket5+FoodExcess5
    #print("FoodBasket5", FoodBasket5)
    TotalProduction5 = TotalProduction5+ProductionProduction5
    if(Population5!=30):
        if(FoodBasket5>=FoodGrowth[Population5]):
            FoodBasket5=FoodBasket5-FoodGrowth[Population5]
            Population5=Population5+1
            print("5 CITY GREW TO", Population5, "POP IN", Turn, "TURNS")
    if (FoodBasket5 < 0 and Population5>1):
        FoodBasket5 = 0
        Population5 = Population5 - 1
        print("5 CITY STARVED TO", Population5, "POP IN", Turn, "TURNS")
    ProductionArr5.append(TotalProduction5)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

PopulationBAL=1
FoodBasketBAL=0
TotalProductionBAL=0
ProductionArrBAL=[]
print("~~~BALANCED CITY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Turn=0
while(Turn<=TurnLimit):
    Turn = Turn + 1
    FoodProductionBAL=BalancedFood*PopulationBAL
    FoodProductionBAL=FoodProductionBAL+2
    ProductionProductionBAL=BalancedProd*PopulationBAL
    ProductionProductionBAL=ProductionProductionBAL+1
    FoodRequirementBAL=2*PopulationBAL
    FoodExcessBAL=FoodProductionBAL-FoodRequirementBAL
    FoodBasketBAL=FoodBasketBAL+FoodExcessBAL
    #print("FoodBasketBAL", FoodBasketBAL)
    TotalProductionBAL = TotalProductionBAL+ProductionProductionBAL
    if(PopulationBAL!=30):
        if(FoodBasketBAL>=FoodGrowth[PopulationBAL]):
            FoodBasketBAL=FoodBasketBAL-FoodGrowth[PopulationBAL]
            PopulationBAL=PopulationBAL+1
            print("BALANCED CITY GREW TO", PopulationBAL, "POP IN", Turn, "TURNS")
    if (FoodBasketBAL < 0 and PopulationBAL>1):
        FoodBasketBAL = 0
        PopulationBAL = PopulationBAL - 1
        print("BALANCED CITY STARVED TO", PopulationBAL, "POP IN", Turn, "TURNS")
    ProductionArrBAL.append(TotalProductionBAL)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# create data
plotstart=0
plotend=Turn
#print("plotstart",plotstart)
#print("plotend",plotend)
x1 = np.arange(plotstart, plotend)#Number of Values
y1 = np.array(ProductionArrFOOD) #Plot Values
x2 = np.arange(plotstart, plotend)#Number of Values
y2 = np.array(ProductionArrPROD) #Plot Values
x3 = np.arange(plotstart, plotend)#Number of Values
y3 = np.array(ProductionArrEOIN) #Plot Values
x4 = np.arange(plotstart, plotend)#Number of Values
y4 = np.array(ProductionArrBAL) #Plot Values
x5 = np.arange(plotstart, plotend)#Number of Values
y5 = np.array(ProductionArr5) #Plot Values

# plotting
plt.title("Food v.s Production Focus")
plt.xlabel("Turns")
plt.ylabel("Total Production")
plt.plot(x1, y1, label = "Food City", color="green")
plt.plot(x2, y2, label = "Production City", color="orange")
plt.plot(x3, y3, label = "Eoin Method City", color="blue")
plt.plot(x4, y4, label = "Balanced City", color="purple")
plt.plot(x5, y5, label = "5 Method City", color="red")
plt.legend()
plt.show()