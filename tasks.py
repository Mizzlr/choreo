import time
import random
from choreo.multirq.job import Job


def sleepy(duration):
    print('Starting sleepy task ...')
    countdown = duration
    if random.random() < 0.1:
        1 / 0

    while countdown > 0:
        print(f'\tCountdown: {countdown}')
        time.sleep(1)
        countdown -= 1
    print('Finished sleepy task!')


def universe():
    return 42


def square(x):
    time.sleep(2)
    return x[0] ** 2


def add(job_id):
    job1 = Job.fetch(job_id[0])
    job2 = Job.fetch(job_id[1])
    return job1.result + job2.result


def add1(job_id):
    job = Job.fetch(job_id[0])
    print(job)
    return job.result + 1
