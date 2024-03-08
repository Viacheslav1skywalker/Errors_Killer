'''Модуль по исправлению выявленных ошибок в коде'''


from abc import ABC
from abc import abstractmethod
from projectHalfStart import gigachat_responce
import re
import Errors

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

    def __init__(self,incorrect_code,error_message):
        self.incorrect_code = incorrect_code
        self.error_message = error_message

    # Отправляем запрос нейросети с соответсвующим сообщением и возвращаем результат её ответа
    def fix(self):
        prompt = f'''в данном коде возникает ошибка "{self.error_message}":\n{self.incorrect_code}\n\n
        исправь ошибки и выведт новый код с дополнительными сообщениями к каждой 
        ошибки,чтобы я больше не допускал такие ошибки'''
        responce = gigachat_responce.main(prompt)
        return self.handle_responce(responce)

    # обработка ответа от GIGACHAT
    def handle_responce(self,responce):
        print(responce)
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

class NeuralNetworkGigaChatExplanation(NeuralNetworkFixing):
    """исправление ошибок за счет пояснения к ним, которые не всегда грамотно могут быть исправлены с помощью
        простого предоставления нового кода,"""

    def __init__(self,incorrect_code,error_message):
        self.incorrect_code = incorrect_code
        self.error_message = error_message

    def fix(self):
        prompt = f'''в данном коде возникает ошибка "{self.error_message}":\n{self.incorrect_code}\n\n
        Объясни почему она может возникать и предложи варианты ее исправления и пришли исправленный код'''
        responce = gigachat_responce.main(prompt)
        return responce








class IndOutRange(AlgoritmFixing):
    '''реализауия пояснения к ошибке 'Index Out of Range' для более удобного исправления'''
    def __init__(self,code,error_message):
        self.code = code
        self.error_message = error_message

    def fix(self):

        print('длина списка ')



