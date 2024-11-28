"""
Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, while maintaining the corresponding order between them. 
The function should have an optional seed parameter for reproducibility.

Example:
    X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8]])
    y = np.array([1, 2, 3, 4])
    output: (array([[5, 6],
                    [1, 2],
                    [7, 8],
                    [3, 4]]), 
             array([3, 1, 4, 2]))
"""

"""
outline

shuffle the list and the list of list
the element of the list of list doesn't change

Concept: "combination of row iteration"
    - Rearrange the index of sequence of each row in each numpy array
            Because of the countable case of shuffling, we will calculate the probability
             #set of sample space - 4!*4!
            s = [0,1,2,3],[0,1,2,3] # these values are index number
        
Sketch of my logic:

    # condition for seed existence that same index of numpy array will have the same seed value

    # Rearrange the index of sequence of each row in each numpy array
"""


import numpy as np

def shuffle_data(X, y, seed=None):
    # Condition for deterministic function of non-deterministic 
    if seed:
        np.random.random(seed)
    # Rearrange the index of sequence of each row in each numpy array
    num_samples = len(X)
    indices = np.random.permutation(num_samples)
    return X[indices], y[indices]


# Example case
# Case 1: Simple 2D array with numerical labels
shuffle_data(
    X=np.array([[1, 2], [3, 4], [5, 6], [7, 8]]),
    y=np.array([10, 20, 30, 40]),
    seed=42
)
# Expected output example:
# (array([[5, 6], [1, 2], [7, 8], [3, 4]]), array([30, 10, 40, 20]))

# Case 2: Features with one-hot encoded labels
shuffle_data(
    X=np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]),
    y=np.array([[1,0,0], [0,1,0], [0,0,1]]),
    seed=42
)
# Expected output example:
# (array([[0.5, 0.6], [0.1, 0.2], [0.3, 0.4]]), 
#  array([[0,0,1], [1,0,0], [0,1,0]]))

# Case 3: Text features with categorical labels
shuffle_data(
    X=np.array([['red', 'hot'], ['blue', 'cold'], ['green', 'warm']]),
    y=np.array(['A', 'B', 'C']),
    seed=42
)
# Expected output example:
# (array([['green', 'warm'], ['red', 'hot'], ['blue', 'cold']]),
#  array(['C', 'A', 'B']))

# Case 4: Sparse matrix features
shuffle_data(
    X=np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]),
    y=np.array([1, 0, 1, 0]),
    seed=42
)
# Expected output example:
# (array([[0,0,1,0], [1,0,0,0], [0,0,0,1], [0,1,0,0]]),
#  array([1, 1, 0, 0]))

# Case 5: Features with different scales
shuffle_data(
    X=np.array([[1000, 0.001], [2000, 0.002], [3000, 0.003]]),
    y=np.array([0, 1, 2]),
    seed=42
)
# Expected output example:
# (array([[3000, 0.003], [1000, 0.001], [2000, 0.002]]),
#  array([2, 0, 1]))

# Case 6: Single feature example
shuffle_data(
    X=np.array([[1], [2], [3], [4]]),
    y=np.array([0, 1, 0, 1]),
    seed=42
)
# Expected output example:
# (array([[3], [1], [4], [2]]),
#  array([0, 0, 1, 1]))