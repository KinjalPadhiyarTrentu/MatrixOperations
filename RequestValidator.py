"""
Class RequestValidator validates the HTTP request.
"""

from os.path import exists
from pathlib import Path

class RequestValidator:
    def __init__(self):
        pass
    
    def validate_provided_file(self, file):
        return exists(file) and Path(file).is_file()

    def validate_request(self, file):
        """
        validate_request validates incoming request based on
        whether or not valid file was provided.

        Accepts:
            file: string - filepath provided by user
        Returns:
            boolean - True if valid file was provided
                      False otherwise
        """
        if(file == None or file == ""):
            return False
        return self.validate_provided_file(file)