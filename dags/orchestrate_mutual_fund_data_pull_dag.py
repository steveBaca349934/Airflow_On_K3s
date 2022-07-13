import sys
# local path
sys.path.append("/home/oxbigsnowman/Airflow_On_Micro-k8s_Cluster/jobs/extract/")
sys.path.append("/home/oxbigsnowman/Airflow_On_Micro-k8s_Cluster/jobs/transform/")
# docker path
sys.path.append("/opt/airflow/jobs/extract/")
sys.path.append("/opt/airflow/jobs/transform/")
from extract_mutual_fund_data import scrape_schwab_mf_tickers, scrape_schwab_etf_tickers

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



    mf_ticks = extract_mf_tickers()
    etf_ticks = extract_etf_tickers()

mf_dag = orchestrate_mutual_fund_data_pull_dag()