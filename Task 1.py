class Tvaryna:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Тварина видає звук")


class Sobaka(Tvaryna):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print("Гав-гав!")


class Kit(Tvaryna):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("Мяу!")


if __name__ == "__main__":
    dog = Sobaka("Рекс", 3, "Вівчарка")
    cat = Kit("Мурчик", 2, "Рудий")

    print(f"Собака: {dog.name}, Вік: {dog.age} роки, Порода: {dog.breed}")
    dog.make_sound()

    print(f"Кіт: {cat.name}, Вік: {cat.age} роки, Колір: {cat.color}")
    cat.make_sound()