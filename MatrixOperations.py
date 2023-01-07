"""
Class MatrixOperations performs all the required operations
on the given matrix. 
"""

class MatrixOperations:
    def __init__(self):
        pass

    def echo_matrix(self, mat):
        """
        1. Returns the matrix as a string in matrix format.

        Accepts: 
            mat: list of list of integers i.e. [[]int].
        Returns:
            result: string representation of a given matrix.
        """
        row = len(mat)
        col = len(mat[0])
        
        result = ""
        
        for i in range(row):
            curr = []
            for j in range(col):
                curr.append(str(mat[i][j]))
            
            result += ",".join(curr)
            if(i < row-1):
                result += "\n"
    
        return result
        
    def invert_matrix(self, mat):
        """
        2. Returns the matrix as a string in matrix format 
        where the columns and rows are inverted.

        Accepts: 
            mat: list of list of integers i.e. [[]int].
        Returns:
            string representation of an inverted matrix.
        """
        n = len(mat)
        
        inverted_matrix = []
        
        for j in range(n):
            curr = []
            for i in range(n):
                curr.append(mat[i][j])
            
            inverted_matrix.append(curr)
        
        return self.echo_matrix(inverted_matrix)
        
    def flatten_matrix(self, mat):
        """
        3. Returns the matrix as a 1 line string, 
        with values separated by commas.

        Accepts: 
            mat: list of list of integers i.e. [[]int].
        Returns:
            string representation of a flattened matrix.
        """
        n = len(mat)
        
        flattened_matrix = []
    
        for i in range(n):
            for j in range(n):
                flattened_matrix.append(mat[i][j])
        
        return self.echo_matrix([flattened_matrix])
        
    def get_sum_of_matrix(self, mat):
        """
        4. Returns the sum of the integers in the matrix.

        Accepts: 
            mat: list of list of integers i.e. [[]int].
        Returns:
            result: string - sum of the integers in the matrix.
        """
        n = len(mat)
        
        result = 0
        
        for i in range(n):
            for j in range(n):
                result += mat[i][j]
        
        return str(result)
    
    def get_mul_of_matrix(self, mat):
        """
        5. Returns the product of the integers in the matrix.

        Accepts: 
            mat: list of list of integers i.e. [[]int].
        Returns:
            result: string - product of the integers in the matrix.
        """
        n = len(mat)
        
        result = 1
        
        for i in range(n):
            for j in range(n):
                result *= mat[i][j]
        
        return str(result)
        