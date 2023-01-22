import time
import os


def log(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__.title().replace('_', ' ')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start
        unit = 's'
        if exec_time < 1:
            exec_time *= 1000
            unit = 'ms'
        USER = os.getenv('USER')
        with open('machine.log', 'a') as f:
            f.write(f'({USER})Running: {func_name:18} [ exec-time = {exec_time:.3f} {unit} ]\n')
        return result
    return wrapper
