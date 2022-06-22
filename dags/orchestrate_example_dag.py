import pendulum

@dag(start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
     schedule_interval="@daily", catchup=False)
def generate_dag():
    op = EmptyOperator(task_id="task")

dag = generate_dag()