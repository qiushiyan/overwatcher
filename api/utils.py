def first_dict_key(x: dict) -> str:
    """get first key of a dictionary"""
    return list(x.keys())[0]


def first_dict_value(x: dict):
    """get first value of a dictionary"""
    fk = first_dict_key(x)
    return x.get(fk)
