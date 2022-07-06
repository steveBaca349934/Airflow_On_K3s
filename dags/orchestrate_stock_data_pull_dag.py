# from jobs.extract import scrape_stock_tickers
import sys
# local path
sys.path.append("/home/oxbigsnowman/Airflow_On_Micro-k8s_Cluster/jobs/extract/")
# docker path
sys.path.append("/opt/airflow/jobs/extract/")
from extract_stock_data import scrape_stock_tickers
import extract_stock_data
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models.xcom import XCom
import pendulum
from datetime import timedelta


def extract_stock_tickers(**kwargs) -> None:
    """
    Extracts dictionaries of stock market tickers and serializes them
    """

    res_dict = scrape_stock_tickers()

    return res_dict



with DAG(

    dag_id='orchestrate_stock_data_pull_dag',
    schedule_interval="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['orchestrate_stock_data_pull_dag'],

) as dag:


    extract_stock_data_task = PythonOperator(
        task_id='extract_stock_tickers',
        python_callable=extract_stock_tickers,
        op_args=None,
        depends_on_past=False,
        dag=dag
    )

extract_stock_data_task