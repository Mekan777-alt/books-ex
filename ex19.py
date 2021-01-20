def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"У нас есть {cheese_count} сырков!")
    print(f"У нас есть {boxes_of_crackers} пачек чипсов!")
    print(f"Этого достаточно для вечиринки")
    print("Погнали!\n")
# Создаем функсию и придаем ему переменные,
print("Мы можем непосредственно передать число функсии:")
cheese_and_crackers(20, 30)
# Тут с созданой функсии в скобках придаем аргументы переменной
print("ИЛИ, мы можем использовать переменные из нашего ссенария:")
amount_of_cheese = 10
amount_of_crackers = 50
#
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# Тут мы добаляем альтернативы в функсии

print("Мы даже можем вичислять внутри фунсии")
cheese_and_crackers(10 + 20, 5 + 6)
# Так же мы подсоединяем
print("И обьединять переменные с вычислением")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#