import logging
import os
from datetime import datetime

#logging.basicConfig(filename='example.log', level=logging.DEBUG)



log_file = datetime.now().strftime("%m-%d-%Y %H-%M-%S")+".log"
file_path = os.path.join(os.getcwd(),"Logs")

log_file_path = os.path.join(file_path,log_file)

fmt = "[%(asctime)s] : %(name)s : %(levelname)s : line no- %(lineno)s : %(message)s"

logging.basicConfig(filename=log_file_path,format=fmt ,level=logging.DEBUG)

if __name__ == "__main__" :
    logging.info("logging has started") 
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')