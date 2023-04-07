import os
import sys

from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_modelpath_config = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("Initializing model trainer")
            X_train, X_test, y_train, y_test = (train_arr[:,:-1], test_arr[:,:-1],train_arr[:,-1],test_arr[:,-1])
            logging.info("X_train {}".format(X_train.shape))
            logging.info("y_train {}".format(y_train.shape))
            logging.info("X_test {}".format(X_test.shape))
            logging.info("y_test {}".format(y_test.shape))
            models = {"decisiontree": DecisionTreeClassifier(random_state=42), "knn":KNeighborsClassifier(n_neighbors=5)}
            models_report = evaluate_models(X_train, X_test, y_train, y_test, models)

            best_score = max(sorted(models_report.values()))

            best_model_name = list(models_report.keys())[list(models_report.values()).index(best_score)]

            best_model = models[best_model_name]
            logging.info("{}".format(best_model))
            if best_score <= 0.6:
                raise CustomException("No best model found")
            logging.info("Best model found for training and testing dataset")
            logging.info("best model {}".format(best_model))
            save_object(filepath = self.model_trainer.trained_modelpath_config , obj = best_model)
            best_model.fit(X_train,y_train)
            y_predicted = best_model.predict(X_test)
            accuracy = accuracy_score(y_predicted, y_test)
           
            return accuracy
        except Exception as e:
            raise CustomException(e,sys)
            
