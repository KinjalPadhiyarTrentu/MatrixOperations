# Matrix Operations:
League Backend Challenge - League Inc. Assessment

* The input file to these functions is a matrix, of any dimension where the number of rows are equal to the number of columns (square). Each value is an integer, and there is no header row. matrix.csv is example valid input. 

* Classes prepared: [Refer to individual classes for detailed documentation]
  
  * LoadMatrix.py - Class LoadMatrix reads the matrix from given csv file.
  * MatrixOperations.py - Class MatrixOperations performs all the required operations
    on the given matrix.
  * RequestValidator.py - Class RequestValidator validates the HTTP request.

* How to run:
  
  * Step-1 : Clone the repository
  * Step-2 : Run the requirements.txt to download necessary dependencies.
  * Step-3 : Start the web server on localhost('127.0.0.1') by running main.py (Port=5000)
  * Step-4 : Send POST requests with-> 
    ```
    curl -F "file=matrix.csv" "http://127.0.0.1:5000/<ENDPOINT>"
    ``` 
    * NOTE : Supported endpoints are: /echo, /invert, /flatten, /sum, /multiply
 
 * How to run Test Cases:
   * Run TestRequestValidator.py

