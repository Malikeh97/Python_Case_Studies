import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering

whisky = pd.read_csv("whiskies.txt")
whisky["Regions"] = pd.read_csv("regions.txt")
flavors = whisky.iloc[:, 2:14]
corr_flavors = pd.DataFrame.corr(flavors)
plt.figure(figsize = (10, 10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")

corr_whiskies = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize = (10, 10))
plt.pcolor(corr_whiskies)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whiskies.pdf")

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whiskies)
print(np.sum(model.rows_, axis = 1)) # number of whiskies in each cluster
print(np.sum(model.rows_, axis = 0)) # number of clusters for each observation
print(model.row_labels_)
