# 16.9.1./16.9.2
# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'
#
#     def get_area(self):
#         return self.width * self.height
#
# rect_1 = Rectangle(5, 10, 50, 100)
# print(rect_1)
# print(rect_1.get_area())

# 16.9.3./16.9.4.
class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'''"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб"'''

    def get_clients(self):
        return f'''"{self.name} {self.surname}. {self.city}."'''

client_1 = Client('Иван', 'Петров', 'Москва', '50')
client_2 = Client('Сергей', 'Глухов', 'Саратов', '500')
client_3 = Client('Марина', 'Павлова', 'Казань', '100')
client_4 = Client('Антон', 'Зыков', 'Ульяновск', '70')
print(client_1)
print()
print(client_1.get_clients(), client_2.get_clients(), client_3.get_clients(), client_4.get_clients())

# Правильный ответ для д/з 16.9.4:
# client_list = [client_1, client_2, client_3, client_4]
# for client in client_list:
#     print(client.get_clients())