import numpy as np
from collections import Counter
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

def generate_synth_data(n = 50):
    """
    Create two sets of points from bivariate normal distribution
    """
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis = 0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)

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


p = np.array([2.5, 2])
n = 20
(points, outcomes) = generate_synth_data(n)
print(knn_predict(p , points, outcomes, 5))


plt.figure()
plt.plot(points[:n,0], points[:n,1], "ro")
plt.plot(points[n:,0], points[n:,1], "bo")
plt.plot(p[0], p[1], "yo")
plt.axis([-3.5,3.5, -3.5, 3.5])
plt.savefig('bivardata.pdf')
plt.show()
