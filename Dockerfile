FROM apache/airflow:latest-python3.7

COPY requirements.txt .
COPY dags $AIRFLOW_HOME/dags
RUN true
COPY jobs $AIRFLOW_HOME/jobs
RUN true
# AIRFLOW_HOME is /opt/airflow
# RUN sudo adduser airflow sudo
# RUN true

RUN pip install --upgrade pip \ 
&& pip install apache-airflow==2.3.2  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.7.txt" \
&& pip install -r requirements.txt