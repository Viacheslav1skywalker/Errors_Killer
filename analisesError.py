'''моудль по анализу кода на ошибки'''


import fixError
from traceback import format_exc
import re
import black
import Errors
import  code_highlight

class AnlizesError:
    def analize(self,code:str):
        """функция которая возвращает или сообщение об ошибке или о том что ее нет"""
        self.check_code_strings(code)
        error_message = self.check_code_exceptions(code)
        if not error_message:
            print('код работает должным образом')
        else:
            return error_message

    def check_code_strings(self,code):
        """Функция, которая проверяет количество строк в запросе
        пользователя на то чтобы их было не больше 43"""
        code = code.split('\n')
        if len(code) <= 43:
            return len(code)
        else:
            code = list(filter(lambda a: a != '', code))
            if len(code) > 43:
                raise Errors.StringsCodeCountToMuch('Программа может обрабатывать коды с максимальным количестыом 43 строки кода')
            else:
                return len(code)
    def check_code_exceptions(self,code):
        try:
            exec(code)
            print('ваш код работает исправно')
            return None
        except Exception as ex:
            tb = format_exc()
            return str(tb)







