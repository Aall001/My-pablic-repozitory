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
    def get_quest(self):
        return f'{self.name} {self.surname}, г.{self.town}'

client_1 = Client( "Илья", "Иванов", "Москва", 50)
client_2 = Client( "Максим", "Петров", "Москва", 40)
client_3 = Client( "Антон", "Смирнов", "Белово", 100)

list_client = [client_1, client_2, client_3]
for x in list_client:
    print(x.get_quest())