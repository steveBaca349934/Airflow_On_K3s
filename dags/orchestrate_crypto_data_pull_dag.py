import sys
# local path
sys.path.append("/home/oxbigsnowman/Airflow_On_Micro-k8s_Cluster/jobs/extract/")
sys.path.append("/home/oxbigsnowman/Airflow_On_Micro-k8s_Cluster/jobs/transform/")
# docker path
sys.path.append("/opt/airflow/jobs/extract/")
sys.path.append("/opt/airflow/jobs/transform/")
from extract_crypto_data import get_list_of_crypto_pairs
from transform_crypto_data import get_crypto_data

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models.xcom import XCom
from airflow.decorators import dag, task
import pendulum
from datetime import timedelta
from typing import Dict, Tuple, List

@dag(
    dag_id='orchestrate_crypto_data_pull_dag',
    schedule_interval="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['orchestrate_crypto_data_pull_dag']
)
def orchestrate_crypto_data_pull_dag():

    @task
    def extract_crypto_pairs() -> list:

        crypto_pairs = get_list_of_crypto_pairs()

        return crypto_pairs

    @task
    def extract_crypto_data(crypto_pairs: list) -> dict:

        res_dict = get_crypto_data(crypto_pairs)

        return res_dict    


    crypto_pairs = extract_crypto_pairs()
    res_dict = extract_crypto_data(crypto_pairs)
