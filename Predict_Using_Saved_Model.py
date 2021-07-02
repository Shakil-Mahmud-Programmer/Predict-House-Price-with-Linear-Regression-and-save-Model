import pickle as pk
model=pk.load(open('model','rb'))
m1,m2,m3=model.coef_
print("first Coef= ",m1,",second coef=",m2,',third Coef=',m3)
print('intercept= ',model.intercept_)
size=int(input("Size: "))
roof=int(input("Roof: "))
area_rating=int(input("Area Rating: "))
print('Price=',model.predict([[size,roof,area_rating,]]))