# Matrix Operations:

* The input file to these functions is a matrix, of any dimension where the number of rows are equal to the number of columns (square). Each value is an integer, and there is no header row. matrix.csv is example valid input. 

* Classes prepared: [Refer to individual classes for detailed documentation]
  
  * [LoadMatrix.py](/LoadMatrix.py) - Class LoadMatrix reads the matrix from given csv file.
  * [MatrixOperations.py](/MatrixOperations.py) - Class MatrixOperations performs all the required operations on the given matrix.
  * [RequestValidator.py](/RequestValidator.py) - Class RequestValidator validates the HTTP requests sent to web server.

* How to run:
  
  * Step-1 : Clone the repository
  * Step-2 : Run the [requirements.txt](/requirements.txt) to download necessary dependencies.
  * Step-3 : Start the web server on localhost('127.0.0.1') by running [main.py](/main.py) (Port=5000)
  * Step-4 : Send POST requests with-> 
    ```
    curl -F "file=matrix.csv" "http://127.0.0.1:5000/<ENDPOINT>"
    ``` 
    * NOTE : Supported endpoints are: /echo, /invert, /flatten, /sum, /multiply
 
 * How to run Test Cases:
   * There are 14 test cases. To run them all -> Run [TestRequestValidator.py](/TestRequestValidator.py)

