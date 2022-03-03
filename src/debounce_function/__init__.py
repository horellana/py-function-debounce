import time
import functools

def now():
    return int(time.time()) * 1000


def debounce(ms_delay):
    def wrap(f):
        callback = f
        t = now()
        d = ms_delay

        @functools.wraps(callback)
        def wrapper(*args, **kwargs):
            nonlocal t
            nonlocal d
            nonlocal callback

            dt = now() - t

            if dt >= d:
                t = now()
                callback(*args, **kwargs)

        return wrapper

    return wrap 


def async_debounce(ms_delay):
    def wrap(f):
        callback = f
        t = None
        d = ms_delay

        @functools.wraps(callback)
        async def wrapper(*args, **kwargs):
            nonlocal t
            nonlocal d
            nonlocal callback
            
            dt = now() - t

            if dt >= d:
                t = now()
                await callback(*args, **kwargs)

        return wrapper

    return wrap 
