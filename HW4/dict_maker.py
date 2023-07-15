import datetime


def dict_maker(**kwargs):
    res = dict()
    for k, v in kwargs.items():
        try:
            res[v] = k
        except Exception:
            res[str(v)] = k
    return res


print(dict_maker(name='Koha', current_date=str(datetime.datetime.now())))