import pandas as pd 
import matplotlib.pyplot as plt 

data=pd.read_csv('/home/suraj/Downloads/bank.csv')
Total_score=data.CreditScore.mean()
total_Salary_estimated=data.EstimatedSalary.mean()
total_Balance=data.Balance.mean()
gender=data.Gender 
Females=0
for i in gender:
    if i=='Female':
        Females=Females+1
Males=10000-Females
No_of_peoples_has_a_card=data.HasCrCard.sum()
graph=[Total_score,total_Balance,total_Salary_estimated,Females,Males,No_of_peoples_has_a_card]
label=["Total_Score","Total_Balance","EstimatedSalary","Females","Males","HasAcard"]
colors=["Green","Blue","Red","Pink","Black","Brown"]
t=plt.bar(label,graph,color=colors)
plt.title("Bank Records")
plt.xticks(rotation=10)
plt.show()