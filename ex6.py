types_of_people = 10
x = f'Существует {types_of_people} типов людей.'
# Создаем переменую. f = format, вне скобки а так же понимаем что внутри скобок вставляется значение переменой
binary = 'Python'
do_not = 'Нет'
y = f'Те, кто понимает {binary} и те, кто - {do_not}.'
# Так же создаем переменные и в том же духе вставляем через f 
print(x)
print(y)
# Принтуем все выше
print(f'Я сказал: {x}')
print(f'А еще я сказал: {y}')

hilarious = False
joke_evalution = 'Разве это не смешно?! {}'

print(joke_evalution.format(hilarious))

w = 'Это часть строки слева...'
e = 'а это справа.'

print(w + e)
# ТУт так же через + соединяем строки

