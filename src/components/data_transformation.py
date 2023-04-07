import os
import sys

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer 
from src.logger import logging
from src.exceptions import CustomException
from src.utils import save_object
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

@dataclass
class DataTransformationConfig:
    preprocessor_objfile_path = os.path.join("artifacts","preprocessor.pkl")


class Data_Reduction( BaseEstimator, TransformerMixin):
    def __init__(self):
        print("Inside the CustomFunctions")

    def fit(self,df):        
        return self
    
    def transform(self,df):
        df["Questions_total"] = df.filter(regex='^Que',axis=1).sum(axis=1)       
        df["Misses_total"] = df.loc[:,df.columns.str.startswith("Mis")].sum(axis=1)
        df["Score_total"] = df.loc[:,df.columns.str.startswith("Sco")].sum(axis=1)
        df["Accuracy_total"] = df.loc[:,df.columns.str.startswith("Acc")].sum(axis=1)
        df["Missrate_total"] = df.loc[:,df.columns.str.startswith("Missra")].sum(axis=1)    
        df = df[["Gender","Nativelang","Otherlang","Age","Questions_total","Misses_total","Score_total","Accuracy_total","Missrate_total"]]
        return df

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        This function is create pipeline about the data transformation w.r.to the data column types
        """
        try:
            Oh_Enc = OneHotEncoder(sparse_output=True, handle_unknown="ignore") 
            data_reduction_pipe = Pipeline([("data_reduction",Data_Reduction())])
            num_pipe = Pipeline([("num_compute",SimpleImputer(missing_values=np.nan,strategy="mean")),("Scaler",StandardScaler())])
            cat_pipe = Pipeline([("cat_compute",SimpleImputer(missing_values="missing_values",strategy="most_frequent")),("onehot",Oh_Enc)])
            num_features = ["Age","Questions_total","Misses_total","Score_total","Accuracy_total","Missrate_total"]
            cat_features = ["Gender","Nativelang","Otherlang"]
            logging.info("features has been separated")
            logging.debug("num features are {}".format(num_features))
            logging.debug("cat_features are {}".format(cat_features))
            cols_transformer = ColumnTransformer([("num_pipeline",num_pipe,num_features),("cat_pipeline",cat_pipe,cat_features)])
            preprocessor = make_pipeline(data_reduction_pipe, cols_transformer)
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
            
    
    def  initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("training and testing dataset completed")

            target_name = "Dyslexia"
            input_feature_train_df = train_df.drop(columns=[target_name],axis=1)
            logging.info("input_feature_train_df columns are {}".format(input_feature_train_df.columns))
            target_feature_train_df = train_df[target_name]
            input_feature_test_df = test_df.drop(columns=[target_name],axis=1)
            target_feature_test_df = test_df[target_name]

            preprocessing_obj = self.get_data_transformer_object()

            logging.info("input and output features for training and testing datasets has been divided")
            logging.debug("this is input_feature_train_df {}".format(input_feature_train_df))
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.fit_transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(filepath=self.data_transformation_config.preprocessor_objfile_path, obj=preprocessing_obj)

            return train_arr, test_arr#, self.data_transformation_config.preprocessor_objfile_path



        except Exception as e:
            raise CustomException(e,sys)
