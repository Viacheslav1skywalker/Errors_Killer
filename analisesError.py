'''моудль по анализу кода на ошибки'''
'''Эта надпись должна исчезнуть при переключение на дргуалоыав'''

import fixError
from traceback import format_exc
import re
import black
import Errors
import  code_highlight

DescriptiveError = ['No such file or directory']



def main(code,deskription=False,file_write = True):
    count = 0
    current_error = None
    code = code
    while True:
        count += 1
        if count == 13:
            print('превышение попыток исправления')
        code = identification_error(code,deskription,file_write)
        if code == 'Код работает исправно':
            print('код работает исправно')
            return code
        try:
            print(code)
            exec(open('correct_code.py','r').read())
            print('Код работает исправно')
        except Exception as ex:
            if current_error == str(ex):
                print('код совершает одну и ту же ошибку')
                return False
            current_error = str(ex)


def identification_error(code,deskription=False):
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
        print('ваш код работает исправно')
        return None
    except Exception as ex:
        tb = format_exc()
        text_code = NeuralNetwork(code,str(ex)).fix()
        if deskription != True:
            text_code = black.format_str(text_code, mode=black.FileMode())
        elif deskription == False:
            write_in_file(text_code)
        if not deskription:
            print()
            print('исправленный код с выделением')
            print(code_highlight.HighLight(text_code,code).highlight())
            print('конец выделенного кода')
            print()
        else:
            print()
            print('информация об исправленном коде')
            print(text_code)
            print('конец исправленного кода')
            print()
        print('RETURN CODE')
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




def write_in_file(text):
    """запись в файл исправленного кода"""
    with open('correct_code.py','w',encoding='utf-8') as file:
        file.write(text)
        file.flush()

def codeColor(new_code,old_code):
    """выделение цветом кода подверженного изменениям"""


