class Archive:
    """Takes one int and one str attribute, and saves it in string_arch and nums_arch lists
    which sptriped later and placed in objects"""

    string_arch = list()
    nums_arch = list()
    _counter = 0

    def get_name (self):
        """returns name of  variable linked to its object of class"""
        for i, j in globals().items():
            if j is self:
                return i

    def __new__ (cls, string, num):
        """creates and remembers all created class objects data
        _counter need for creating correct list of history for class objects"""

        cls.string_arch.append(string)
        cls.nums_arch.append(num)
        cls._counter += 1
        return super().__new__(cls)

    def __init__ (self, string, num):
        self.string_arch = self.string_arch[:self._counter - 1]
        self.nums_arch = self.nums_arch[:self._counter - 1]
        self.num = num
        self.string = string

    def __str__ (self):
        variable_name = self.get_name()
        return f'{variable_name}: num: {self.num}\n\
   string: {self.string}\n\
   history of strings: {self.string_arch}\n\
   history of nums: {self.nums_arch}\n'

    def __repr__ (self):
        return f'Archive(string = {self.string}, num = {self.num})\n'


a = Archive('ololo', 2)
print(a)
print(repr(a))
del a

try:
    print(a)
except Exception:
    print('CANT FIND a, it has been delited')

b = Archive('bububub', 3)
print(b)
print(repr(b))
del b

c = Archive('HEEERE WE ARE, BORN TO BE FREE', 5)
print(c)
print(repr(c))
del c

d = Archive('Shampo', 12)
print(d)
print(repr(d))
del d

print(help(Archive))
