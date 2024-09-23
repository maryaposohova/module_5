
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)



    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)



    # def go_to(self, new_floor):
    #     for i in range(1, new_floor+1):
    #         new_floor = i
    #         print(f"{new_floor}")
    #         if new_floor > self.number_of_floors or new_floor < 1:
    #             print('Такого этажа не существует')
    #             return
    #


    # def __len__(self):
    #     return self.number_of_floors

    # def __str__(self):
    #     return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    # def __eq__(self, other):
    #     print('other', isinstance(other, House))
    #     print('self', isinstance(self, House))
    #     return self.number_of_floors == other.number_of_floors
    #
    # def __lt__(self, other):
    #     return self.number_of_floors < other.number_of_floors
    #
    # def __le__(self, other):
    #     return self.number_of_floors <= other.number_of_floors
    #
    #
    # def __gt__(self, other):
    #     return self.number_of_floors > other.number_of_floors
    #
    #
    # def __ge__(self, other):
    #     return self.number_of_floors >= other.number_of_floors
    #
    #
    # def __ne__(self, other):
    #     return self.number_of_floors != other.number_of_floors
    #
    # def __add__(self, value):
    #     return House(self.name, self.number_of_floors + value)
    #
    # def __radd__(self, value):
    #     return House(self.name, value + self.number_of_floors)
    #
    # def __iadd__(self, value):
    #     self.number_of_floors = self.number_of_floors + value
    #     return self

    def __del__(self):
        print(f'"{self.name} снесён, но он останется в истории"')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)



