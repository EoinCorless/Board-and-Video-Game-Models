#Eoin Corless
#15th/March/2025

##IMPORTS##
import numpy as np
import matplotlib.pyplot as plt

class Crop:
  def __init__(self, name, seedPrice, harvestValue, regrows, growthTime, regrowthTime, colour, results):
    self.name = name #The name of the Crop
    self.seedPrice = seedPrice #The price of planting per crop
    #The money made per harvest (for example, if a potato is worth 25 and you get 2.5 per harvest on average, the harvestValue is 62.5)
    self.harvestValue = harvestValue
    self.regrows = regrows #Boolean, if True the crop regrows (e.g strawberries off a bush), if false it doesn't regrow (e.g potatoes out of the ground)
    self.growthTime = growthTime #The time it takes for a crop to grow after being planted
    self.regrowthTime = regrowthTime #The regrow time after a crop is harvested if it regrows (e.g how long it takes for a strawberry to regrow on the bush)
    self.colour = colour #The colour used to when plotting the graph
    self.results = results #The array where the results are stored

class Settings:
  def __init__(self, startingMoney, daysLimit, startingDay, cropLimit):
    self.startingMoney = startingMoney #The amount of money available at the start of the simulation
    self.daysLimit = daysLimit #How many days you want to simulate
    self.startingDay = startingDay #What day you want the simulation to start on, idk why you'd want anything other then 1 but at least you have the option
    self.cropLimit = cropLimit #How many crops can be planted at once

#Counts the total number of crops planted
def countTotalCrops(array):
    length = len(array)
    i = 0
    totalCrops = 0
    while(i <= length-1):
        totalCrops = totalCrops + array[i]
        i=i+1
    return totalCrops

#Function could be made tidier, clean it up!
#Looking at this a a day later, why didn't I just use a modulus?
def buySeeds(currentMoney, seedPrice, slots, crops):
    money = currentMoney
    availableCropSlots = slots-crops
    seeds = 0
    if(money >= seedPrice):
        while(money >= seedPrice and seeds != availableCropSlots):
            money = money-seedPrice
            seeds = seeds+1
    return seeds

#Simulates the growing season and returns an array of money earned over time
def seasonSimulator(crop, settings):
    ##Values are declared like this as a hold over from a previous version
    ##And because I think it makes the code a bit less messy
    seedPrice = crop.seedPrice
    harvestValue = crop.harvestValue
    regrows = crop.regrows
    growthTime = crop.growthTime
    regrowthTime = crop.regrowthTime
    cropsLim= settings.cropLimit
    currentMoney = settings.startingMoney
    daysLimit = settings.daysLimit
    currentDay = settings.startingDay

    #Perhaps in future I should make batchNumber and batchTimer just 1 2D array?
    batchNumber = [] #Each index is a batch of crops (A Batch being a group of crops all planted at once)
    batchTimer = [] #Each index is how long in days until the crop has grown (Index i of batchNumber corresponds to Index i of batchTimer)

    moneyEarned = 0  # Amount of money earned, NOT just profit
    moneyOverTime = [] #An array of moneyEarned. Each index is one day
    growthTime = growthTime+1 #+1 because displayed grow time doesn't include the first day (e.g day it was planted)
    newSeeds = buySeeds(currentMoney, seedPrice, cropsLim,0) #Buys initial set of seeds
    currentMoney = currentMoney - (seedPrice * newSeeds) #Pays for the Seeds
    batchNumber.append(newSeeds) #Adds new batch to batchNumber
    batchTimer.append(growthTime) #Adds new batch to batchTimer

    ##Loops for all days being simulated
    while(currentDay <= daysLimit):
        totalCrops = countTotalCrops(batchNumber) #Counts total number of planted Crops
        length = len(batchNumber) #Gets the length that the Harvest Loop will loop for
        i = 0

        ## H A R V E S T  L O O P##
        while(i <= length-1):
            batchTimer[i] = batchTimer[i]-1 #A day has passed so the timer goes down by 1
            if(batchTimer[i] == 0): #When == 0, the plant is ready to be harvested and sold
                #Calculates the value of the harvest
                currentMoney = currentMoney+(batchNumber[i]*harvestValue)
                moneyEarned = moneyEarned+(batchNumber[i]*harvestValue)

                if(regrows == True): #Sets regrowth time, like waiting for berries to regrow on a bush
                    batchTimer[i] = regrowthTime
                else: #Removes the crops from the array, like taking carrots out of the ground
                    batchNumber[i] = 0
                    batchTimer[i] = daysLimit*100 #Just set this high so it never hits 0, no kill like overkill!
            i=i+1 #Checks next plant in the batch Array
        moneyOverTime.append(moneyEarned) #Adds the total money made so far since the start to the array, these values are used for the graph
        totalCrops = countTotalCrops(batchNumber) #Recounts the total number of crops, which may have gone down
        #I do realize this number is almost always the same as counted before or 0, but this makes it easier too add additional features in future
        #Such as plants that only regrow a certain number of times

        if(regrows == True):
            newCrops = buySeeds(currentMoney,seedPrice,cropsLim,totalCrops) #Buys a new batch of crops
            currentMoney = currentMoney-(seedPrice*newCrops) #Pays for the crops
            batchNumber.append(newCrops) #Adds new batch
            batchTimer.append(growthTime) #Adds new batch
        else:
            newCrops = buySeeds(currentMoney, seedPrice, cropsLim, totalCrops) #Buys a new batch of crops
            currentMoney = currentMoney - (seedPrice * newCrops) #Pays for the crops
            batchNumber.append(newCrops) #Adds new batch
            batchTimer.append(growthTime) #Adds new batch
            totalCrops = countTotalCrops(batchNumber) #Recounts number of crops, which for none regrowable should just be same as newCrops

        currentDay=currentDay+1#Moves onto the next day
    return moneyOverTime

