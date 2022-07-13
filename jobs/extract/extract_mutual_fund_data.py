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
import re


def scrape_schwab_etf_tickers() -> List[str]:
    """
    scrape schwab ETF and MF tickers
    off the world wide web
    
    return list of tickers
    """
    link = 'https://etfdb.com/etfs/issuers/charles-schwab/'

    # Grab data from website
    page_response = requests.get(link, timeout=1000)

    # Structure the raw data so that we can parse it
    soup = BeautifulSoup(page_response.content, features="lxml")

    
    etf_table = soup.find("table", {"id": "etfs"})

    rows = [] 
    # SCRAPE: Extract Table Contents
    for row in etf_table.tbody.findAll('tr'):
        rows.append ([col.text for col in row.findAll('td')])  # Gather all columns in the row

    ticker_list = [row[0] for row in rows]

    return ticker_list


def scrape_schwab_mf_tickers() -> List[str]:
    """
    scrape schwab ETF and MF tickers
    off the world wide web
    
    return list of tickers
    """
    link = 'https://mutualfunds.com/fund-company/charles-schwab-funds/'

    # Grab data from website
    page_response = requests.get(link, timeout=1000)

    # Structure the raw data so that we can parse it
    soup = BeautifulSoup(page_response.content, features="lxml")

    
    # mf_divs = soup.find("div", {"class": "mp-table-body-row-container"})

    ticker_list = []
    mf_p = soup.findAll("p", {"class": "m-table-body-subtext"})
    for row in mf_p:
        if row.span is not None:
            ticker_list.append(row.span.getText())
    

    
    return ticker_list
