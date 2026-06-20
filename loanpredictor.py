import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# Step 1: DataSet Creation
data ={
    "Income" : [20000,25000,30000,35000,40000,45000,50000,55000,60000,65000],
    "CreditScore" :[500,550,600,620,650, 700, 720,750,780,800],
    "LoanAmount":[500000,450000,400000,350000,300000,250000,200000,150000,100000,50000],
    "Approved":[0,0,0,0,1,1,1,1,1,1]
}
df=pd.DataFrame(data)
#Step 2: Identifying Features & Targets
#Features
X = df[["Income","CreditScore","LoanAmount"]]
#Target
Y=df[["Approved"]]
#Step 3: Creating Model
model=DecisionTreeClassifier()
#Step 4: Train Model
model.fit(X,Y)
print("\n==========Loan Prediction System===================")
income=int(input("Enter Monthly income"))
credit=int(input("Enter your Credit Score"))
loan=int(input("Enter the loan amount"))
result=model.predict([[income,credit,loan]])
print("\n===============RESULT================")
if result[0]==1 :
    print("Loan Approved")
else:
    print("Loan Rejected")
print("\n=========SUGESSTIONS===============")
if credit< 650:
    print("improve credit Score")
if income < 40000:
    print("improve income")
if loan >500000:
    print("try for lower amount")