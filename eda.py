import io

import pandas as pd
import numpy as np

import seaborn as sns
from IPython.display import display, HTML
from IPython.core.interactiveshell import InteractiveShell

# FILE READ
file_name = 'PATH/TO/FILE'
data = pd.read_csv(file_name)

# CREATE FILE TYPE DICT DATA
buffer = io.StringIO()
data.info(buf=buffer)
info_s = buffer.getvalue()

type_dict = {}
type_row = len(info_s.splitlines()) - 3
for idx, line in enumerate(info_s.splitlines()):
