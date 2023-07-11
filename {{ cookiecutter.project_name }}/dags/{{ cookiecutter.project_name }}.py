from airflow import DAG
from conveyor.factories import ConveyorDbtTaskFactory
from conveyor.secrets import AWSParameterStoreValue
from {{ cookiecutter.project_name }}.alerting import slack_failed_dag_notification
from datetime import datetime, timedelta


default_args = {
    "owner": "Conveyor",
    "depends_on_past": False,
    "start_date": datetime(year=2023, month=7, day=11),
    "email": [],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


dag = DAG(
    "{{ cookiecutter.project_name }}", default_args=default_args, schedule_interval="@daily", max_active_runs=1, on_failure_callback=slack_failed_dag_notification
)
factory = ConveyorDbtTaskFactory(task_aws_role="conveyor-samples",
                                 task_arguments=["--no-use-colors", "{command}", "--profiles-dir", ".", "--select", "{model}",],
                                 task_env_vars={"POSTGRES_PASSWORD": AWSParameterStoreValue(name="/conveyor-samples/postgres_password")})
factory.add_tasks_to_dag(dag=dag)
