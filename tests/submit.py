from redis import Redis
from choreo.multirq import Queue
import time
import threading
import random


def main():
    queue = Queue(connection=Redis())
    result = queue.enqueue('tasks.sleepy', args=(random.randint(20, 20),), timeout=10)

    tic = time.time()
    while result.get_status() not in ('finished', 'failed'):
        time.sleep(1)
        toc = time.time()
        duration = round(toc - tic, 2)
        print(f'Waiting for result, for {duration}')

    print(f'Got result: {result.return_value}')


for _ in range(1):
    time.sleep(1)
    threading.Thread(target=main).start()
