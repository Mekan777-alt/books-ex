from sys import argv
# Импортируем модуль argv путем import
script, user_name = 'argv','Мекан'
prompt = '> '
# Выполняю команду script = argv. user_name = Мекан, Сколько слева аргументов столько и справа должно быть
# Все путем подстоновки через запетую в ковычках. 
print(f"Привет, {user_name}, я - сценарий {script}.")
print("Я хочу задать тебе несколько вопросов.")
print(f"Я тебе нравлюсь, {user_name}?")
likes = input(prompt)
# Тут все понятно вроде, через f строку подстовляем переменные.
print(f"Где ты живешь, {user_name}?")
lives = input(prompt)

print(f"На каком компютере ты работаешь?")
computer = input(prompt)

print(f"""
Итак, ты ответил {likes} на вопрос, нравлюсь ли я тебе.
Ты живешь {lives}. Не представляю где это.
И у тебя есть компютер {computer}. Прекрасно!
""")
