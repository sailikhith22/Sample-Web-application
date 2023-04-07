from src.logger import logging
from src.exceptions import CustomException
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import  DataTransformationConfig
from src.components.model_development import ModelTrainer
from src.components.model_development import ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("Artifacts","train_data.csv")
    test_data_path = os.path.join("Artifacts","test_data.csv")
    raw_data_path = os.path.join("Artifacts","raw_data.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Data ingestion started..")
            df = pd.read_csv("notebook\data\modified_dataset.csv")

            os.makedirs((os.path.dirname(self.data_ingestion.train_data_path)),exist_ok=True)
            df.to_csv(self.data_ingestion.raw_data_path, header=True, index=False)
            logging.info("Raw data has stored in the desired location")
            logging.info("training and testing of the data has been initiated")
            train_set, test_set = train_test_split(df, test_size = 0.2,random_state=42)

            train_set.to_csv(self.data_ingestion.train_data_path,index=False,header=True)
            logging.info("training dataset has been saved to the desired location")
            test_set.to_csv(self.data_ingestion.test_data_path,index=False,header=True)
            logging.info("testing dataset has been saved to the desired location")

            return self.data_ingestion.train_data_path, self.data_ingestion.test_data_path 
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()

    data_transformation_obj = DataTransformation()
    train_data, test_data = data_transformation_obj.initiate_data_transformation(train_data_path,test_data_path)
    
    model_trainer = ModelTrainer()
    logging.info("Final accuracy of the model is {}".format(model_trainer.initiate_model_trainer(train_data,test_data)))
    logging.info("Model Development Completed")