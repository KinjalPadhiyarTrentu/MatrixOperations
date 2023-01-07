"""
Class LoadMatrix reads the matrix from given csv file.
"""

import csv
class LoadMatrix:
    def __init__(self):
        pass

    def get_matrix_from_file(self,file):
        """
        get_matrix_from_file reads the matrix from the input file.

        Accepts:
            file: string - filepath provided by user
        Returns:
            all_matrix_values: list of list of integers
        """
        
        with open(file, newline = '') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            all_matrix_values = []
            for row in reader:
                for value in row:
                    integers = [int(i) for i in value.split(',')]   
                    all_matrix_values.append(integers)

        return all_matrix_values
