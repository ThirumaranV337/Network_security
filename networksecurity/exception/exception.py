"""Adds the original source file and line number to project errors."""

import sys
from networksecurity.logging import logger

# A project-specific error that preserves where the original failure happened.
class NetworkSecurityException(Exception):##here we are inheriting the parent class Exception
    def __init__(self,error_message,error_details:sys):
        # Keep the original error text and inspect Python's current exception details.
        self.error_message=error_message##assing the error message to the instance variable 
        _,_,exc_tb=error_details.exc_info()##in the error_details object we using the exc_info() 

        # Save the source line and filename where the exception was raised.
        self.lineno=exc_tb.tb_lineno##from the table we getting the line info
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    # Format the saved details so the error is readable in the terminal.
    def __str__(self):##overiding the message 
        return "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(self.file_name,self.lineno,str(self.error_message))

# This optional self-test demonstrates how the custom exception appears.
if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
        logger.logging.info("Enter the except block")
        raise  NetworkSecurityException(e,sys)
