# Исправленный код


def find_sum_of_list(lst):
    return sum(lst)


# Пример использования
my_list = [1, 2, 3, 4, 5]
print("Сумма всех элементов списка:", find_sum_of_list(my_list))


def find_average(lst):
    return sum(lst) / len(lst) if len(lst) > 0 else 0


# Пример использования
my_list = [1, 2, 3, 4, 5]
print("Среднее значение списка:", find_average(my_list))


def is_prime(num):
    if num <= 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Пример использования
number = 17
if is_prime(number):
    print(number, "является простым числом.")
else:
    print(number, "не является простым числом.")


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# Пример использования
number = 5
print("Факториал числа", number, "равен:", factorial(number))


def sort_list(lst):
    return sorted(lst)


# Пример использования


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Приве, меня зовут {self.name} и мне {self.age} лет."


student1 = Student("Иван", 20)
print(student1.greeting())
