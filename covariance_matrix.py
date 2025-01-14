"""
Write a Python function to calculate the covariance matrix for a given set of vectors. The function should take a list of lists, where each inner list represents a feature with its observations, and return a covariance matrix as a list of lists. Additionally, provide test cases to verify the correctness of your implementation.
"""

"""
Example:
Input:
[[1, 2, 3], [4, 5, 6]]
Output:
[[1.0, 1.0], [1.0, 1.0]]
Reasoning:
The covariance between the two features is calculated based on their deviations from the mean. For the given vectors, both covariances are 1.0, resulting in a symmetric covariance matrix.
"""

"""
algorithm
- find mean
We calculate mean by pick each value from the set in list representation from left to right to calculate the sum of all value, each time we store value as a variable (value)
and we count how much time we need to as a another variable (count).

- find variance
We use (value) variable to find the difference and scale it with two to get the square terms and divided this term with (count) variable




-find covariance 
we use (value) variable and mean two times


"""


def calculate_covariance_matrix(vector: list[list[float]]) -> list[list[float]]:
   n_features = len(vector)
   covariance_matrix = [[0.0] * n_features for _ in range(n_features)]
   
   means = []
   for feature in vector:
       value = 0
       count = 0
       for x in feature:
           value += x
           count += 1
       means.append(value / count)
   
   for i in range(n_features):
       for j in range(n_features):
           if i == j:
               value = 0
               count = 0
               for x in vector[i]:
                   value += (x - means[i]) ** 2
                   count += 1
               covariance_matrix[i][i] = value / count
           
           else:
               value = 0
               count = 0
               for x, y in zip(vector[i], vector[j]):
                   value += (x - means[i]) * (y - means[j])
                   count += 1
               covariance_matrix[i][j] = value / count
   
   return covariance_matrix

if __name__ == "__main__":
   test_data = [
       [1.0, 2.0, 3.0],
       [4.0, 5.0, 6.0]
   ]
   
   result = calculate_covariance_matrix(test_data)
   print("Covariance Matrix:")
   for row in result:
       print(row)








