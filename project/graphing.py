import matplotlib.pyplot as plt
import numpy as np
import time
import sys

colors = ["green", "brown", "silver", "red", "orange", "yellow", "black", "blue", "cyan", "indigo", "violet"]
count = 0



#simple function takes in title, x and y data
def plotData(dataName, x, y):
    global count
    
    plt.plot(x, y, marker='o', color=colors[count], linestyle='--', label = dataName)


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python graphing.py <Year>")
        return 1

    year = int(sys.argv[1])

    start_time = time.time()

    #plot individual graphs
    plotAvgGlobalTemp()
    SeaLevel = plotSeaLevel(year)
    plotGlobalCo2()

    #plot country co2 data
    plotCo2Data()

    #plot correlational graphs
    plotTempCo2()
    plotTempSea()
    
    print("\nThe Projected Sea Level in", year, "is", SeaLevel)
    print("--- %s seconds ---" % (time.time() - start_time))


#Reads in from file
#pulls out all temperature and co2 data
#plots the data co2 on x, temperature on y
def plotTempCo2():

    infile = open("allData.txt", 'r')
    infile.readline()

    co2s = []
    temps = []

    #reads through file
    for line in infile:
        year, co2, temp, sea = line.strip().split()

        co2s.append(float(co2))
        temps.append(float(temp))
            

    ####polyfit co2 and temp###                                                   
    x = np.array(co2s)
    y = np.array(temps)
    z, res, _, _, _ = np.polyfit(x, y, 1, full=True)
    _, res2, _, _, _ = np.polyfit(x, y, 2, full=True)

    p = np.poly1d(z)
    
    xp = np.linspace(300, 425, 100)

    plt.plot(xp, p(xp), '-', label="Best Fit")

    #statistical stuff                                               
    equation = 'y = ' + str(round(z[0],4)) + 'x' ' + ' + str(round(z[1],4))

    #print to terminal
    print("CO2 vs Temp")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))
    print("Error=", res)
    print("Error with 2 degree=", res2)
    print()

    #set up graph labels
    plt.title("CO2 VS Temperature")
    plt.xlabel("CO2 (PPM)")
    plt.ylabel("Temperature (C)")
    plt.scatter(co2s, temps, label="CO2 VS Temp")
    

    #add line of best fit to graph
    plt.annotate(equation, xy=(362,.391), xytext=(300,1),
                 arrowprops=dict(facecolor='black', shrink=0.01))


    plt.legend()
    plt.show()


#Reads in from file
#pulls out all temperature and sea data
#plots the temperature on x, sea on y
def plotTempSea():

    infile = open("allData.txt", 'r')
    infile.readline()

    temps = []
    seas = []

    for line in infile:
        year, co2, temp, sea = line.strip().split()

        if(int(year) >= 1993):
            temps.append(float(temp))
            seas.append(float(sea))
        

    ####polyfit sea and temp###
    x = np.array(temps)
    y = np.array(seas)

    z, res, _, _, _ = np.polyfit(x, y, 1, full=True)
    _, res2, _, _, _ = np.polyfit(x, y, 2, full=True)

    p = np.poly1d(z)

    xp = np.linspace(.2, 1, 100)

    plt.plot(xp, p(xp), '-', label="Best Fit")

    #statistical stuff
    equation = 'y = ' + str(round(z[0],4)) + 'x' ' + ' + str(round(z[1],4))

    #print to terminal
    print("Sea vs Temp")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))
    print("Error=",res)
    print("Error with 2 degree=", res2)
    print()
    
    #set up graph labels
    plt.title("Sea Level VS Temperature")
    plt.xlabel("Temperature (C)")
    plt.ylabel("Sea Level (mm)")
    plt.scatter(temps, seas, label="Sea VS Temp")

    #add line of best fit to graph
    plt.annotate(equation, xy=(.57, 22.7), xytext=(.2, 60),
                 arrowprops=dict(facecolor='black', shrink=0.01))


    plt.legend()
    plt.show()


#reads in from file and takes out all the temperatures and corresponding years
#then plots data using pyplot in a graph
def plotAvgGlobalTemp():    

    infile = open("avg_global_temp.txt", 'r')

    #reading a line right here skips the first line in the file
    infile.readline()
    year = []
    avg_global_temp = []
    for line in infile:
        line = line.strip().split()
        
        year.append(int(line[0]))
        avg_global_temp.append(float(line[1]))
        
        

    plotData("Temperature", year, avg_global_temp)
    infile.close()


    ####polyfit###
    x = np.array(year)
    y = np.array(avg_global_temp)

    _, res, _, _, _ = np.polyfit(x, y, 1, full=True)
    z, res2, _, _, _ = np.polyfit(x, y, 2, full=True)

    p = np.poly1d(z)

    xp = np.linspace(1880, 2050, 100)
    
    plt.plot(xp, p(xp), '-', label="Best Fit")    

    #statistical stuff
    theMean = [np.mean(y) for i in x]
    stdDev = [np.std(y) for i in x]
    theVar = [np.var(y) for i in x]


    equation = 'y = ' + str(round(z[0],7)) + 'x^2' ' + ' + str(round(z[1],4)) + 'x' + ' + ' + str(round(z[2],4))

    #prints to terminal
    print("Global Temperature")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))
    print("Error=", res)
    print("Error with 2 degree=",res2)
    print()

    
    #sets up x y axis labels
    plt.ylabel("Temperature Change (C)")
    plt.xlabel("Years")

    #puts line of best fit equation on graph
    plt.annotate(equation, xy=(1945,-.143), xytext=(1900,1),
                 arrowprops=dict(facecolor='black', shrink=0.01))

    plt.title("Global Temperature in Degrees Celcius From 1880")

    plt.legend()

    plt.show()
    



