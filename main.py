import analisesError
import fixError
import displayData


def main(code,deskription=False):
    '''Функция которая управляет логикой работы программы'''
    result = check_correcting(code,deskription)
    if result[-1] == 'only_code':
        displayData.FileDisplay().file_write(result[0])
        return result[0]
    elif result[-1] == 'explain':
        return result[0]

    

def check_not_first_launch(code,error_message):
    NNWork = fixError.IdentificationProcessingFuncError().check_descriptive_errors(error_message)
    if fixError.IdentificationProcessingFuncError().check_descriptive_errors(error_message):
        return NNWork(code,error_message).fix()


def display_code(displaying_data:str):
    """Функция отображения соответствующего кода или информации"""

    print()
    print('результат ->')
    print()
    print(displaying_data)
    print()
    print('конец кода')
    print()


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
    for i in range(4):
        print(f'{i} вызов')
        code = check_file_or_codestring(checking_code)
        analize = analisesError.AnlizesError()
        error_message = analize.analize(code)
        print(error_message)
        if not error_message:
            print('Код работает исправно, код завершен без ошибок')
            return code,'only_code'
        processing_obj = fixError.IdentificationProcessingFuncError(). \
            return_processing_obj(code, error_message, deskription)
        if check_description_class(processing_obj):
            print('обработка кода завершена с пояснением к ошибкам в коде')
            return processing_obj.fix(),'explain'
        checking_code = processing_obj.fix()
        if error_message == current_error:
            break
        current_error = error_message
    print()
    print('обработка кода завершена вот итоговый код -----')
    print()
    return checking_code,'only_code'


def check_description_class(processing_obj):
    """Проверка на то является ли класс тем классом который только объяяняет как
    исправить ошибки"""
    for i in fixError.explanation_error_classes:
        if processing_obj.__class__.__name__ == i:
            return True












