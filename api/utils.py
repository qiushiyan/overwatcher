from pandas import DataFrame
import functools


def first_dict_key(x: dict) -> str:
    """get first key of a dictionary"""
    return list(x.keys())[0]


def first_dict_value(x: dict):
    """get first value of a dictionary"""
    fk = first_dict_key(x)
    return x.get(fk)


def safely(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            return e
    return wrapper


def gen_response(res):
    if isinstance(res, DataFrame):
        if not res.empty:
            return {
                "error_code": 1,
                "msg": "success",
                "data": res.to_json(orient="records"),
                "error": ""
            }
        else:
            return {
                "error_code": 1,
                "msg": "success (empty df)",
                "data": "",
                "error": ""
            }
    else:
        return {
            "error_code": -1,
            "msg": "error",
            "data": "",
            "error": res
        }
