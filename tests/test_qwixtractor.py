from qwixtractor.qwixtractor import  get_qwi, create_qwi_df
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
# environment variables

api_key = os.getenv('qwi_key')
col_names = ['emp', 'turn_overs', 'earn_beg', 'sex', 'age_group', 'industry', 'owner_code','quarter', 'season_adj', 'state', 'county']

def test_create_qwi_df():
    """ Test if create_qwi_df() function create a panda dataframe"""
    actual =  create_qwi_df(states = '27', col_names = col_names, my_key = api_key)
    assert isinstance(actual, pd.DataFrame), "We correctly generated a pandas dataframe with QWI data"
