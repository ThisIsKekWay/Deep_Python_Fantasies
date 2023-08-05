class Animal:
    def __int__ (self, name, color):
        self.name = name
        self.color = color

    def get_sound (self):
        return self.sound


class Fish(Animal):
    sound = 'Буль буль'

    def __init__ (self, name, color, length):
        super().__init__()
        self.length = length



class Horse(Animal):
    sound = 'Игого'

    def __init__ (self, name, color, length, height):
        super().__init__()
        self.height = height
        self.length = length



class Cat(Animal):
    sound = 'МАО'

    def __init__ (self, name, color, length, height):
        super().__init__()
        self.height = height
        self.length = length


class FactoryAnimal:
    def __init__(self, name_of_class):
        self.name_of_class = name_of_class

    def get_new_animal(self, *args):
        return self.name_of_class(*args)

cat_factory = FactoryAnimal(Cat)
c1 = cat_factory.get_new_animal('Кузя', 'Черный', 0.5, 0.3)
print(f'Котик говорит {c1.get_sound()}')

fish_factory = FactoryAnimal(Fish)
f1 = fish_factory.get_new_animal('Щука', 'Рыбный', 1)
print(f'Рыбка говорит {f1.get_sound()}')

horse_factory = FactoryAnimal(Horse)
h1 = horse_factory.get_new_animal('Буян', 'Вороной', 2.5, 2.2)
print(f'Лошадка говорит {h1.get_sound()}')
