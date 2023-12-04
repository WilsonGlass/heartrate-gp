import pandas as pd
from fitparse import FitFile
from lib.data.util import extract_all_fit_data

file = FitFile('./data/Evening_Run.fit')

print(pd.DataFrame(extract_all_fit_data(file)).columns)

