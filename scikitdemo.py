from sklearn.tree import DecisionTreeClassifier
import numpy as np
cgpa = np.array([[5],[6],[7],[8],[9]])
placement = np.array([0,0,1,1,1,])
model=DecisionTreeClassifier()
model.fit(cgpa,placement)
result=model.predict([[2.5]])
if result[0] == 1:
    print("Eligible")
else:
    print("Not Eligible")
