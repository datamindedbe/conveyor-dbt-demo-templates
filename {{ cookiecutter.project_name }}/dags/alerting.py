from airflow.models import Variable
from airflow.providers.slack.operators.slack_webhook import SlackWebhookHook


def slack_failed_dag_notification(context):
    environment = Variable.get("environment", "unknown")
    slack_msg = """
            :red_circle: DAG `{dag}` in environment `{env}` failed. 
            *DAG*: {dag}
            *Environment*: {env}
            *Execution Time*: {exec_date}
            *Reason*: {reason}
            *Url*: https://app.conveyordata.com/environments/{env}/airflow/tree?dag_id={dag}
            """.format(
            dag=context.get('dag_run').dag_id,
            env=environment,
            exec_date=context.get('execution_date'),
            reason=context.get('reason'),
        )
    hook = SlackWebhookHook(
        http_conn_id="slack_webhook",
        message=slack_msg,
    )
    hook.execute()