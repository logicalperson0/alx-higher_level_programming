#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return (res)
    except (ZeroDivisionError) as z:
        print("Exception: {}".format(z), file=sys.stderr)
        return None
    except (IndexError) as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return None
