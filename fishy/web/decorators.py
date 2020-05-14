import logging
import traceback
import typing
from functools import wraps

if typing.TYPE_CHECKING:
        from fishy.web.web import get_session


def uses_session(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if get_session(args[0]) is None:
            logging.error("Couldn't create a session")
            return None
        else:
            return f(*args, **kwargs)

    return wrapper


def fallback(default):
    def inner(f):
        # noinspection PyBroadException
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception:
                traceback.print_exc()
                return default
        return wrapper

    return inner
