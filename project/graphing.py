import matplotlib.pyplot as plt
import numpy as np
colors = ["green", "brown", "silver", "red", "orange", "yellow", "black", "blue", "cyan", "indigo", "violet"]
count = 0

def plotData(dataName, year, data):
    global count

    
    plt.plot(year, data, marker='o', color=colors[count], linestyle='--', label = dataName)#"C02 Level Changes")#, color='b', label=title)

    return 0




def main():

    plotAvgGlobalTemp()
    plotSeaLevel()
    plotGlobalCo2()
    plotCo2Data()

    plotTempCo2()

    plotTempSea()

def plotTempCo2():

    infile = open("allData.txt", 'r')
    infile.readline()

    years = []
    co2s = []
    temps = []
    seas = []

    for line in infile:
        year, co2, temp, sea = line.strip().split()

        years.append(int(year))
        co2s.append(float(co2))
        temps.append(float(temp))
            

    ####polyfit co2 and temp###                                                   
    x = np.array(co2s)
    y = np.array(temps)
    z = np.polyfit(x, y, 1)

    p = np.poly1d(z)

    xp = np.linspace(300, 425, 100)

    plt.plot(xp, p(xp), '-', label="Best Fit")

    #statistical stuff                                               
    equation = 'y = ' + str(round(z[0],4)) + 'x' ' + ' + str(round(z[1],4))

    print("CO2 vs Temp")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))
    print()

    plt.title("CO2 VS Temperature")
    plt.xlabel("CO2 (PPM)")
    plt.ylabel("Temperature (C)")
    plt.scatter(co2s, temps, label="CO2 VS Temp")
    
    plt.annotate(equation, xy=(362,.391), xytext=(300,1),
                 arrowprops=dict(facecolor='black', shrink=0.01))


    plt.legend()
    plt.show()

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

    z = np.polyfit(x, y, 1)

    p = np.poly1d(z)

    xp = np.linspace(.2, 1, 100)

    plt.plot(xp, p(xp), '-', label="Best Fit")

    #statistical stuff
    equation = 'y = ' + str(round(z[0],4)) + 'x' ' + ' + str(round(z[1],4))

    print("Sea vs Temp")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))

    plt.title("Sea Level VS Temperature")
    plt.xlabel("Temperature (C)")
    plt.ylabel("Sea Level (mm)")
    plt.scatter(temps, seas, label="Sea VS Temp")

    plt.annotate(equation, xy=(.57, 22.7), xytext=(.2, 60),
                 arrowprops=dict(facecolor='black', shrink=0.01))


    plt.legend()
    plt.show()


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
        
        

    plotData("Temperature change in Degrees Celcius", year, avg_global_temp)
    infile.close()


    ####polyfit###
    x = np.array(year)
    y = np.array(avg_global_temp)
    z = np.polyfit(x, y, 2)

    p = np.poly1d(z)

    xp = np.linspace(1880, 2050, 100)
    
    plt.plot(xp, p(xp), '-', label="Best Fit")    

    #statistical stuff
    theMean = [np.mean(y) for i in x]
    stdDev = [np.std(y) for i in x]
    theVar = [np.var(y) for i in x]

    #plt.plot(year, theMean, label="Mean", color="red") 
    #plt.plot(year, stdDev, label="Std Dev", color="gold") 
    #plt.plot(year, theVar, label="Var", color="magenta") 
    equation = 'y = ' + str(round(z[0],4)) + 'x^2' ' + ' + str(round(z[1],4)) + 'x' + ' + ' + str(round(z[2],4))
    
    print("Global Temperature")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))
    print()
    ###
    
    plt.ylabel("Temperature Change (C)")
    plt.xlabel("Years")

    plt.annotate(equation, xy=(1945,-.143), xytext=(1900,1),
                 arrowprops=dict(facecolor='black', shrink=0.01))

    plt.title("Global Temperature in Degrees Celcius From 1880")

    plt.legend()

    plt.show()





def plotSeaLevel():

    infile = open("sea_level.txt", 'r')
    
    #reading a line right here skips the first line in the file
    infile.readline()
    year = []
    sea_level = []
    for line in infile:
        line = line.strip().split()

        year.append(float(line[2]))
        sea_level.append(float(line[5]))

    plotData("Sea Level change in Millimeters", year, sea_level)
    infile.close()

    ####polyfit###                                                                
    x = np.array(year)
    y = np.array(sea_level)
    z = np.polyfit(x, y, 1)

    p = np.poly1d(z)

    xp = np.linspace(1992, 2050, 100)

    plt.plot(xp, p(xp), '-', label="Best Fit")

    #statistical stuff
    equation = 'y = ' + str(round(z[0],4)) + 'x' ' + ' + str(round(z[1],4))

    print("Sea Level")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))
    print()

    ### 

    plt.ylabel("Sea Level Change (mm)")
    plt.xlabel("Years")

    plt.annotate(equation, xy=(2020,70.44), xytext=(2030,30),
                 arrowprops=dict(facecolor='black', shrink=0.01))

    plt.title("Global Sea Level change in Millimeters")

    plt.legend()

    plt.show()





def plotGlobalCo2():

    infile = open("global_co2.txt", 'r')

    #reading a line right here skips the first line in the file
    infile.readline()
    year = []
    co2_level = []

    count = 1
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

    plotData("CO2 Level change in PPM", year, co2_level)
    infile.close()

    ####polyfit###                                                                
    x = np.array(year)
    y = np.array(co2_level)
    z = np.polyfit(x, y, 1)

    p = np.poly1d(z)

    xp = np.linspace(1958, 2050, 100)

    plt.plot(xp, p(xp), '-', label="Best Fit")

    #statistical stuff
    equation = 'y = ' + str(round(z[0],4)) + 'x' ' + ' + str(round(z[1],4))

    print("CO2")
    print("Mean =", np.mean(y))
    print("Standard Deviation =", np.std(y))
    print("Variance =", np.var(y))
    print("Line of Best Fit= " + equation)
    print()

    ### 

    plt.ylabel("CO2 (PPM)")
    plt.xlabel("Years")

    plt.title("Global CO2 Level in PPM From " + str(int(year[0])))

    plt.annotate(equation, xy=(1993,360), xytext=(1960,420),
                 arrowprops=dict(facecolor='black', shrink=0.01))
    
    plt.legend()

    plt.show()





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

    plt.ylabel("CO2 Change (PPM)")
    plt.xlabel("Years")

    plt.title("C02 Change in PPM Across Countries")
    plt.legend()

    plt.show()

main()
