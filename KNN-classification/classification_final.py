import numpy as np
from collections import Counter
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

p1 = np.array([1,1])
p2 = np.array([4,4])

def distance(p1, p2):
    """Finds the distance between points p1 and p2"""
    return  np.sqrt(np.sum(np.power(p1 - p2, 2)))

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

def majority_vote_short(votes):
    """
    Return the most common elements in votes
    """
    mode, count = ss.mstats.mode(votes)
    return mode

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return(ind)

def knn_predict(p , points, outcomes, k):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])



points = np.array([[1,1], [1,2], [1,3], [2,1] ,[2,2] ,[2,3], [3,1], [3,2], [3,3]])
p = np.array([2.5, 2])
outcomes = np.array([0,0,0,0,1,1,1,1,1])
print(knn_predict(p , points, outcomes, 2))


plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5,3.5, 0.5, 3.5])
plt.show()
