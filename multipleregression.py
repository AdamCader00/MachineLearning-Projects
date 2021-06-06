import pandas

from sklearn import linear_model

df = pandas.read_csv("cars.csv")

x = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x,y)

#predict CO2 emissions of a car with weight 2300kg, volume 1300cm^3
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
