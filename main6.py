class Nikola:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.age = age
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"

    def __setattr__(self, attr, value):
        if attr not in self.__slots__:
            raise AttributeError(f"Нельзя добавлять новые атрибуты в класс Nikola!")
        object.__setattr__(self, attr, value)

    def __str__(self):
        return f"{self.name}, возраст: {self.age}"

person1 = Nikola("Николай", 20)
person2 = Nikola("Максим", 55)
person3 = Nikola("Андрей", 70)

print(person1)
print(person2)
print(person3)

try:
    person1.patronymic = "Иванович"
except AttributeError as e:
    print(e)


try:
    person1.greet = lambda: print("Привет!")
except AttributeError as e:
    print(e)
