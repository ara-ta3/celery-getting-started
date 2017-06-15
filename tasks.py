from celery import Celery, Task
import os

app = Celery('tasks', broker='redis://127.0.0.1:6379/0')

@app.task(bind=True)
def hoge(self):
    r = 0
    with open('count.txt', 'r') as f:
        x = f.read()
        r = int(x)
        r+=1
        print(r)
    with open('count.txt', 'w') as f:
        f.write(str(r))

    try:
        if r <= 2:
            raise KeyError()
    except KeyError, e:
        return self.retry(
            countdown=1,
            exc=e,
            max_retries=3,
        )
