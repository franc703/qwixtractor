import pandas as pd
import requests
from progressbar import ProgressBar

pbar = ProgressBar()
# create progress bar for the loop

# Construct function to make api call for qwi
def get_qwi(state = '24', key = "your api key", the_vars = ['Emp', 'TurnOvrS', 'EarnBeg']):
    HOST = 'http://api.census.gov/data/timeseries/qwi/sa?'
    get_vars = the_vars
    predicates = {}
    predicates['get'] = ",".join(get_vars)
    predicates['for'] = 'county:*'
    predicates['in'] = 'state:' + state
    predicates['sex'] = '0'
    predicates['agegrp'] = 'A00'
    predicates['industry'] = '6244'
    predicates['ownercode'] = 'A00'
    predicates['time'] = 'from 2001-Q1 to 2007-Q4'
    predicates['seasonadj'] = 'U'
    predicates['key'] = f'{key}'
    r = requests.get(HOST, params = predicates)
    df = pd.DataFrame(data = r.json()[1:])
    return df # columns = r.json()[0],


def create_qwi_df(states = "states", col_names = "col_names", my_key = "your key"):
    appended_data = []
    for st in pbar(states):
        df = get_qwi(state = st, key=my_key)
        appended_data.append(df)
    data = pd.concat(appended_data)
    data.columns = col_names
    return data