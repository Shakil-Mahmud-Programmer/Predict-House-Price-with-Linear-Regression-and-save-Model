import sklearn.linear_model as lm
import pandas as pd
import pickle as pk
import matplotlib.pyplot as plt
df=pd.read_csv('price.csv')
df=df.head(11)
X=df.drop(columns=['price'])
Y=df['price']
model=lm.LinearRegression()
model.fit(X,Y)
pk.dump(model,open('model','wb'))
print("Coef= ",model.coef_)
print('intercept= ',model.intercept_)
size=int(input("Size: "))
roof=int(input("Roof: "))
area_rating=int(input("Area Rating: "))
print('Price=',model.predict([[size,roof,area_rating,]]))
plt.plot(df['size'],df['price'])
plt.show()