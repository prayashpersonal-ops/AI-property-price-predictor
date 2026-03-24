import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


# model start

data = {
    "area": [600, 750, 900, 1100, 1300, 700, 850, 1000, 1200, 1500,
                  800, 1000, 1200, 1500, 1800, 900, 1100, 1400, 1700, 2000,
                  850, 1100, 1400, 1600, 1900, 600, 800, 1100, 1400, 1700],

    "bedrooms": [1, 2, 2, 3, 3, 2, 2, 3, 3, 4,
                 2, 2, 3, 3, 4, 2, 3, 3, 4, 4,
                 2, 3, 3, 4, 4, 1, 2, 3, 3, 4],

    "bathrooms": [1, 1, 2, 2, 2, 1, 2, 2, 2, 3,
                  2, 2, 2, 3, 3, 2, 2, 3, 3, 4,
                  2, 2, 3, 3, 4, 1, 2, 2, 3, 3],

    "age": [10, 8, 5, 4, 3, 9, 6, 5, 4, 2,
            7, 5, 3, 2, 1, 6, 4, 3, 2, 1,
            8, 5, 3, 2, 1, 12, 8, 5, 3, 2],

    "price": [18, 24, 30, 38, 45, 22, 28, 35, 42, 55,
                    32, 40, 50, 65, 80, 45, 60, 75, 95, 120,
                    30, 42, 55, 70, 90, 25, 38, 55, 72, 90]
}

df=pd.DataFrame(data)

x = df[["area", "bedrooms", "bathrooms", "age"]]
y = df["price"]

model=LinearRegression()
model.fit(x,y)

# model end


# a=int(input("enter area in sqft:"))
# b=int(input("enter your no. of bedrooms:"))
# c=int(input("enter your no. of bathrooms:"))
# d=int(input("enter age in years:"))
# predicted_price=model.predict([[a,b,c,d]])
# print("price:", predicted_price[0], "lakhs")

with open("model.pkl","wb") as f:
    pickle.dump(model,f)