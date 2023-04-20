from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': days_ago(31),
    'email': ['example@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

#instantiates a directed acyclic graph
dag = DAG(
    'main-dag',
    default_args=default_args,
    description='Dag to download, preprocess and load SAR images.',
    schedule_interval=timedelta(days=30),
)

#Downloads the SAR image
download_images = BashOperator(
    task_id='download_images',
    bash_command='python3 /Users/annanya/airflow/scripts/download.py',
    dag=dag,
)

#Preprocesses the SAR image
process_images = BashOperator(
    task_id='process_images',
    bash_command='python3 /Users/annanya/airflow/scripts/preprocess.py',
    dag=dag,
)

#Load the SAR image
load_images = BashOperator(
    task_id='load_images',
    bash_command='python3 /Users/annanya/airflow/scripts/load.py',
    dag=dag,
)

download_images>>process_images>>load_images