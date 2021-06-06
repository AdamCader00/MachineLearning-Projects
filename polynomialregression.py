import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22] #x values
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100] # y values

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3)) #x, y and 3rd degree polynomial

#r^2 value of fit
print(r2_score(y, mymodel(x)))

#prediction of speed of a car passing at 17 P.M
speed = mymodel(17)
print(speed)

myline = numpy.linspace(1, 22, 50)

plt.scatter(x,y) # scatter plot
plt.plot(myline, mymodel(myline))
plt.show()


