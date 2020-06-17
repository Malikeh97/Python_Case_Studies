import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("bird_tracking.csv")
ix = birddata.bird_name == 'Eric'
x , y = birddata.longitude[ix], birddata.latitude[ix]
bird_names = pd.unique(birddata.bird_name)
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.figure(figsize = (8,4))
plt.hist(speed[~ind], bins = np.linspace(0, 30, 20), normed = True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency")
plt.savefig("speed_hist.pdf")

#no need to deal with nans explicitly using pandas
birddata.speed_2d.plot(kind = "hist", range = [0, 30])
plt.xlabel("2D speed (m/s)")
plt.savefig("pd_hist")
