import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model as lm
from IPython import embed

datapath = "../data/tunnel.csv"

# go here to get the data https://www.kaggle.com/code/ryanholbrook/linear-regression-with-time-series/tutorial

# Load data
df = pd.read_csv(datapath)
df["time"] = np.arange(0, len(df))

# get x and y values
x = df.time.values.reshape(-1, 1)
y = df.NumVehicles.values.reshape(-1, 1)

# define the model
model = lm.LinearRegression()

# fit the model
reg = model.fit(x, y)

newx = np.arange(0, 1000).reshape(-1, 1)

plt.plot(x, y, "o")
plt.plot(newx, reg.predict(newx), "r-")
plt.text(0, 130000, f"R^2: {np.round(reg.score(x, y), 3)}")
plt.xlabel("Time")
plt.ylabel("Number of Vehicles")
plt.show()
