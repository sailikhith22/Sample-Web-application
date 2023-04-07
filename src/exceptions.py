import sys
from src.logger import logging
 
def error_message_details(error, error_detail):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] and line no {1} error message is {2}".format(filename,exc_tb.tb_lineno,str(error))
    logging.error(error_message)
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)
    def __str__(self):
        return self.error_message

if __name__ == '__main__':
    try:
        logging.info("logging started for exceptions")
        a,b = 10, 0
        logging.info("c value is {}".format(a/b))
    except Exception as e:
        logging.error("Exception caused by division by zero")
        raise CustomException(e,sys)