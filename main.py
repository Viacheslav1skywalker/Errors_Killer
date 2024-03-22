import analisesError
import fixError
import displayData




def main(code,deskription=False):
    '''Главная функция для отображения результатов текущей работы программы'''
    information = check_correcting(code,deskription)
    if len(information) == 1:
        print('все сведения об исправленных ошибках:')
        print(f'''Ваш код был проанализирован. Вот информация которую 
        вы должны изучить чтобы исправить ошибки:\n{information[0]}''')
        return information[0]
    print('Результаты исправления кода для подробного ознакомления:')
    print("""ЕСЛИ ХОТИТЕ СРАЗУ ПЕРЕЙТИ К ПРОСМОТРУ РЕЗУЛЬТАТА ТО ОН НАХОДИТСЯ
             В ФАЙЛЕ - correct_code.py""")
    for index,inf in enumerate(information[0:-1]):
        print()
        print(f'''на {index+1} этапе в коде была исправлена следующая 
            ошибка: {inf[1]}\n вот код с пояснением и исправлением данной ошибки:
            \n {inf[0]}''')
        print()
        print(f'конец пояснения и исправления {index+1} ошибки')
        print()
    displayData.FileDisplay().file_write(information[-1][-1]) if len(information[-1]) == 3 else None
    print(f'результат работы программы и конечный исправленный вариант:\n{information[-1][-1]}')
    return information[-1][-1]
    

# def check_not_first_launch(code,error_message):
#     NNWork = fixError.IdentificationProcessingFuncError().check_descriptive_errors(error_message)
#     if fixError.IdentificationProcessingFuncError().check_descriptive_errors(error_message):
#         return NNWork(code,error_message).fix()


# def display_code(displaying_data:str):
#     """Функция отображения соответствующего кода или информации"""
#
#     print()
#     print('результат ->')
#     print()
#     print(displaying_data)
#     print()
#     print('конец кода')
#     print()


def check_file_or_codestring(code):
    '''проверяем является ли строка путем к файлу или самим кодом'''
    if '.py' in code:
        return open(code,'r',encoding='utf-8').read()
    else:
        return code


def check_correcting(code,deskription):
    """Фунция которая будет запускать код и исправлять ошибки до тех пор
    пока ошибки не станут повторяться 3 раза или пока их вообще не будет"""
    checking_code = code
    current_error = None
    get_result = False
    for i in range(4):
        # print(f'{i} вызов')
        code = check_file_or_codestring(checking_code)
        analize = analisesError.AnlizesError()
        error_message = analize.analize(code)
        if error_message == current_error and error_message != None:
            # print('в коде возникает одна и та же ошибка')
            break
        current_error = error_message
        # print(error_message)
        if not error_message:
            # print('Код работает исправно, код завершен без ошибок')
            break
        processing_obj = fixError.IdentificationProcessingFuncError(). \
            return_processing_obj(code, error_message, deskription)
        if check_description_class(processing_obj):
            # print('обработка кода завершена с пояснением к ошибкам в коде')
            break
        checking_code = processing_obj.fix()[-1]
    # print()
    # print('обработка кода завершена вот итоговый код -----')
    # print()
    return fixError.inf


def check_description_class(processing_obj):
    """Проверка на то является ли класс тем классом который только объяяняет как
    исправить ошибки"""
    for i in fixError.explanation_error_classes:
        if processing_obj.__class__.__name__ == i:
            return True











