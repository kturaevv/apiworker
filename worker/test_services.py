from celery import Celery


def test_celery():
    celery = Celery(
        'tasks', 
        backend='rpc://', 
        broker=f'pyamqp://localhost:5672',
    )
    in_ = 1
    assert celery.send_task("test", (in_,)).get(timeout=5) == {"Success": in_}