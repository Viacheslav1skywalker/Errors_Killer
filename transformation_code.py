"""Модуль преобразования кода для более удобного исправления
ошибок"""

code ='''
def check_number(num):
if num % 2 == 0:
print("Число четное")
else:
print("Число нечетное")

num = 10
check_number(num)
#2)
def check_number(num)
    if num % 2 == 0
        print("Число четное")
    else
        print("Число нечетное")

num = 10
check_number(num)

#3)
def calculate_area():
    area = length * width
    print("Площадь прямоугольника:", area)

length = 10
calculate_area()


#4)
x = 5
if x = 5:
    print("x равно 5")

#5)
# Неправильное использование пробелов в имени переменной
my variable = "Hello"
print(my variable)

# Неправильное использование пробелов в имени функции
def my_function ():
    print("Привет")

my_function()
'''

class Transformation:
    def __init__(self,code):
        self.code = code

    def delete_comments(self):
        string = ''''''
        for i in self.code.split('\n'):
            if '#' not in i:
                string += i + '\n'
        return string



