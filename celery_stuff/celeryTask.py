from celery import Celery



app = Celery(
    'process_task',
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
)


@app.task
def process_task(path):
    from log_handler.LogHandler import LogHandler
    obj = LogHandler(path)
    obj.isfileOrDir()
    return 1




