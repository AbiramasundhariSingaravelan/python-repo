import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    "CGPA":[5,6,7,8,9,8.5,6.5,7.5,9.2,5.8],
    "Aptitude":[40,50,70,80,90,85,60,75,95,45],
    "Communication":[45,55,65,80,90,75,60,70,92,50],
    "Placed":[0,0,1,1,1,1,0,1,1,0]
}

df = pd.DataFrame(data)

# Features
X = df[["CGPA","Aptitude","Communication"]]

# Target
y = df["Placed"]

# Model
model = DecisionTreeClassifier()

# Training
model.fit(X,y)

print("\n===== Placement Prediction System =====\n")

cgpa = float(input("Enter CGPA: "))
aptitude = int(input("Enter Aptitude Score: "))
communication = int(input("Enter Communication Score: "))

result = model.predict(
    [[cgpa, aptitude, communication]]
)

if result[0] == 1:
    print("\nPrediction: Likely to be Placed")
else:
    print("\nPrediction: Placement Needs Improvement")

print("\nRecommendations:")

if aptitude < 60:
    print("- Improve Aptitude Skills")

if communication < 60:
    print("- Improve Communication Skills")

if cgpa < 7:
    print("- Improve Academic Performance")