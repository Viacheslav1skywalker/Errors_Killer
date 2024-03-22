'''Модуль по исправлению выявленных ошибок в коде'''


from abc import ABC
from abc import abstractmethod
import gigachat_responce
import re
import Errors

fixing_error_classes = ['NeuralNetworkFixingGIGACHAT',]
explanation_error_classes = ['NeuralNetworkGigaChatExplanation']
#массив информации о запросах к нейросетям
inf = []


class IdentificationProcessingFuncError:
    """Класс для выявляния класса который будет обрабатывать ошибку"""

    def __init__(self):
        # self.descriptive_errors:list = ['is not defined','No such file or directory']
        self.NeuralNetworkFixingGIGACHAT = NeuralNetworkFixingGIGACHAT
        self.NeuralNetworkGigaChatExplanation = NeuralNetworkGigaChatExplanation

    def return_processing_obj(self,code:str,error_message:str,deskription:bool):
        """функция которая выявляет какой экземпляр класса создать для того чтобы исправить ошибки"""
        # if self.check_descriptive_errors(error_message):
        #     return  self.NeuralNetworkGigaChatExplanation(code,error_message)
        if deskription:
            return self.NeuralNetworkGigaChatExplanation(code,error_message)
        else:
            return self.NeuralNetworkFixingGIGACHAT(code,error_message)

    # def check_descriptive_errors(self,error_message):
    #     for i in self.descriptive_errors:
    #         if i in error_message:
    #             return  self.NeuralNetworkGigaChatExplanation


class NeuralNetworkFixing(ABC):
    '''интерфейс для исправление ошибок которые легко могут быть исправлены с помощью нейросетей'''

    @abstractmethod
    def fix(self,*args,**kwargs):
        pass


class AlgoritmFixing(ABC):
    '''Интерфейс для исправления ошибок которые тяжело исправить с помощью нейросети,
    или не исправления, а пояснения к этим ошибкам'''

    @abstractmethod
    def fix(self):
        pass


class NeuralNetworkFixingGIGACHAT(NeuralNetworkFixing):
    """исправление ошибки в коде с помощью нейросети под названием GigaChat"""
    first_call = True
    def __init__(self,incorrect_code,error_message):
        if self.first_call:
            self.warning_message()
            self.first_call_change()
        self.incorrect_code = incorrect_code
        self.error_message = error_message
        self.check_length_code(incorrect_code)
    @classmethod
    def first_call_change(cls):
        cls.first_call = False
    @staticmethod
    def add_value_to_inf(value):
        inf.append(value)

    # Отправляем запрос нейросети с соответсвующим сообщением и возвращаем результат её ответа
    def fix(self):
        prompt = f'''в данном коде возникает ошибка "{self.error_message}":\n{self.incorrect_code}\n\n
        исправь ошибку а также исправь другие ошибки в коде если они есть'''
        responce = gigachat_responce.main(prompt)
        # print()
        # print('Целый ответ от нейросети с полезной информацией:')
        # print()
        # print(responce)
        # print('-------')
        # print('конец ответа')
        res_responce_with_handle = responce,self.error_message,self.handle_responce(responce)
        self.add_value_to_inf(res_responce_with_handle)
        return res_responce_with_handle

    # обработка ответа от GIGACHAT
    def handle_responce(self,responce):
        value = re.findall(r'```python[\w\W]+', responce, re.DOTALL)
        if len(value) == 0:
            raise Errors.GigaChatOutputNotCorrect ('Ошибка вывода данных')
        elif len(value) == 1:
            return self.transformation(value[0])
        else:
            string = ''''''
            for i in value:
                if 'python' in i:
                    string += i.replace('python','') + '\n'
            return self.transformation(string)

    # функция по обработке ответа до чистого представления в виде кода
    def transformation(self,text):
        list_code = text.split('```')
        result_string = ''''''
        for i in list_code:
            if 'python' in i:
                result_string += i.replace('python', '') + '\n'
        return result_string

    def check_length_code(self,code):
        if len([i for i in code.split('\n') if i != '']) >=43:
            raise Errors.StringsCodeCountToMuch('строк должно быть меньше 43')
        else:
            return True
    def warning_message(self):
        """Функция которая предоставляет описание используемой нейросети"""
        print('''WARNIHG: использование этой нейросети имеет следующие ограничения:\n
        1) Количество строк вышего кода может быть не больше 42;\n
        2) Старайтесь передавать в программу один блоко кода для
        лучших результатов\n''')

class NeuralNetworkGigaChatExplanation(NeuralNetworkFixing):
    """исправление ошибок за счет пояснения к ним, которые не всегда грамотно могут быть исправлены с помощью
        простого предоставления нового кода,"""

    def __init__(self,incorrect_code,error_message):
        self.incorrect_code = incorrect_code
        self.error_message = error_message

    @staticmethod
    def add_value_to_inf(value):
        inf.append(value)

    def fix(self):
        prompt = f'''в данном коде возникает ошибка "{self.error_message}":\n{self.incorrect_code}\n\n
        Объясни почему она может возникать и предложи варианты ее исправления и пришли исправленный код'''
        responce = gigachat_responce.main(prompt)
        self.add_value_to_inf((responce,self.error_message))
        return responce










class IndOutRange(AlgoritmFixing):
    '''реализауия пояснения к ошибке 'Index Out of Range' для более удобного исправления'''
    def __init__(self,code,error_message):
        self.code = code
        self.error_message = error_message

    def fix(self):

        print('длина списка ')



