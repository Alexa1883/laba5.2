class Animal:
    def speak(self):
        print("Животное издаёт звук")

class Dog(Animal):
    def speak(self):
        print("Гав-гав")

class Cat(Animal):
    def speak(self):
        print("Мяу-мяу")

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()
cat.speak()
