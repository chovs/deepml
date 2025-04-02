"""
Write a Python function that calculates the eigenvalues of a 2x2 matrix. 
The function should return a list containing the eigenvalues, sort values from highest to lowest.

Example:
Input:
matrix = [[2, 1], [1, 2]]

Output:
[3, 1]
"""


# eig


def calculate_eigenvalues(matrix:list[list[float]]) -> list[float]:
    # check the matrix is 2x2 matrix
    if len(matrix) != 2 and len(matrix[0]) != 2:
        raise ValueError("Input should be in 2x2 dimension")
    # calculate the eigenvalues
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    determinant = a * d - b * c
    
    # Calculate the eigenvalues using the characteristic polynomial: λ^2 - (trace)λ + (determinant) = 0
    trace = a + d
    # The roots of the polynomial are the eigenvalues. 
    # In this context, "roots" refer to the values of λ that satisfy the equation, meaning they make the equation equal to zero.
    eigenvalues = np.roots([1, -trace, determinant])
    eigenvalues = sorted(eigenvalues, reverse=True)  # Sort eigenvalues from highest to lowest
    return eigenvalues



"""
This is the solution from the site
def calculate_eigenvalues(matrix: list[list[float]]) -> list[float]:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    trace = a + d
    determinant = a * d - b * c
    # Calculate the discriminant of the quadratic equation
    discriminant = trace**2 - 4 * determinant
    # Solve for eigenvalues
    lambda_1 = (trace + discriminant**0.5) / 2
    lambda_2 = (trace - discriminant**0.5) / 2
    return [lambda_1, lambda_2]
"""