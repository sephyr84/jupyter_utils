import io
# Data handling library
import pandas as pd
import numpy as np
# Data Visualizing library
import seaborn as sns
from IPython.display import display, HTML
from IPython.core.interactiveshell import InteractiveShell
from ipywidgets import interact, interactive, fixed, interact_manual
import matplotlib.pyplot as plt
import seaborn as sns

# FILE READ
file_name = 'PATH/TO/FILE'
data = pd.read_csv(file_name)

# CREATE COL_DATA_TYPE DICT_DATA
def get_type_dict(dataname):
    data = dataname
    # CREATE FILE TYPE DICT DATA
    buffer = io.StringIO()
    col_len = len(dataname.columns)
    dataname.info(buf=buffer, max_cols=col_len)
    info_s = buffer.getvalue()
    type_dict = {}
    type_row = len(info_s.splitlines()) - 3
    for idx, line in enumerate(info_s.splitlines()):
        if (idx >= 3) & (idx <= type_row):
            col_name = line.split()[0]
            type_name = line.split()[3]
            type_dict[col_name] = type_name
    
    return type_dict

type_dict = get_type_dict(data)

# CHANGE FLOAT TO INT
def float_to_int(dataframe, type_dict):
    changed_cols = []
    for col in dataframe.columns:
        if 'float' in type_dict[col]:
            if dataframe[col].apply(float.is_integer).all() == True:
                dataframe[col] = dataframe[col].astype('int')
                changed_cols.append(col)
                
    print("changed_cols :", changed_cols)

    return dataframe, changed_cols
        
data, changed_cols = float_to_int(data, type_dict)

# REMOVE ONE DATA COLUMNS
def remove_one_data(dataframe):
    remove_cols = []
    for col in dataframe.columns:
        data_len = len(dataframe.groupby(col).count())
        if data_len == 1:
            dataframe = dataframe.drop(col, axis=1)
            remove_cols.append(col)
            
    print("remove_cols :", remove_cols)
            
    return dataframe, remove_cols

data, remove_cols = remove_one_data(data)

# DATA VISUALIZE FOR EDA
@interact
def show_col_info(col_name=data.columns):
    count_table = data.reset_index().groupby(col_name).count().reset_index()[[col_name, 'index']].sort_values('index', ascending=False)
    count_table = count_table.rename(columns={'index':'count'})
    count_table['rate'] = count_table['count'] / len(data)
    if 'float' in type_dict[col_name]:
        ax = sns.distplot(data[~data[col_name].isna()][col_name])
    else:
        ax = sns.barplot(x=col_name, y='count', data=count_table[:10])
    plt.show()
    
    if data[col_name].isnull().sum() > 0:
        null_table = data.isnull()[[col_name]].reset_index().groupby(col_name).count().reset_index()
        null_table = null_table.rename(columns={'index':'count'})
        null_table['rate'] = null_table['count'] / len(data)
        print('NULL TABLE')
        display(null_table)
    print("<", col_name, ">")
    display(count_table[:10])

# DATA FILTER FOR ANAYSIS
def remove_null_cols(dataframe, rate=0, ch_method='mean'):
    null_cols = []
    ch_cols = []
    for col in dataframe.columns:
        if dataframe[col].isnull().sum() > rate:
            null_cols.append(col)
        elif (dataframe[col].isnull().sum() <= rate) & (dataframe[col].isnull().sum() > 0):
            ch_cols.append(col)
            
    if ch_method=='mean':
        return dataframe.drop(null_cols, axis=1).fillna(dataframe[ch_cols].mean()), null_cols, ch_cols
    elif ch_method=='max':
        return dataframe.drop(null_cols, axis=1).fillna(dataframe[ch_cols].max()), null_cols, ch_cols
    elif ch_method=='min':
        return dataframe.drop(null_cols, axis=1).fillna(dataframe[ch_cols].min()), null_cols, ch_cols
            
    return dataframe_null.drop(null_cols, axis=1), null_cols

# FACTORIZE CATEGORICAL DATA
def dataframe_fac(dataframe):
    dataframe_dict = {}
    object_cols = []
    for col in dataframe.columns:
        if type_dict[col] == 'object':
            fac = pd.factorize(dataframe[col], sort=True)
            dataframe[col+'_fac'] = fac[0]
            dataframe_dict[col] = dataframe[[col, col+'_fac']].drop_duplicates()
            object_cols.append(col)
            dataframe[col] = dataframe_fac[col+'_fac']
            dataframe = dataframe.drop(col+'_fac', axis=1)
            
    return dataframe, dataframe_dict, object_cols
