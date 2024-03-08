'''моудль по анализу кода на ошибки'''


import fixError
from traceback import format_exc
import re
import black
import Errors
def identification_error(code,deskription=False,file_write = True):
    '''функция по выявлению ошибки в коде и вызова соответствующей функции для ее исправления
    Параметр deskription при знчение True будет также выводить подробное описание, чтобы пользователь
    понял свою ошибку в коде, при значении file_write = True и deskription=False код будет записываться
    в файл'''
    if not check_code_strings(code):
        raise Errors.StringsCodeCountToMuch('Программа может обрабатывать коды с максимальным количестыом 43 строки кода')
    NeuralNetwork = fixError.NeuralNetworkFixingGIGACHAT
    if deskription:
        NeuralNetwork = fixError.NeuralNetworkGigaChatExplanation
    try:
        exec(code)
        return 'Код работает исправно'
    except Exception as ex:
        tb = format_exc()
        text_code = NeuralNetwork(code,str(ex)).fix()
        text_code = black.format_str(text_code, mode=black.FileMode())
        if file_write == True and deskription == False:
            write_in_file(text_code)
        return text_code


def check_code_strings(code):
    """Функция, которая проверяет количество строк в запросе
    пользователя на то чтобы их было не больше 43"""
    code = code.split('\n')
    if len(code) <= 43:
        return len(code)
    else:
        code = list(filter(lambda a: a != '', code))
        if len(code) > 43:
            return False
        else:
            return len(code)

def transformation_code(code,error_message):
    '''функция, которая преобразует код в удобный вид для последующего анализа и исправления ошибок,
    возвращаемым значением будет эта самая модель кода'''
    model_code = code.split('\n')
    error_string = re.findall(r'line\s*\d*', error_message)[-1]
    count_error_string = int(re.findall(r'\d+', error_string)[0])
    return {'code':model_code,'line_error':count_error_string-1}


def write_in_file(text):
    """запись в файл исправленного кода"""
    with open('correct_code.py','w',encoding='utf-8') as file:
        file.write(text)
        file.flush()


print(identification_error('''
            def find_sum_of_list(lst
return sum(lst
# Пример использования
my_list == 1, 2, 3, 4, 5]
print("Сумма всех элементов списка:" find_sum_oflist(my_list
                            def find_average(lst)
                return sum(lst) =/ len(lst) if len(lst) => 0 else 0
# Пример использования
my_list = [1, 2, 3, 4, 5
print("Среднее значение списка:" find_average(my_list)
            def is_prime(num
    i num <= 2:
return False
            for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
return False
    return True
# Пример использования
        number = 17
if is_prime(number)
    print(number, "является простым числом.")
else
    print(number "не является простым числом.")
        def factorial(num)
    if num= 0:
    return 1
else
    return num * factorial(num - 1)
    # Пример использования
number = 5
            print("Факториал числа", number, "равен:", factorial(number))
                def sort_list(lst)
    return sortedlst)
# Пример использования

class Student
    def __init_(self name, age)
        self.name == name
        self.age == age
    def greeting(self)
                return f"Приве, меня зовут {self.name} и мне {self.age} лет."
student1 = Student("Иван" 20)
print(student1.greeting()
'''))



