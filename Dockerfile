FROM apache/airflow:slim-2.3.0-python3.7

COPY requirements.txt .
COPY dags $AIRFLOW_HOME/dags
RUN true
COPY jobs $AIRFLOW_HOME/jobs
RUN true
# AIRFLOW_HOME is /opt/airflow

RUN pip install --upgrade pip \
 && pip install -r requirements.txt



