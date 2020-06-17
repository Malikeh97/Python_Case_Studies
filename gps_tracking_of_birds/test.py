import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("bird_tracking.csv")
ix = birddata.bird_name == 'Eric'
x , y = birddata.longitude[ix], birddata.latitude[ix]
bird_names = pd.unique(birddata.bird_name)
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.hist(speed[~ind])
plt.savefig("hist.pdf")
# plt.figure(figsize=(7,7))
# for birdname in bird_names:
#     ix = birddata.bird_name == birdname
#     x , y = birddata.longitude[ix], birddata.latitude[ix]
#     plt.plot(x, y, ".", label = birdname)
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.legend(loc = "lower right")
# plt.savefig("3traj.pdf")
# plt.show()
# plt.hist(speed[:10])
# plt.show()
