rec = Rectangle(5, 10, 50, 100)
print(rec.__str__())
print(rec.rec_area())

class Client:
    def __init__(self, name, surname, town, balance):
        self.name = name
        self.surname = surname
        self.town = town
        self.balance = balance

    def __str__(self):
        return f'''"{self.name} {self.surname}. {self.town}. Баланс: {self.balance} руб."'''

client_1 = Client('Иван','Петров','Москва',50)
print(client_1) 