cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
# Задаем нужные параметры для каждой переменной 
# Каждую переменную можно так же умножать и складывать вычитать и прибавлять
# Указыая переменную мы присваеваем знаком = в каждую переменную число, называется знаком присваение
# В итоге принтуем каждую строку
 

print("В наличии", cars, "автомобилей.")
print("И только", drivers, "водителей вышли на работу.")
print("Получается, что", cars_not_driven, "машины пустуют.")
print("Мы можем перевезти сегодня", carpool_capacity, "человек.")
print("Сегодня нужно отвезти", passengers, "человек.")
print("В каждой машине будет примерно", average_passengers_per_car, "человек.")

# при изменении 2 строки на селое число изменится 7 строка переменой carpool_capacity
# После кавычек обязательно нужно ставить запетую
# Также можно поменять имена переменных популярные i x и y
# если поменять переменные не вкоем случае нельзя забывать изменить имена переменных и скобках
# Конес кода!
#  