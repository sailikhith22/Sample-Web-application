from src.logger import logging
from src.exceptions import CustomException
import os, sys 
import pickle 


class PredictPipeline():
    def __init__(self):
        pass

    def predict(self, data):
        try:
            model_path = "Artifacts\model.pkl"
            preprocessor_path = "Artifacts\preprocessor.pkl"
            model = pickle.load(open(model_path,"rb"))
            preprocessor = pickle.load(open(preprocessor_path,"rb"))
            logging.info("Preprocessor loaded")
            print("The data received is\n\n\n type{}\n shape {}\n\n columns of the dataframe {}".format(type(data),data.shape,data.columns))
            transformed_data = preprocessor.transform(data)
            result_value = model.predict(transformed_data)
            return result_value[0]
        except Exception as e:
            raise CustomException(e,sys)
    
class CustomData:
    def __init__(self,name:str, age:int, gender:str, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15):
        self.name = name
        self.age = age
        self.gender = gender
        self.Q1 = Q1
        self.Q2 = Q2
        self.Q3 = Q3
        self.Q4 = Q4
        self.Q5 = Q5
        self.Q6 = Q6
        self.Q7 = Q7
        self.Q8 = Q8
        self.Q9 = Q9
        self.Q10 = Q10
        self.Q11 = Q11
        self.Q12 = Q12
        self.Q13 = Q13
        self.Q14 = Q14
        self.Q15 = Q15
