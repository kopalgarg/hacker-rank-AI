import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
students=[[15,10],[12,25],[8,17],[8,11],[7,13],[7,17],[7,20],[6,13],[5,9],[3,15]]
data=pd.DataFrame(students)
x=data.iloc[:,0].values.reshape(-1,1)
y=data.iloc[:,1].values.reshape(-1,1)

z=np.array(10).reshape(-1,1)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x,y)

print(lr.coef_)