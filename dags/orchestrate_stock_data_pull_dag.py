# from jobs.extract import scrape_stock_tickers
import sys
# local path
sys.path.append("/home/oxbigsnowman/Airflow_On_Micro-k8s_Cluster/jobs/extract/")
sys.path.append("/home/oxbigsnowman/Airflow_On_Micro-k8s_Cluster/jobs/transform/")
# docker path
sys.path.append("/opt/airflow/jobs/extract/")
sys.path.append("/opt/airflow/jobs/transform/")
from extract_stock_data import scrape_stock_tickers
from transform_stock_data import get_ticker_data
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models.xcom import XCom
from airflow.decorators import dag, task
import pendulum
from datetime import timedelta
from typing import Dict, Tuple


@dag(
    dag_id='orchestrate_stock_data_pull_dag',
    schedule_interval="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['orchestrate_stock_data_pull_dag']
)
def orchestrate_stock_data_pull_dag():

    @task
    def extract_stock_tickers() -> Dict:
        """
        Extracts dictionaries of stock market tickers and serializes them
        """

        res_dict = scrape_stock_tickers()

        return res_dict

    @task
    def retrieve_ticker_data(stock_ticker_dict: Dict) -> Dict:
        """
        Retrieves historical price data for a dictionary of tickers
        """
        s_and_p_dict, nasdaq_dict, djia_dict = get_ticker_data(stock_ticker_dict)

        dict_of_dict = {'s_and_p': s_and_p_dict,
                        'nasdaq': nasdaq_dict,
                        'djia': djia_dict}

        return dict_of_dict


    stock_tickers_dict = extract_stock_tickers()
    res_dict = retrieve_ticker_data(stock_tickers_dict)



extract_stock_data_task = orchestrate_stock_data_pull_dag()