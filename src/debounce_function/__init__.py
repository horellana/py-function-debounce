import time
import asyncio
import functools


def debounce(ms_delay):
    def get_ts():
        return time.monotonic_ns() / 1_000_000

    def should_callback(last_called, delay, now):
        dt = now - last_called

        if dt >= delay:
            return True
        else:
            return False

    def wrap(f):
        callback = f
        last_called = get_ts()
        delay = ms_delay

        if asyncio.iscoroutinefunction(f):
            @functools.wraps(callback)
            async def wrapped(*args, **kwargs):
                nonlocal last_called
                nonlocal delay
                nonlocal callback

                now = get_ts()

                if should_callback(last_called, delay, now):
                    last_called = now
                    return await callback(*args, *kwargs)
        else:
            @functools.wraps(callback)
            def wrapped(*args, **kwargs):
                nonlocal last_called
                nonlocal delay
                nonlocal callback

                now = get_ts()

                if should_callback(last_called, delay, now):
                    last_called = now
                    return callback(*args, *kwargs)

        return wrapped
    return wrap


async_debounce = debounce
