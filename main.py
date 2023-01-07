from flask import Flask, jsonify, request
from MatrixOperations import MatrixOperations
from LoadMatrix import LoadMatrix
from RequestValidator import RequestValidator

app = Flask(__name__)

###curl -F 'file=matrix.csv' "http://127.0.0.1:8080/echo"

matrix_operations = MatrixOperations()
load_matrix = LoadMatrix()
request_validator = RequestValidator()

FILE_NOT_PROVIDED_MSG = "Invalid file provided."
FILE_NOT_PROVIDED_ERR_CODE = 400

@app.route('/echo', methods=['POST'])
def echo():
    input_file = request.form.get('file')
    if(not request_validator.validate_request(input_file)):
        return FILE_NOT_PROVIDED_MSG, FILE_NOT_PROVIDED_ERR_CODE
    matrix = load_matrix.get_matrix_from_file(input_file)
    return matrix_operations.echo_matrix(matrix)

@app.route('/invert', methods=['POST'])
def invert():
    input_file = request.form.get('file')
    if (not request_validator.validate_request(input_file)):
        return FILE_NOT_PROVIDED_MSG, FILE_NOT_PROVIDED_ERR_CODE
    matrix = load_matrix.get_matrix_from_file(input_file)
    return matrix_operations.invert_matrix(matrix)

@app.route('/flatten', methods=['POST'])
def flatten():
    input_file = request.form.get('file')
    if (not request_validator.validate_request(input_file)):
        return FILE_NOT_PROVIDED_MSG, FILE_NOT_PROVIDED_ERR_CODE
    matrix = load_matrix.get_matrix_from_file(input_file)
    return matrix_operations.flatten_matrix(matrix)

@app.route('/sum', methods=['POST'])
def sum():
    input_file = request.form.get('file')
    if (not request_validator.validate_request(input_file)):
        return FILE_NOT_PROVIDED_MSG, FILE_NOT_PROVIDED_ERR_CODE
    matrix = load_matrix.get_matrix_from_file(input_file)
    return matrix_operations.get_sum_of_matrix(matrix)

@app.route('/multiply', methods=['POST'])   
def multiply():
    input_file = request.form.get('file')
    if (not request_validator.validate_request(input_file)):
        return FILE_NOT_PROVIDED_MSG, FILE_NOT_PROVIDED_ERR_CODE
    matrix = load_matrix.get_matrix_from_file(input_file)
    return matrix_operations.get_mul_of_matrix(matrix)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)