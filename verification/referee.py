"""
CheckiOReferee is a base referee for checking you code.
    arguments:
        tests -- the dict contains tests in the specific structure.
            You can find an example in tests.py.
        cover_code -- is a wrapper for the user function and additional operations before give data
            in the user function. You can use some predefined codes from checkio.referee.cover_codes
        checker -- is replacement for the default checking of an user function result. If given, then
            instead simple "==" will be using the checker function which return tuple with result
            (false or true) and some additional info (some message).
            You can use some predefined codes from checkio.referee.checkers
        add_allowed_modules -- additional module which will be allowed for your task.
        add_close_builtins -- some closed builtin words, as example, if you want, you can close "eval"
        remove_allowed_modules -- close standard library modules, as example "math"

checkio.referee.checkers
    checkers.float_comparison -- Checking function fabric for check result with float numbers.
        Syntax: checkers.float_comparison(digits) -- where "digits" is a quantity of significant
            digits after coma.

checkio.referee.cover_codes
    cover_codes.unwrap_args -- Your "input" from test can be given as a list. if you want unwrap this
        before user function calling, then using this function. For example: if your test's input
        is [2, 2] and you use this cover_code, then user function will be called as checkio(2, 2)
    cover_codes.unwrap_kwargs -- the same as unwrap_kwargs, but unwrap dict.

"""

from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from golf import CheckiORefereeGolf
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

INSPECTOR_ERROR = "Your code maybe returns correct answers, but it contains forbidden characters."
INSPECTOR_OK = "OK"


def inspector(code, _):
    for c in 'eiou*/.':
        if c in code:
            return False, INSPECTOR_ERROR
    return True, INSPECTOR_OK


api.add_listener(
    ON_CONNECT,
    CheckiORefereeGolf(
        tests=TESTS,
        max_length=300,
        inspector=inspector,
        cover_code={
            'python-27': None,
            'python-3': None
        },
        function_name="davasaan"
    ).on_ready)
