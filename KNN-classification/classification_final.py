import numpy as np
p1 = np.array([1,1])
p2 = np.array([4,4])

def distance(p1, p2):
    """Finds the distance between points p1 and p2"""
    return  np.sqrt(np.sum(np.power(p1 - p2, 2)))
