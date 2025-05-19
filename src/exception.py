import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def error_message_detail(error, error_detail: sys):
    """
    This function takes an error and its details as input and returns a formatted error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message  

class customException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the custom exception with an error message and its details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        logging.error(f"Custom Exception Raised: {self.error_message}")  # Log the custom exception

    def __str__(self):
        """
        Returns the string representation of the custom exception.
        """
        return self.error_message


