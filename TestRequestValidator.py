import unittest
from RequestValidator import RequestValidator
from LoadMatrix import LoadMatrix
from MatrixOperations import MatrixOperations

request_validator = RequestValidator()
load_matrix = LoadMatrix()
matrix_operations = MatrixOperations()

class TestRequestValidator(unittest.TestCase):

    def test_validate_request_negative(self):
        expected_output = False
        actual_output = request_validator.validate_request("")
        self.assertEqual(expected_output, actual_output, "Did not get the valid input file")

    def test_validate_request_positive(self):
        expected_output = True
        actual_output=request_validator.validate_request("matrix.csv")
        self.assertEqual(expected_output, actual_output, "Got valid file")

    def test_get_matrix_from_file_negative(self):
        expected_output = [[10,20,30],[40,50,60],[70,80,90]]
        actual_output = load_matrix.get_matrix_from_file("matrix.csv")
        self.assertNotEqual(expected_output, actual_output, "Did not get the expected matrix from file")
    
    def test_get_matrix_from_file_positive(self):
        expected_output = [[1,2,3],[4,5,6],[7,8,9]]
        actual_output = load_matrix.get_matrix_from_file("matrix.csv")
        self.assertEqual(expected_output, actual_output, "Got the expected matrix from file")
    
    def test_echo_matrix_negative(self):
        expected_output = "10,20,30"+"\n"+"40,50,60"+"\n"+"70,80,90"
        actual_output = matrix_operations.echo_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertNotEqual(expected_output, actual_output, "Did not get correct representation of matrix")

    def test_echo_matrix_positive(self):
        expected_output = "1,2,3"+"\n"+"4,5,6"+"\n"+"7,8,9"
        actual_output = matrix_operations.echo_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertEqual(expected_output, actual_output, "Got correct representation of matrix")

    def test_invert_matrix_negative(self):
        expected_output = "10,40,70"+"\n"+"20,50,80"+"\n"+"30,60,90"
        actual_output = matrix_operations.invert_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertNotEqual(expected_output, actual_output, "Did not get correct inverted matrix")

    def test_invert_matrix_positive(self):
        expected_output = "1,4,7"+"\n"+"2,5,8"+"\n"+"3,6,9"
        actual_output = matrix_operations.invert_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertEqual(expected_output, actual_output, "Got correct inverted matrix")

    def test_flatten_matrix_negative(self):
        expected_output = "10,20,30,40,50,60,70,80,90"
        actual_output = matrix_operations.flatten_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertNotEqual(expected_output, actual_output, "Did not get correct flattened matrix")

    def test_flatten_matrix_positive(self):
        expected_output = "1,2,3,4,5,6,7,8,9"
        actual_output = matrix_operations.flatten_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertEqual(expected_output, actual_output, "Got correct flattened matrix")

    def test_get_sum_of_matrix_negative(self):
        expected_output = "450"
        actual_output = matrix_operations.get_sum_of_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertNotEqual(expected_output, actual_output, "Did not get correct sum of the integers in the matrix")

    def test_get_sum_of_matrix_positive(self):
        expected_output = "45"
        actual_output = matrix_operations.get_sum_of_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertEqual(expected_output, actual_output, "Got correct sum of the integers in the matrix")

    def test_get_mul_of_matrix_negative(self):
        expected_output = "3628800"
        actual_output = matrix_operations.get_mul_of_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertNotEqual(expected_output, actual_output, "DId not get correct product of the integers in the matrix")

    def test_get_mul_of_matrix_positive(self):
        expected_output = "362880"
        actual_output = matrix_operations.get_mul_of_matrix(load_matrix.get_matrix_from_file("matrix.csv"))
        self.assertEqual(expected_output, actual_output, "Got correct product of the integers in the matrix")

if __name__ == "__main__":
    unittest.main()