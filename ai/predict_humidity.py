import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from sympy import Line

def predicthumidity(startDate, endDate, knownTimestamps, humidity, timestamps):

    x = [int(abs((datetime.datetime.utcfromtimestamp(0) - datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")).total_seconds())) for item in knownTimestamps]
    y = humidity

    lm = LinearRegression()

    lm.fit(np.array(x).reshape(-1,1))

    z = [int(abs((datetime.datetime.utcfromtimestamp(0) - datetime.datetime.strptime(item,"%Y-%m-%d %H:%M")).total_seconds())) for item in timestamps]

    return lm.predict(np.array(z).reshape(-1,1))

def predictTemperature(startDate, endDate, temperature, n):
    p = int(len(temperature)/24)
    x = []
    for i in range(1,((24*p)+1)):
        x.append(i)
    y = temperature
    lm = LinearRegression()
    lm.fit(np.asarray(x).reshape(-1,1),y)
    
    f = x[-1]+1
    z = []
    for i in range(24*n):
        z.append(f)
        f += 1
    return(lm.predict(np.asarray(z).reshape(-1,1)).tolist())
