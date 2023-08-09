import time
from getpass import getuser


class My_str(str):
    """Takes str and adds time and username
    Can be used as normal string f.e. split(), concat etc."""

    def __new__ (cls, my_str):
        instance = super().__new__(cls, my_str)
        instance.name = getuser()
        instance.time = time.time()
        return instance


s = My_str('olo lo')
print(s, s.name, s.time)
print(s.split())
print(help(My_str))
