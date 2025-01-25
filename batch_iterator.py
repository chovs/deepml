"""
Write a Python function to create a batch iterator for the samples in a numpy array X and an optional numpy array y. 
The function should yield batches of a specified size. If y is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield batches of X only.

Example:
    X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
    y = np.array([1, 2, 3, 4, 5])
    batch_size = 2
    batch_iterator(X, y, batch_size)
    output:
    [[[[1, 2], [3, 4]], [1, 2]],
     [[[5, 6], [7, 8]], [3, 4]],
     [[[9, 10]], [5]]]

     Reasoning:
    The dataset X contains 5 samples, and we are using a batch size of 2. 
    Therefore, the function will divide the dataset into 3 batches. The first two batches will contain 2 samples each, 
    and the last batch will contain the remaining sample. The corresponding values from y are also included in each batch.


    idea:
    
"""

from typing import Optional, Union, Generator, Tuple
import numpy as np

def batch_iterator(
    X: np.ndarray,
    y: Optional[np.ndarray] = None,
    batch_size: int = 32
) -> Generator[Union[np.ndarray, Tuple[np.ndarray, np.ndarray]], None, None]:
    """Creates batches from numpy arrays X and optional y"""
    n_samples = len(X)
    
    for start in range(0, n_samples, batch_size):
        end = min(start + batch_size, n_samples)
        if y is not None:
            yield X[start:end], y[start:end]
        else:
            yield X[start:end]
    

X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
batch_iterator(X, y, batch_size)
for batch in batch_iterator(X, y, batch_size):
    print(batch)