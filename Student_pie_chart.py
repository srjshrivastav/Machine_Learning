import pandas as pd
import matplotlib.pyplot as plt 
def show():
    plt.legend()
    plt.show()

#Chart showing ages
data=pd.read_csv('student.csv')
plt.pie(data.age,labels=data.student_name,shadow=True)
show()

#Chart showing Marks
plt.pie(data.Marks,labels=data.student_name,shadow=True)
show()

#Chart for Showing Study Hours

plt.pie(data.study_hours,labels=data.student_name,shadow=True,autopct='%1.1f%%')
show()

