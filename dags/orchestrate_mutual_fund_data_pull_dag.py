import sys
# local path
sys.path.append("/home/oxbigsnowman/Airflow_On_Micro-k8s_Cluster/jobs/extract/")
sys.path.append("/home/oxbigsnowman/Airflow_On_Micro-k8s_Cluster/jobs/transform/")
# docker path
sys.path.append("/opt/airflow/jobs/extract/")
sys.path.append("/opt/airflow/jobs/transform/")
from extract_mutual_fund_data import scrape_schwab_mf_tickers, scrape_schwab_etf_tickers
from transform_mutual_fund_data import get_mutual_fund_data

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models.xcom import XCom
from airflow.decorators import dag, task
import pendulum
from datetime import timedelta
from typing import Dict, Tuple, List


@dag(
    dag_id='orchestrate_mutual_fund_data_pull_dag',
    schedule_interval="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['orchestrate_mutual_fund_data_pull_dag']
)
def orchestrate_mutual_fund_data_pull_dag():

    @task
    def extract_mf_tickers() -> List[str]:
        
        mf_ticks = scrape_schwab_mf_tickers()

        return mf_ticks

    @task
    def extract_etf_tickers() -> List[str]:

        etf_ticks = scrape_schwab_etf_tickers()

        return etf_ticks

    @task
    def retrieve_mutual_fund_data(schwab_mf_ticks: list, schwab_etf_ticks: list):

        vanguard_dict, fidelity_dict, schwab_dict = get_mutual_fund_data(schwab_mf_ticks, schwab_etf_ticks)

        dict_of_dict = {'vanguard': vanguard_dict,
                        'fidelity': fidelity_dict,
                        'schwab': schwab_dict}

        return dict_of_dict


    mf_ticks = extract_mf_tickers()
    etf_ticks = extract_etf_tickers()
    res_dict = retrieve_mutual_fund_data(mf_ticks, etf_ticks)

mf_dag = orchestrate_mutual_fund_data_pull_dag()