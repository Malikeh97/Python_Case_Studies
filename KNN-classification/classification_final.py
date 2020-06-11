import numpy as np
from collections import Counter
import random
import scipy.stats as ss
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


def generate_synth_data(n = 100):
    """
    Create two sets of points from bivariate normal distribution
    """
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis = 0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def majority_vote(votes):
    """
    Return the most common elements in votes
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    max_count = max(vote_counts.values())
    winners = []
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    return random.choice(winners)

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

def make_prediction_grid(predictors, outcomes, limits, h, k):
    """
    classify each point on the prediction grid.
    """
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype = int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j, i] = knn_predict(p, predictors, outcomes, k) # j as row, i as col
    return (xx, yy, prediction_grid)

def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)

# (predictors, outcomes) = generate_synth_data()

# k=50; filename = "knn_synth_50.pdf"; limits = (-3, 4, -3, 4); h = 0.1
# (xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
# plot_prediction_grid(xx, yy, prediction_grid, filename)
iris = datasets.load_iris()
predictors = iris.data[:, 0:2] #extract two first columns
outcomes = iris.target
plt.plot(predictors[outcomes == 0][:,0], predictors[outcomes == 0][:,1], "ro")
plt.plot(predictors[outcomes == 1][:,0], predictors[outcomes == 1][:,1], "go")
plt.plot(predictors[outcomes == 2][:,0], predictors[outcomes == 2][:,1], "bo")
plt.savefig("iris.pdf")

k=5; filename = "iris_grid.pdf"; limits = (4, 8, 1.5, 4.5); h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)
my_predictions = np.array([knn_predict(p , predictors, outcomes, 5) for p in predictors ])
print(100*np.mean(sk_predictions == my_predictions))
print(100*np.mean(sk_predictions == outcomes)) #accuracy
print(100*np.mean(my_predictions == outcomes))
