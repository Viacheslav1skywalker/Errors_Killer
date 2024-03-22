from main import main

test_code = '''


# Неправильное использование пробелов в имени функции
def my_function ():
    print("Привет")

my_function()

#6)
my_list = [1, 2, 3, 4, 5]
print(my_list[10])  # Попытка обратиться к индексу 10, который выходит за пределы списка

#7)
import mat  # Неправильное имя модуля math

#8)
def greet(name):
    print(f"Hello, {name}!")

# Передано недостаточное количество аргументов
greet()



def add(a, b):
    return a + b

# Неправильное использование имени функции
result = add(3, 5)  # Используется неправильное имя функции "add" вместо "sum"

#9)

# Попытка открыть несуществующий файл для чтения
try:
    with open("несуществующий_файл.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"Ошибка: {e}")

#10)
# Ошибка из-за непонимания правил области видимости
def outer_function():
    x = 10

    def inner_function():
        # Пытаемся изменить значение переменной x, которая находится во внешней функции
        x += 5
        print(f"Внутри внутренней функции: {x}")

    inner_function()
    print(f"Внутри внешней функции: {x}")


outer_function()


'''

main(test_code)

