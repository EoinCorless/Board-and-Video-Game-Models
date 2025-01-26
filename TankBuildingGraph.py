##This is a model that shows the different productions rates of different tanks over time in the game Hearts of Iron 4
#Eoin Corless

import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt
DaysInput=input("How many days?:")
DaysInput=int(DaysInput)

factories=input("How many factories?:")
factories=int(factories)

BaseOut=4.5*factories
FacOutMod=0#DecimalPercentage
ProdEff=0.25#DecimalPercentage
ProdEffCap=0.5#DecimalPercentage
FacOut=BaseOut*(1+FacOutMod)*ProdEff
ProdEffGrowth=0.001*((ProdEffCap**2)/ProdEff)

ProductionCost=10
TankTotal1=[0]
print("--->MsT-40<----------------------------------------------------")
#Tank 1
TankID=1
TankTotal1=[]
EndEff=0.1
TankCost1=6.97
Day=0
TankStockpile1=0
#Tank1
while(Day<=DaysInput):
    Day=Day+1

    FacOut=BaseOut*(1+FacOutMod)*EndEff
    TanksMade1=FacOut/TankCost1
    TankStockpile1=TankStockpile1+TanksMade1
    TankTotal1.append(TankStockpile1)

    if(EndEff<ProdEffCap):
        StartEff=EndEff
        EndEff = ((1/ 500) + StartEff ** 2) ** 0.5
        if(EndEff>=ProdEffCap):
            EndEff = ProdEffCap

    #print(TanksMade1, "built")
    #print("Factory Output",FacOut)
    #print("Production Efficency",EndEff)
print(TankStockpile1,"total MsT-40s Tanks built")
#print(TankTotal1)

print("--->Sherman----------------------------------------------------")
#Tank 2
TankID=2
TankTotal2=[]
EndEff=0.1
TankCost2=14.00
Day=0
TankStockpile2=0
while(Day<=DaysInput):
    Day=Day+1

    FacOut=BaseOut*(1+FacOutMod)*EndEff
    TanksMade2=FacOut/TankCost2
    TankStockpile2=TankStockpile2+TanksMade2
    TankTotal2.append(TankStockpile2)

    if(EndEff<ProdEffCap):
        StartEff=EndEff
        EndEff = ((1/ 500) + StartEff ** 2) ** 0.5
        if(EndEff>=ProdEffCap):
            EndEff = ProdEffCap

    #print(TanksMade2, "built")
    #print("Factory Output",FacOut)
    #print("Production Efficency",EndEff)
print(TankStockpile2,"total Shermans built")
#print(TankTotal2)

print("--->T-34<----------------------------------------------------")
#Tank 3
TankID=3
TankTotal3=[]
EndEff=0.1
TankCost3=18.15
Day=0
TankStockpile3=0
while(Day<=DaysInput):
    Day=Day+1

    FacOut=BaseOut*(1+FacOutMod)*EndEff
    TanksMade3=FacOut/TankCost3
    TankStockpile3=TankStockpile3+TanksMade3
    TankTotal3.append(TankStockpile3)

    if(EndEff<ProdEffCap):
        StartEff=EndEff
        EndEff = ((1/ 500) + StartEff ** 2) ** 0.5
        if(EndEff>=ProdEffCap):
            EndEff = ProdEffCap

    #print(TanksMade3, "built")
    #print("Factory Output",FacOut)
    #print("Production Efficency",EndEff)
print(TankStockpile3,"total T-34s built")

print("--->Panzer IV<----------------------------------------------------")
#Tank 4
TankID=4
TankTotal4=[]
EndEff=0.1
TankCost4=13.5
Day=0
TankStockpile4=0
#Tank4
while(Day<=DaysInput):
    Day=Day+1

    FacOut=BaseOut*(1+FacOutMod)*EndEff
    TanksMade4=FacOut/TankCost4
    TankStockpile4=TankStockpile4+TanksMade4
    TankTotal4.append(TankStockpile4)

    if(EndEff<ProdEffCap):
        StartEff=EndEff
        EndEff = ((1/ 500) + StartEff ** 2) ** 0.5
        if(EndEff>=ProdEffCap):
            EndEff = ProdEffCap

    #print(TanksMade4, "built")
    #print("Factory Output",FacOut)
    #print("Production Efficency",EndEff)
print(TankStockpile4,"total Panzer IVs built")

print("--->Cromwell<----------------------------------------------------")
#Tank 5
TankID=5
TankTotal5=[]
EndEff=0.1
TankCost5=17.5
Day=0
TankStockpile5=0
while(Day<=DaysInput):
    Day=Day+1

    FacOut=BaseOut*(1+FacOutMod)*EndEff
    TanksMade5=FacOut/TankCost5
    TankStockpile5=TankStockpile5+TanksMade5
    TankTotal5.append(TankStockpile5)

    if(EndEff<ProdEffCap):
        StartEff=EndEff
        EndEff = ((1/ 500) + StartEff ** 2) ** 0.5
        if(EndEff>=ProdEffCap):
            EndEff = ProdEffCap

    #print(TanksMade3, "built")
    #print("Factory Output",FacOut)
    #print("Production Efficency",EndEff)
print(TankStockpile5,"total Cromwells built")

print("--->MsT-40UA<----------------------------------------------------")
#Tank 6
TankID=6
TankTotal6=[]
EndEff=0.1
TankCost6=10.2
Day=0
TankStockpile6=0
while(Day<=DaysInput):
    Day=Day+1

    FacOut=BaseOut*(1+FacOutMod)*EndEff
    TanksMade6=FacOut/TankCost6
    TankStockpile6=TankStockpile6+TanksMade6
    TankTotal6.append(TankStockpile6)

    if(EndEff<ProdEffCap):
        StartEff=EndEff
        EndEff = ((1/ 500) + StartEff ** 2) ** 0.5
        if(EndEff>=ProdEffCap):
            EndEff = ProdEffCap

    #print(TanksMade3, "built")
    #print("Factory Output",FacOut)
    #print("Production Efficency",EndEff)
print(TankStockpile6,"total MsT-40UA built")

#print(TankTotal4)
#print("Day",Day)
plotstart=0
plotend=Day
#print("plotstart",plotstart)
#print("plotend",plotend)
x1 = np.arange(plotstart, plotend)#Number of Values
y1 = np.array(TankTotal1) #Plot Values
x2 = np.arange(plotstart, plotend)#Number of Values
y2 = np.array(TankTotal2) #Plot Values
x3 = np.arange(plotstart, plotend)#Number of Values
y3 = np.array(TankTotal3) #Plot Values
x4 = np.arange(plotstart, plotend)#Number of Values
y4 = np.array(TankTotal4) #Plot Values
x5 = np.arange(plotstart, plotend)#Number of Values
y5 = np.array(TankTotal5) #Plot Values
x6 = np.arange(plotstart, plotend)#Number of Values
y6 = np.array(TankTotal6) #Plot Values

# plotting
plt.title("Tank Production")
plt.xlabel("Days")
plt.ylabel("Total Tanks")
plt.plot(x1, y1, label = "MsT-40", color="orange")
plt.plot(x2, y2, label = "Sherman", color="blue")
plt.plot(x3, y3, label = "T-34", color="red")
plt.plot(x4, y4, label = "Panzer IV", color="black")
plt.plot(x5, y5, label = "Cromwell", color="pink")
plt.plot(x6, y6, label = "MsT-40UA", color="green")
plt.legend()
plt.show()
'''
'''