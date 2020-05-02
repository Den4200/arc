from functools import wraps
from threading import Thread
from typing import Callable


def threaded(func: Callable) -> Callable:
    """
    A decorator that runs a function on
    a separate thread.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()

    return wrapper
