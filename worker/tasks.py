from .worker import celery
from celery import Task

import time


class BaseTask(Task):
    """ Genereric base task for all tasks. """

class CustombaseTask(Task):
    """ Base tasks for use inside of tasks. """
    _custom = None

    @property
    def custom(self):
        if self._custom is None:
            self._custom = "This is custom property."
        return self._custom


@celery.task(base=CustombaseTask)
def custom_base():
    return custom_base.custom

@celery.task(name='test')
def test_task(complexity):
    time.sleep(int(complexity))
    return {"Success":complexity}
