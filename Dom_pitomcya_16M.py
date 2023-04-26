class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age


#ниже код с импортированным файлом

from modul_16M import Cat

cat_1 = Cat("Барон", "Мальчик", "2 года")
print(f'имя: {cat_1.name}, пол: {cat_1.gender}, возраст: {cat_1.age}')

cat_2 = Cat("Сэм", "Мальчик", "2 года")
print(f'имя: {cat_2.name}, пол: {cat_2.gender}, возраст: {cat_2.age}')