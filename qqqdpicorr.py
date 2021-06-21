import pandas
import numpy as np
import pylab
import math
import numpy
from scipy import stats
from datetime import datetime




df = pandas.read_csv("qqqdata.csv")
df2 = pandas.read_csv("dpidata.csv")

x = df['Close']
y = df2['price']

new_y = []
for data in y:
    new_y.append(math.log(data))
    
    
    

d = df['Date']

date = []
rsq = []

for i in range (1, len(df)+1):
    slope, intercept, r, p, std_err = stats.linregress(x[1:i+1], new_y[1:i+1])
    rsq.append(r)
    date.append(d[i-1])


pylab.xticks(np.arange(0, 300, step=25))
pylab.plot(date, rsq)
pylab.xlabel("Date")
pylab.ylabel("R^2 Value QQQ VS DPI")
pylab.show()
