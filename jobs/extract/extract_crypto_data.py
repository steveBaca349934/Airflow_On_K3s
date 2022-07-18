from Historic_Crypto import Cryptocurrencies, HistoricalData
from datetime import datetime, date
import sys
import copy
from datetime import datetime, timedelta


def get_list_of_crypto_pairs()->list:
    """
    Utilize the "Historic_Crypto" library to pull 
    a list of Crypto 'pairs'.
    
    returns list of crypto pairs
    """
    crypto_pairs_df = Cryptocurrencies().find_crypto_pairs()

    # only pulling pairs that are USD
    return [pair for pair in crypto_pairs_df['id'] if pair.split("-")[1] == 'USD']



