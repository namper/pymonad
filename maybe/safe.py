from maybe.maybe import Maybe
from functools import wraps

class NothingWasCaught(Exception):
    """ raised when nothing was returned by maybe instance"""
    pass


def safe(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except NothingWasCaught:
            res = Maybe()
        return res

    return wrapper


def do(mx: Maybe):
    if not mx:
        raise NothingWasCaught
    return mx.value


safe_return = Maybe
