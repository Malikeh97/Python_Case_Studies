import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("bird_tracking.csv")
ix = birddata.bird_name == 'Eric'
x , y = birddata.longitude[ix], birddata.latitude[ix]
print(x)
plt.figure(figsize=(7,7))
plt.plot(x, y, ".")
plt.show()
