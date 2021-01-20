def name(arg1, arg2):
    print(f"Привет! меня зовут, {arg1} приятно познокомится ")
    print(f"Меня {arg2} очень приятно!")

name('Мекан', 'Ровшен')


def cracker(arg1, arg2):
    print(f"Сегодня я купил {arg1} чипсов!")
    print(f"Надеюсь мне сегодня хватит {arg2} пачек чипсов")

cracker(50, 10)

def print_name(arg1):
    n1 = input("Приветствую! \nКак вас зовут?")
    #n1 = print_name(arg1)
    print(f"Очень приятно! {arg1}")

print_name('Мекан')

