import os
import tensorflow as tf
import pandas as pd


class PreprocessUtils:

    def dataset_path(self,dataset_archive):
        splits= dataset_archive.split('/')
        file_names = splits[-1].split('.')
        ds_name = f'{file_names[0]}.{file_names[1]}'
        file_path = ''
        for name in splits[:-1]:
            file_path = os.path.join(file_path,name)
        file_path = os.path.join(file_path,ds_name)
        return file_path

    def fetch_dataset(self,url,cache_dir='.'):
        data_set_path = tf.keras.utils.get_file(origin=url,cache_dir=cache_dir,extract=True)
        file_name = self.dataset_path(data_set_path)
        return pd.read_csv(file_name)
    

    def prepare_rows_and_cols(self,data):
        rw=[]
        return_val = {'headers':data.columns.values.tolist()}
        for i in range(len(data)):
            row = data.iloc[i].values
            rw.append(data.iloc[i].values.astype(str).tolist())
        return_val['rows']=rw

        return return_val
                
        