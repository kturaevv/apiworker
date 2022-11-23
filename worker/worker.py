from celery import Celery

import os

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

celery = Celery(
    'tasks', 
    backend='rpc://', 
    broker=f'pyamqp://{RABBITMQ_HOST}:{RABBITMQ_PORT}',
    task_cls='worker.tasks:BaseTask'
    )
