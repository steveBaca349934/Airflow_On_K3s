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
    dag_id='orchestrate_mutual_fund_data_pull_dag',
    schedule_interval="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['orchestrate_mutual_fund_data_pull_dag']
)
def orchestrate_mutual_fund_data_pull_dag():
    
    pass