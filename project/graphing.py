import matplotlib.pyplot as plt
import numpy as np
colors = ["green", "brown", "silver", "red", "orange", "yellow", "black", "blue", "cyan", "indigo", "violet"]
count = 0

def plotData(dataName, year, data):
    global count

    
    plt.plot(year, data, marker='o', color=colors[count], linestyle='--', label = dataName)#"C02 Level Changes")#, color='b', label=title)

    return 0



def linearModel(year, data):
    return 0




def main():

    plotAvgGlobalTemp()
    plotSeaLevel()
    plotGlobalCo2()
    plotCo2Data()

    



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
    z = np.polyfit(x, y, 1)

    p = np.poly1d(z)

    xp = np.linspace(1992, 2032, 100)
    
    plt.plot(xp, p(xp), '-')    
    ###
    
    plt.ylabel("Temperature Change (C) From " + str(int(year[0])))
    plt.xlabel("Years")

    plt.title("Global Temperature in Degrees Celcius")

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

    xp = np.linspace(1992, 2032, 100)

    plt.plot(xp, p(xp), '-')
    ### 

    plt.ylabel("Sea Level Change (mm) From " + str(int(year[0])))
    plt.xlabel("Years")

    plt.title("Global Sea Level change in Millimeters")

    plt.legend()

    plt.show()





def plotGlobalCo2():

    infile = open("global_co2.txt", 'r')

    #reading a line right here skips the first line in the file
    infile.readline()
    year = []
    co2_level = []
    for line in infile:
        line = line.strip().split()

        year.append(float(line[2]))
        co2_level.append(float(line[3]))

    plotData("CO2 Level change in PPM", year, co2_level)
    infile.close()

    ####polyfit###                                                                
    x = np.array(year)
    y = np.array(co2_level)
    z = np.polyfit(x, y, 1)

    p = np.poly1d(z)

    xp = np.linspace(1992, 2032, 100)

    plt.plot(xp, p(xp), '-')
    ### 

    plt.ylabel("CO2 PPM From " + str(int(year[0])))
    plt.xlabel("Years")

    plt.title("Global CO2 Level in PPM From " + str(int(year[0])))
    
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

    plt.ylabel("CO2 Change in PPM")
    plt.xlabel("Years")

    plt.title("C02 Change in PPM Across Countries")
    plt.legend()

    plt.show()

main()
