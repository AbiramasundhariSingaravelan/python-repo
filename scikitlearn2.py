from sklearn.linear_model import LinearRegression
import pandas as pd
data = {
    "Hours":[1,2,3,4,5],
    "Marks":[35,45,55,65,75]
}
df=pd.DataFrame(data)
x=df[["Hours"]]
y=df[["Marks"]]
model = LinearRegression()
model.fit(x,y)
prediction = model.predict([[7]])
print(prediction)