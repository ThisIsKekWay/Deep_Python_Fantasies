# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.
import random


class Human:
    def __init__ (self, name, age):
        self.name = name
        self._age = age

    def birth_day (self):
        self._age += 1

    def __str__ (self):
        return f'Возраст человека с именем {self.name}: {self._age}'


# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

class Employee(Human):
    def acsess_counter (self, id):
        if id < 10:
            return id
        else:
            return id % 10 + self.acsess_counter(id // 10)

    def __init__ (self, name, age, id):
        super().__init__(name, age)
        self.id = id
        self.acsess = self.acsess_counter(id)

    def __str__ (self):
        return f"Имя: {self.name}\n" \
               f"Возраст: {self._age}\n" \
               f"id: {self.id}\n" \
               f"Уровень доступа: {self.acsess}"


e1 = Employee('jupe', 26, random.randint(100000, 999999))
print(e1)
