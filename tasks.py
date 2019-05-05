import time
import random


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
