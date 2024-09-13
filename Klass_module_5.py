class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()
    def say_info(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age}")

    def birthday(self):
        self.age += 1
        print(f"У меня день рождения, мне теперь {self.age}")

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age


    def __eq__(self, other):
        return self.age == other.age

    def __eq__(self, other):
        return self.name == other.age and self.age == other.age

    def __del__(self):
        print(f"{self.name} ушел")




den = Human('Денис', 22)
max = Human('Максим', 22)
max.name = 'Денис'
print(max == den)
# jur = Human("Юргис", 18)
# print('Дену 22, Максу еще 22',den == max)

max.birthday()      # False, разные имена
# jur.birthday()
# print('Дену 22, Максу уже 23',den < max)
# print('Дену 22, Максу уже 23',den > max)
# print('Дену 22, Максу уже 23', den == max)
#
# print(max == den)  # False, разные имена и возраст
