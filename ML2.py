import numpy as np
import random
arr=np.arange(16).reshape(8,2)
for i in range(8):
    for j in range(1):
        arr[i][j]=random.randrange(100,200,5)
        t=1
        while arr[i][j]-arr[i][t]!=5:
            arr[i][t]=random.randrange(100,200,5)  
print(arr)                      
        