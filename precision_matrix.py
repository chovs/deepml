"""
Write a Python function precision that calculates the precision metric given two numpy arrays: y_true and y_pred. The y_true array contains the true binary labels, and the y_pred array contains the predicted binary labels. Precision is defined as the ratio of true positives to the sum of true positives and false positives.
"""

"""
Example:
Input:
import numpy as np

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])

result = precision(y_true, y_pred)
print(result)
Output:
1.0
"""

def precision(y_true, y_pred):
    true_positive = 0
    false_positive = 0  
    # Compare the two list of array and count the positive index
    for i in range(len(y_true)):
        if y_pred[i] == 1: # the positive prediction array is the new sample space
            if y_true[i] == 1:
                true_positive += 1
            else:
                false_positive += 1  
    
    # handle the non-existence case because of zero divisor
    if true_positive + false_positive == 0:  
        return print(f"Can not find the precision value")
        
    return true_positive / (true_positive + false_positive) 


# Example case 
# Case 1:
# y_true = np.array([1, 0, 1, 1, 0, 1])
# y_pred = np.array([1, 0, 1, 0, 0, 1])
# Expected output 
# 1.0

# Case 2:
# y_true = np.array([1, 0, 1, 1, 0, 0]) 
# y_pred = np.array([1, 0, 0, 0, 0, 1])
# Expected output
# 0.5