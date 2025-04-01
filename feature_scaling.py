"""
Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. Make sure all results are rounded to the nearest 4th decimal.
Example:
        input: data = np.array([[1, 2], [3, 4], [5, 6]])
        output: ([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])
        reasoning: Standardization rescales the feature to have a mean of 0 and a standard deviation of 1.
        Min-max normalization rescales the feature to a range of [0, 1], where the minimum feature value
        maps to 0 and the maximum to 1.
"""
import numpy as np

data = np.array([[1,2],[3,4],[5,6]])

def feature_scaling(data):
    """
    arg: data input with any given dimension
    output: the new scale of value of the data input
    """
    mean_axis_0 = np.mean(data, axis=0)
    standard_deviation = np.std(data, axis=0) 

    # Standardization
    standardized_data = (data - mean_axis_0) / standard_deviation
    
    # Min-Max Normalization
    min_values = np.min(data, axis=0)
    max_values = np.max(data, axis=0)
    min_max_scaled_data = (data - min_values) / (max_values - min_values)
    
    # Round results to 4 decimal places
    standardized_data = np.round(standardized_data, 4)
    min_max_scaled_data = np.round(min_max_scaled_data, 4)
    
    return standardized_data, min_max_scaled_data