#takes sea level and corresponding year
#outputs graph using pyplot
def plotSeaLevel(yearChosen):

    infile = open("sea_level.txt", 'r')
    
    #reading a line right here skips the first line in the file
    infile.readline()
    year = []
    sea_level = []
    for line in infile:
        line = line.strip().split()

        year.append(float(line[2]))
        sea_level.append(float(line[5]))

    plotData("Sea Level", year, sea_level)
    infile.close()

    ####polyfit###                                                                
    x = np.array(year)
    y = np.array(sea_level)

    z, res, _, _, _ = np.polyfit(x, y, 1, full=True)
    _, res2, _, _, _ = np.polyfit(x, y, 2, full=True)

    p = np.poly1d(z)

    xp = np.linspace(1992, 2050, 100)

    plt.plot(xp, p(xp), '-', label="Best Fit")

    #statistical stuff
    equation = 'y = ' + str(round(z[0],4)) + 'x' ' + ' + str(round(z[1],4))

    #prints to terminal
    print("Sea Level")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))
    print("Error=",res)
    print("Error with 2=", res2)
    print()

    
    #sets up x y axis labels
    plt.ylabel("Sea Level Change (mm)")
    plt.xlabel("Years")


    #puts line of best fit on graph
    plt.annotate(equation, xy=(2020,70.44), xytext=(2030,30),
                 arrowprops=dict(facecolor='black', shrink=0.01))


    plt.title("Global Sea Level change in Millimeters")

    plt.legend()

    plt.show()


    return float(z[0]) * float(yearChosen) + float(z[1])


#takes co2 and corresponding years
#outputs graph using pyplot
def plotGlobalCo2():

    infile = open("global_co2.txt", 'r')

    #reading a line right here skips the first line in the file
    infile.readline()
    year = []
    co2_level = []

    count = 1
    
    #since theres so much data we only want 1 in 6 lines
    limitCount = [2, 3, 4, 5, 6]

    for line in infile:
        if (count in limitCount):
            infile.readline()

        else:
            line = line.strip().split()

            year.append(float(line[2]))
            co2_level.append(float(line[3]))


        count += 1

        if(count == limitCount[-1] + 1):
            count = 1


    plotData("CO2 Level", year, co2_level)
    infile.close()

    ####polyfit###                                                                
    x = np.array(year)
    y = np.array(co2_level)

    z, res, _, _, _ = np.polyfit(x, y, 1, full=True)
    _, res2, _, _, _ = np.polyfit(x, y, 2, full=True)

    p = np.poly1d(z)

    xp = np.linspace(1958, 2050, 100)

    plt.plot(xp, p(xp), '-', label="Best Fit")

    #statistical stuff
    equation = 'y = ' + str(round(z[0],4)) + 'x' ' + ' + str(round(z[1],4))

    #outputs to terminal
    print("CO2")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))
    print("Line of Best Fit= " + equation)
    print("Error=",res)
    print("Error with 2=",res2)
    print()


    #sets up x y axis labels
    plt.ylabel("CO2 (PPM)")
    plt.xlabel("Years")

    plt.title("Global CO2 Level in PPM From " + str(int(year[0])))

    #puts line of best fit in graph
    plt.annotate(equation, xy=(1993,360), xytext=(1960,420),
                 arrowprops=dict(facecolor='black', shrink=0.01))
    
    plt.legend()

    plt.show()
    



#takes co2 data from countries
#outputs to graph
def plotCo2Data():

    global count

    infile = open("CO2Data.txt", 'r')
    
    #reading a line right here skips the first line in the file
    infile.readline()
    year = []
    co2_level = []
    country = ""

    for line in infile:
        line = line.strip().split()

        currentCountry = line[0]

        #checks if it's a new country so I can create a new graph
        if currentCountry != country:
            if country != "":
                plotData(country, year, co2_level)        
                count += 1
            country = currentCountry
            year = []
            co2_level = []

        year.append(int(line[2]))
        co2_level.append(float(line[3]))
        
    plotData(country, year, co2_level)

    plt.xlim(1992, 2020)
    plt.ylim(0, 22)

    #set up x y axis labels
    plt.ylabel("CO2 Change (PPM)")
    plt.xlabel("Years")

    plt.title("C02 Change in PPM Across Countries")
    plt.legend()

    plt.show()

main()
