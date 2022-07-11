import re
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
import sys
import copy
from typing import Dict, Tuple

def get_ticker_data(tickers: Dict)-> Tuple[Dict, Dict, Dict]:
    """
    Given a list of stock market tickers

    Return a dataframe full of previous close data
    """
    past_date = datetime.today() - timedelta(days=1278)
    today = datetime.today()

    s_and_p_500_dict = dict()
    nasdaq_dict = dict()
    djia_dict = dict()
    for financial_index in tickers:
       
        count = 0 
        for ticker in tickers.get(financial_index):

            ticker_obj = yf.Ticker(ticker)
            
            data: pd.Series = ticker_obj.history(start = past_date, end = today)['Close']
            data.rename(ticker, inplace=True)

            data.index = data.index.astype(str)

            #have to convert to a dictionary
            #because pd.Series are not json serializable
            cur_dict = {'dates' : list(data.index), 'ticker': list(data.values)}
           
            if financial_index == 'S_AND_P_500':
                s_and_p_500_dict[ticker] = cur_dict
            elif financial_index == 'NASDAQ':
                nasdaq_dict[ticker] = cur_dict
            else:
                djia_dict[ticker] = cur_dict

            count += 1

    return s_and_p_500_dict, nasdaq_dict, djia_dict