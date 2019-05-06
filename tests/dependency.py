from redis import Redis
from choreo.multirq import Queue
import time

queue = Queue(connection=Redis())
job1 = queue.enqueue('tasks.square', (3,))
job2 = queue.enqueue('tasks.square', (4,))
job3 = queue.enqueue('tasks.add', (job1.id, job2.id), depends_on=[job1, job2])
job4 = queue.enqueue('tasks.add1', (job3.id,), depends_on=[job3])

while True:
    time.sleep(1)
    print(job4.result, job4.get_status())
    if job4.is_finished:
        break

# job1 = queue.enqueue('tasks.universe')
# job2 = queue.enqueue('tasks.add1', (job1.id,), depends_on=[job1])
#
# time.sleep(5)
# print(job1.result)
# print(job2.result)
