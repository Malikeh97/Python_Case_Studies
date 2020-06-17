import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

birddata = pd.read_csv("bird_tracking.csv")
ix = birddata.bird_name == 'Eric'
data = birddata[birddata.bird_name == 'Eric']
x , y = birddata.longitude[ix], birddata.latitude[ix]
bird_names = pd.unique(birddata.bird_name)
speed = birddata.speed_2d[ix]
date_str = birddata.date_time[0]
timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)
times = birddata.timestamp[birddata.bird_name == 'Eric']
elapsed_time = [time - times[0] for time in times]
# plt.plot(np.array(elapsed_time)/ datetime.timedelta(days = 1))
# plt.xlabel("Observation")
# plt.ylabel("Elapsed time (days)")
# plt.savefig("timeplot.pdf")
elapsed_days = np.array(elapsed_time)/ datetime.timedelta(days = 1)
next_day = 1
inds = []
daily_mean_speed = []
for (i, t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize= (8, 6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("dms.pdf")


# ind = np.isnan(speed)
# plt.figure(figsize = (8,4))
# plt.hist(speed[~ind], bins = np.linspace(0, 30, 20), normed = True)
# plt.xlabel("2D speed (m/s)")
# plt.ylabel("Frequency")
# plt.savefig("speed_hist.pdf")
#
# #no need to deal with nans explicitly using pandas
# birddata.speed_2d.plot(kind = "hist", range = [0, 30])
# plt.xlabel("2D speed (m/s)")
# plt.savefig("pd_hist")
