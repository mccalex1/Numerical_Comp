import matplotlib.pyplot as plt
import numpy as np

def plotData(country, year, data, title):

    plt.title(country + " " + title + " vs Years")

    plt.plot(year, data, marker='o', linestyle='--', color='b', label=title)
    plt.ylabel(title)
    plt.xlabel("Years")

    plt.show()

    return 0



def linearModel(year, data):
    return 0


#polyfit                                                                                                               
def doFit(x, y, n):
    return np.polyfit(np.array(x), np.array(y), n)




def main():

    country = "USA"
    year = [1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
    other = [3, 6, 7, 10, 16, 18, 23, 30]
    title = "Sea Level"

#    plotData(country, year, other, title)
#    linearModel(year, other)
    





###########################################################################################
    infile = open("avg_global_temp.txt", 'r')

    #reading a line right here skips the first line in the file
    infile.readline()
    year = []
    avg_global_temp = []
    for line in infile:
        line = line.strip().split()
        
        year.append(int(line[0]))
        avg_global_temp.append(float(line[1]))
        
        

    plotData("Temperature change in Degrees Celcius", year, avg_global_temp, "Global Temperature Change")
    infile.close()
###########################################################################################

    infile = open("sea_level.txt", 'r')
    
    #reading a line right here skips the first line in the file
    infile.readline()
    year = []
    sea_level = []
    for line in infile:
        line = line.strip().split()

        year.append(float(line[2]))
        sea_level.append(float(line[5]))

    plotData("Sea Level change in Millimeters", year, sea_level, "Global Sea Level Change")





main()
