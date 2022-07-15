import re
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, date
import sys
import copy
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

# For getting and parsing the data from the website
from bs4 import BeautifulSoup
import requests

def handle_tickers_retrieve_data(tickers_list:list)->dict:
    """
    Given a list of tickers, retrieve data from yahoo finance

    returns a dictionary that will be saved as json
    """
    return_dict = dict()

    past_date = datetime.today() - timedelta(days=1278)
    today = datetime.today()

    for ticker in tickers_list:

        print(f"\n ticker {ticker} is running \n")

        ticker_obj = yf.Ticker(ticker)
        
        data: pd.Series = ticker_obj.history(start = past_date, end = today)['Close']
        data.rename(ticker, inplace=True)

        data.index = data.index.astype(str)

        #have to convert to a dictionary
        #because pd.Series are not json serializable
        cur_dict = {'dates' : list(data.index), 'ticker': list(data.values)}
        
        return_dict[ticker] = cur_dict

    return return_dict



def get_mutual_fund_data(schwab_mf_tickers: list, schwab_etf_tickers: list):
    """
    Read in excel files that have list of 
    each companies most popular/best performing mutual funds 
    ** Decided to just hardcode in the tickers **

    return data for each ticker
    """
    vanguard_dict = handle_tickers_retrieve_data(
       [ 
        # 'VTAPX', 
        'VGPMX',
        'VHCIX',
        'VITAX',
        'VIPSX',
        'VMCTX',
        'VRGWX',
        'VMGAX',
        'VMSXX',
        'VINIX']
    )
    print("\n after one vanguard dict was handled \n")

    fidelity_dict = handle_tickers_retrieve_data(
        ['FDCPX'
        ,'FSIPX'
        ,'FYHTX'
        ,'FSHCX'
        ,'FACVX'
        ,'FWATX'
        ,'FITLX'
        ,'FFIDX'
        ,'FLCEX'
        ,'FLGEX']
    )

    print("\n after second vanguard dict was handled \n")

    schwab_dict = handle_tickers_retrieve_data(
        schwab_mf_tickers + schwab_etf_tickers
    )


    

    return vanguard_dict, fidelity_dict, schwab_dict


if __name__ == '__main__':
    print("cur running \n")
    print(get_mutual_fund_data(['SWPPX'],['SWPPX']))