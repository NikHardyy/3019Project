import numpy as np
import matplotlib.pyplot as plt
import os
import math


os.chdir("C:/Users/altac/Downloads")

data = np.loadtxt('student_013.txt')


#Part 1

x = data[:, 0]
y = data[:, 1]

plt.plot(x, y,linewidth=0.5, color="red")
plt.xlabel("Time (seconds)") 
plt.ylabel("Relative Brightness")
plt.title("1b) Total Lightcurve for Star 13")
plt.show()


#Part 2

#2c)
x = data[0:97, 0]
y = data[0:97, 1]

plt.plot(x, y, linewidth=0.5, color="red")
plt.xlabel("Time (seconds)")
plt.ylabel("Relative Brightness")
plt.title("2c) First Transit")
plt.show()
#2a)
print("2a) The start and end time of this transit is 0 seconds and around 13000 seconds respectively.")

#2b


#When finding the average I change the bounds of my plot to be only after the planet has fully crossed onto the front of the star.
xa = data[3:93, 0] 
ya = data[3:93, 1]

#Using built in functions
avg = np.average(ya)
std = np.std(ya)
print("2b) Average Brightness during first transit:", avg)
print("2b) Standard Deviation:", std)


#Part 3

#This ommitted code was used to find time between transits. 
#By zooming in on the start of the second transit we are able to see the time it starts on the x axis of the graph.
'''
x1 = data[17420:17470, 0] #Data range for Second Transit
y1 = data[17420:17470, 1]

plt.plot(x1, y1, linewidth=0.5, color="red")
plt.xlabel("Time (seconds)")
plt.ylabel("Relative Brightness")
plt.title("First Transit")
plt.show()
'''

#3a
#To find the orbital period I see the time between the start of the first and second transits. 
print("3a) The Orbital Period of the planet is 2.503e+6 seconds")



#3b) 
#Finding the region on the plot for following transits to overplot transit. 
x1 = data[17430:17520, 0] #Data range for Second Transit
y1 = data[17430:17520, 1]

x2 = data[34856:34950, 0] #Data range for Third Transit
y2 = data[34856:34950, 1]

x3 = data[52284:52376, 0] #Data range for Fourth Transit
y3 = data[52284:52376, 1]

x4 = data[69712:69802, 0] #Data range for Fifth Transit
y4 = data[69712:69802, 1]



#Overplotting all transits to compare on a single graph.
plt.plot(y, linewidth=0.5, color="red")
plt.plot(y1, linewidth=0.5, color="black")
plt.plot(y2, linewidth=0.5, color="blue")
plt.plot(y3, linewidth=0.5, color="orange")
plt.plot(y4, linewidth=0.5, color="green")

positions = (0, 97)
labels = (0, 14000)
plt.xticks(positions, labels)
plt.xlabel("Time (seconds)")
plt.ylabel("Relative Brightness")
plt.title("3b) All five transits, Overplot")
plt.show()

#3c) 
#Finding the average of all transits.
#Take all average transit brightnesses, and average them. 
x1a = data[17430:17520, 0]
y1a = data[17430:17520, 1]

avg1 = np.average(y1a)
std1 = np.std(y1a)

##
x2a = data[34856:34950, 0] #Data range for Third Transit
y2a = data[34856:34950, 1]

avg2 = np.average(y2a)
std2 = np.std(y2a)

##
x3a = data[52284:52376, 0] #Data range for Fourth Transit
y3a = data[52284:52376, 1]

avg3 = np.average(y3a)
std3 = np.std(y3a)

##
x4a = data[69712:69802, 0] #Data range for Fifth Transit
y4a = data[69712:69802, 1]

avg4 = np.average(y4a)
std4 = np.std(y4a)

#Average of all transits
avgAll = (avg + avg1 + avg2 + avg3 + avg4) / 5

#Finding the Uncertainty. (Standard deviation of the mean)
unc1 = (avg - avgAll)**2
unc2 = (avg1 - avgAll)**2
unc3 = (avg2 - avgAll)**2
unc4 = (avg3 - avgAll)**2
unc5 = (avg4 - avgAll)**2

Unc = ((unc1 + unc2 + unc3 + unc4 + unc5) / 5 )**0.5
print("3c) The Uncertainty is", Unc)

print("3c) The average brightness over all 5 transits is", avgAll)

#Using the drop in brightness to calculate the planets radius with Drop = r^2/R^2
R_star = 0.510 #(Solar Radii)
drop = 1 - avgAll
r_planet = (drop*(R_star**2))**0.5

print("3c) The radius of the planet is", r_planet)



