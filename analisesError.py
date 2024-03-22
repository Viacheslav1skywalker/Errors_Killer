'''моудль по анализу кода на ошибки'''
from traceback import format_exc
import Errors
import sys
import io

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
        """Проверяем работы пользовательского кода и если допускается ошибка то возвращаем
        сообщение об ошибке, в противном случае возвращаем сам код если ошибок не было"""
        try:
            # перенаправляем вывод чтобы не оторажать результат работы анализируемого кода
            # в консоли
            sys.stdout = io.StringIO()
            exec(code)
            sys.stdout = sys.__stdout__
            print('ваш код работает исправно')
            return None
        except Exception as ex:
            tb = format_exc()
            return str(tb)
        finally:
            sys.stdout = sys.__stdout__








