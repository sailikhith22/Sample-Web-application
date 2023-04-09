import numpy as np
import pandas as pd
import os 
import sys
import pymongo

from src.logger import logging
from src.exceptions import CustomException
import pickle 
from sklearn.metrics import accuracy_score 
from src.extractinginfo import get_answers

def save_object(filepath,obj):
    """
    This function is to save the obj as pickle in the filepath location
    """ 

    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        with open(filepath,"wb") as f:
            pickle.dump(obj,f)
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train, X_test, y_train, y_test, models):
    
    report = {}
    logging.info("model values {}".format(list(models.values())))
    for i in range(len(list(models))):
        
        model = list(models.values())[i]
        
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)

        logging.info("Inside the utils file Accuracy: {}".format(accuracy))

        report[list(models.keys())[i]] = accuracy
    
    return report 



def get_columns(orig, given):
    if orig>given:
        miss = orig - given
    else:
        miss=0

    if given>orig:
        score = orig-given
    else:
        score = given 
    
    if score<0:
        accuracy=0.0
    else:
        accuracy = score/orig
    
    misrate = 1-accuracy
    return orig , miss, score, accuracy, misrate
# Connecting to Demo1db Database
# Only collections differ 
#client = pymongo.MongoClient("mongodb+srv://maheshbabu9199:RXsHAm3fjrstQQoy@cluster0.6nqhrwi.mongodb.net/test")
#mydb = client["MyDemodatabase"]

def store_surveydata(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11):
    #survey = mydb.Surveytable
   # records = {"name":Q1,"age":Q2, "gender":Q3,"Question1":Q4, "Question2":Q5, "Question3":Q6, "Question4":Q7, "Question5":Q8, "Question6":Q9,"Question7":Q10,"Question8":Q11}
    #survey.insert_one(records)
    print("inside store_surveydata")



# here questions means given answers, answers means original answers
# questions are list, answers are in dict format 
# message = {'name': 'sdfasdf', 'age': 13123, 'gender': 'male'}
def store_examdata(message, questions):
    answers = get_answers()
    message = eval(message)
    logging.info("inside the store_examdata func answers are\n{}".format(answers))
    logging.info("\ninside the store_examdata func questions are\n{}".format(questions))
    logging.info("message inside func\n".format(message))
    records = {} 
    
    gender_value = message["gender"] 
    age_value = message["age"]
     
    records = {"Gender": gender_value , "Nativelang":"no", "Otherlang": "yes", "Age": age_value}
    logging.info("\ninsid the store_examdata function records before loop are\n{} ".format(records))
    for i in range(15):
        orig, misses, score, accuracy, misrate = get_columns(answers[i+1], questions[i])
        logging.info("For {}th question the values are ".format(i+1))
        logging.info("orig:{} miss:{} score:{} accuracy:{} misrate:{}".format(orig, misses, score, accuracy, misrate))
        records["Question"+str(i+1)] = orig
        records["Misses"+str(i+1)] = misses
        records["Score"+str(i+1)] = score
        records["Accuracy"+str(i+1)] = accuracy
        records["Misrate"+str(i+1)] = misrate
    logging.info("\n\nFinal records\n{}".format(records))
    return records
    #exams_data = mydb.Examtable
    #exams_data.insert_one(records)
     

def get_dataframe(data):
    
    data_dataframe = {}
    for key, value in data.items():
        data_dataframe[key] = [value]
    dataframe = pd.DataFrame(data_dataframe)
    return dataframe