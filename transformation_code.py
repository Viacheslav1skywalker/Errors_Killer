"""Модуль преобразования кода для более удобного исправления
ошибок"""



class Transformation:
    def __init__(self,code):
        self.code = code

    def delete_comments(self):
        """Удаление всех строк комментариев в коде"""
        string = ''''''
        for i in self.code.split('\n'):
            if '#' not in i:
                string += i + '\n'
        return string



