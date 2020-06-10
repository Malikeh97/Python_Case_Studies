import numpy as np
from collections import Counter
import random
import scipy.stats as ss

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





votes = [1,2,3,1,2,3,1,2,3,3,3,3,3]
print(majority_vote(votes))
print(majority_vote_short(votes))
