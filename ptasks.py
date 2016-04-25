# tijdelijke file om te kijken hoe celery werkt.

from celery import Celery

app = Celery('ptasks', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y