#####  L  I  S  T    O  F    C  R  O  P  S  #####
## S P R I N G  C R O P S ##
blueJazz = Crop("Blue Jazz", 30, 55, False, 7, 7, "blue", [])
cauliflower = Crop("Cauliflower", 80,175,False,12,12, "green", [])
garlic = Crop("Garlic", 40,60,False,4,4, "tan", [])
greenBean = Crop("Green Bean", 60,40,True,10,3, "lawngreen", [])
kale = Crop("Kale", 70,110,False,6,6, "darkolivegreen", [])
parsnip = Crop("Parsnip", 20,35,False,4,4, "goldenrod", [])
potato = Crop("Potato", 50,100,False,6,6, "saddlebrown", [])
rhubarb = Crop("Rhubarb", 100,220,False,13,13, "firebrick", [])
strawberry = Crop("Strawberry", 100,122,True,8,4, "red", [])
tulip = Crop("Tulip", 20,30,False,6,6, "purple", [])
coffeeBean = Crop("Coffee Bean", 2500,60.3,True,10,2, "pink", [])
riceWithWater = Crop("Rice", 40, 63.3, False, 6, 6, "black", [])
springCrops = [blueJazz, cauliflower, garlic, greenBean, kale, parsnip, potato, rhubarb, strawberry, tulip, coffeeBean, riceWithWater]

## S U M M E R  C R O P S ##
blueberry = Crop("Blueberry", 80,153,True,13,4, "blue", [])
corn = Crop("Corn", 150,50,True,14,4, "goldenrod", [])
hops = Crop("Hops", 60,25,True,11,1, "forestgreen", [])
hotPepper = Crop("Hot Pepper", 40,41.2,True,5,3, "firebrick", [])
melon = Crop("Melon", 40,250,False,12,12, "hotpink", [])
poppy = Crop("Poppy", 100,140,False,7,7, "orange", [])
radish = Crop("Radish", 40,90,False,6,6, "orangered", [])
redCabbage = Crop("Red Cabbage", 100,260,False,9,9, "darkmagenta", [])
starfruit = Crop("Starfruit", 400,750,False,13,13, "gold", [])
summerSpangle = Crop("Summer Spangle", 50,90,False,8,8, "khaki", [])
sunflower = Crop("Sunflower", 125,100,False,13,13, "yellow", [])
tomato = Crop("Tomato", 50,63,True,11,4, "red", [])
wheat = Crop("Wheat", 10,25,False,4,4, "tan", [])
summerCrops = [blueberry, corn, hops, hotPepper, melon, poppy, radish, redCabbage, starfruit, summerSpangle, sunflower, tomato, wheat]

## A U T U M N  C R O P S ##
amaranth = Crop("Amaranth", 70,150,False,7,7, "black", [])
artichoke = Crop("Artichoke", 30,160,False,8,8, "forestgreen", [])
beet = Crop("Beet", 20,100,False,6,6, "firebrick", [])
bokChoy = Crop("Bok Choy", 50,80,False,4,4, "lawngreen", [])
cranberries = Crop("Cranberries", 240,157.5,True,7,5, "red", [])
eggplant = Crop("Eggplant", 20,61.2,True,5,5, "violet", [])
fairyRose = Crop("Fairy Rose", 200,290,False,12,12, "magenta", [])
grape = Crop("Grape", 60,80,True,10,3, "darkmagenta", [])
pumpkin = Crop("Pumpkin", 100,320,False,13,13, "darkorange", [])
yam = Crop("Yam", 60,160,False,10,10, "sienna", [])
autumnCrops = [amaranth, artichoke, beet, bokChoy, cranberries, eggplant, fairyRose, grape, pumpkin, yam]


baseSettings = Settings(2000,28,1, 400) #Sets the base settings for the simulation
xAxis = np.arange(1,baseSettings.daysLimit+1,1) #Sets array for the xAxis of the graph
cropSeasons = [springCrops,summerCrops,autumnCrops] #Saves an array of arrays for all seasons
numberOfSeasons = len(cropSeasons) #Saves the number of crop categories/seasons
currentSeason = 0
while(currentSeason <= numberOfSeasons-1):
    currentCropSet = cropSeasons[currentSeason] #Saves the current crop set
    currentCrop = 0
    numberOfCrops = len(currentCropSet) #Saves the number of different types of crops
    while(currentCrop <= numberOfCrops-1):
        #Runs the simulation
        currentCropSet[currentCrop].results = seasonSimulator(currentCropSet[currentCrop], baseSettings)

        #Graphs the results
        plt.plot(xAxis,currentCropSet[currentCrop].results,label=currentCropSet[currentCrop].name,color=currentCropSet[currentCrop].colour)

        currentCrop = currentCrop+1 #Moves onto the next type of crops
    currentSeason = currentSeason+1 #Moves onto the next season/category of crops
    plt.legend()
    plt.show() #Displays the graph