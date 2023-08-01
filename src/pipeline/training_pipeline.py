import sys
from src.components.data_ingestion import dataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException

class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            data_ingestion=dataIngestion()
            feature_store_file_path=data_ingestion.innitiate_data_ingestion()
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e,sys)
    
    def start_data_transformation(self,feature_Store_file_path):
        try:
            data_transformation=DataTransformation(feature_store_file_path=feature_Store_file_path)
            train_arr,test_arr,preprocessor_path=data_transformation.initiate_data_transformation()
            return train_arr,test_arr,preprocessor_path
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def start_model_training(Self,train_arr,test_arr):
        try:
            model_trainer=ModelTrainer()
            model_score=model_trainer.initiate_model_trainer(
                train_arr,test_arr
            )
            return model_score
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def run_pipeline(self):
        try:
            feature_store_file_path=self.start_data_ingestion()
            train_arr,test_arr,preprocessor_path=self.start_data_transformation(feature_store_file_path)
            r2_Square=self.start_model_training(train_arr,test_arr)
        
            print("training completed. Trained model score : ", r2_Square)
        except Exception as e:
            raise CustomException(e,sys)
        
    