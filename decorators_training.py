# author:               Michał Rybiński
# nickname:             rybinskm
# date of create:       11-08-2022
# date of last edit:    12-08-2022

from datetime import datetime


def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        logged_time = start_time.strftime('%H:%M:%S')
        print(f'Start time of function: {logged_time}')
        func(*args, **kwargs)
        end_time = datetime.now()
        logged_time = end_time.strftime('%H:%M:%S')
        print(f'End time of function: {logged_time}')
    return wrapper


@time_execution
def showtext(text):
    print(f'It me, computer, I show you your text {text}.')