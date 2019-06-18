import numpy as np
import random
x=np.arange(6).reshape(3,2)
y=np.arange(10).reshape(2,5)
for i in range(3):
    for j in range(2):
        x[i][j]=random.randint(1,10)
for i in range(2):
    for j in range(5):
        y[i][j]=random.randint(1,20)

print("Saving following data into  the file :")
print(x)
print(y)
#Saving into files
np.savetxt("thtw.csv",x,delimiter=",")
np.savetxt("twfi.csv",y,delimiter=",")


#reading data From Files
data=np.genfromtxt('thtw.csv',delimiter=',')
data1=np.genfromtxt('twfi.csv',delimiter=',')
print("Reading Data from file and Reshape it :")
print(data.reshape(2,3))
print(data1.reshape(5,2))


