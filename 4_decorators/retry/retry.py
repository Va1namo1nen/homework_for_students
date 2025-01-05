from time import sleep
from datetime import datetime, timedelta
from typing import Callable

def retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exception)] = (Exception,)):
    if count < 1:
        raise ValueError(f"Число попыток должно быть >= 1, получено: {count}")

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < count:
                try:
                    return func(*args, **kwargs)
                except handled_exceptions as e:
                    attempts += 1
                    if attempts >= count:
                        raise e
                    sleep(delay.total_seconds())
        return wrapper
    return decorator

