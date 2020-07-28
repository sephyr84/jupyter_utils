import pandas as pd
import numpy as np

from my_logger import mylogger
import my_logger; logger = my_logger.logger

@mylogger
def save_csv(file_name, dataframe):
  '''save dataframe to csv'''
  dataframe.to_csv(file_name, index=False, header=False)
  
@mylogger
def load_csv(file_name):
  '''load dataframe from csv'''
  result = pd.read_csv(file_name, header=None)
  result.columns = [COLUMN NAMES]
  return result

@mylogger
def change_cd_to_idx(dataframe):
  '''change cd to index
  index start from 0'''
  
  cd_to_idx = dict(enumerate(np.sort(dataframe.unique())))
  idx_to_cd = dict(zip(cd_to_idx.values(), cd_to_idx.keys()))
  return cd_to_idx, idx_to_cd

@mylogger
def add_idx_column(dataframe, idx_to_cd):
  '''add index column from dataframe and idx_to_cd'''
  return [idx_to_cd[i] for i in dataframe]
