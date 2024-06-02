from .preprocess_utils import PreprocessUtils
import pandas as pd


class Regression(PreprocessUtils):

    def __init__(self,file_name):
        self.file_name = file_name

    def preprcess_data(self):
        data_set = self.fetch_dataset(self.file_name,cache_dir='.')
        print('=============dataset',data_set.head(3))
        return data_set
        
        

    def run(self):
        processed_data = self.preprcess_data()
        return processed_data
        processed_data = self.prepare_rows_and_cols(processed_data.head(12))

