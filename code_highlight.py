
import difflib
from colorama import Style, Fore


def deleteValues(lst,value):
    while value in lst:
        lst.remove(value)
    return lst



class HighLight:
    """выделение исправленных строк кода определенным цветом"""
    def __init__(self,new_code:str,old_code:str):
        self.new_code =new_code
        self.old_code = old_code
        self.list_new_strings = deleteValues(new_code.split('\n'),'')
        self.list_old_strings = deleteValues(old_code.split('\n'),'')
        self.similarity = len(self.list_old_strings) == len(self.list_new_strings)

    def check_similarity(self):
        deletes_values = 0
        copi_lst = self.list_new_strings.copy()
        d = {}
        for str_code in range(len(self.list_old_strings)):
            dict_ratio = {}
            for str_code_new in range(len(copi_lst)):
                ratio = difflib.SequenceMatcher(None, self.list_old_strings[str_code],
                                                copi_lst[str_code_new]).ratio()
                if ratio == 1:
                    copi_lst.pop(str_code_new)
                    break

                elif ratio >= 0.7:
                    dict_ratio[ratio] = str_code_new
                    d[str_code] = self.list_old_strings[str_code],copi_lst[str_code_new]
                    copi_lst.pop(str_code_new)
                    deletes_values += 1
                    break
        return d

    def highlight(self):
        """функция по выделению исправленных фрагментов кода"""
        change_need_strings = self.check_similarity()
        string = ''''''
        for i in range(len(self.list_new_strings)):

            if i in change_need_strings.keys():
                if change_need_strings[i][0] in change_need_strings[i][1]:
                    a = change_need_strings[i][1].replace(change_need_strings[i][0], '$')
                    if a[0] == '$':
                        string += Style.RESET_ALL + change_need_strings[i][0] + \
                                  Fore.RED + a.replace('$', '') + '\n'
                    elif a[-1] == '$':
                        string += Fore.RED + a.replace('$', '') + Style.RESET_ALL + \
                                  change_need_strings[i][0] + '\n'
                    else:
                        b = a.split('$')
                        string += Fore.RED + b[0] + Style.RESET_ALL + \
                                  change_need_strings[i][0] + Fore.RED + b[1] + '\n'
                else:
                    if difflib.SequenceMatcher(None, change_need_strings[i][0], self.
                            list_new_strings[i]).ratio() <= 0.7:
                        string += Fore.RED + self.list_new_strings[i] + '\n'
                    else:
                        adding = ''''''
                        split1 = self.list_new_strings[i].split(' ')
                        split2 = change_need_strings[i][0].split(' ')
                        for i in split1:
                            if i == '':
                                adding += Style.RESET_ALL + ' '
                                continue
                            if i in split2:
                                adding += Style.RESET_ALL + i + ' '
                            else:
                                adding += Fore.RED + i + ' '
                        string += adding + '\n'
            else:
                string += Style.RESET_ALL + self.list_new_strings[i] + '\n'
            # print(string)
        return string


def Indicate_On_Space_Change(obj:HighLight):
    '''функция по выделению фрагментов кода, где были допущены ошибки
    и указанию дополнительного количества пробелов'''
    change_need_strings = obj.check_similarity()
    string = ''''''
    for i in range(len(obj.list_new_strings)):

        if i in change_need_strings.keys():
            if change_need_strings[i][0] in change_need_strings[i][1]:
                a = change_need_strings[i][1].replace(change_need_strings[i][0],'$')
                if a[0] == '$':
                    string += Style.RESET_ALL + change_need_strings[i][0] + \
                              Fore.RED + a.replace('$','') + '\n'
                elif a[-1] == '$':
                    string += Fore.RED + a.replace('$','') + Style.RESET_ALL +\
                              change_need_strings[i][0] + '\n'
                else:
                    b = a.split('$')
                    string += Fore.RED + b[0] + Style.RESET_ALL + \
                              change_need_strings[i][0] + Fore.RED + b[1]  + '\n'
            else:
                if difflib.SequenceMatcher(None, change_need_strings[i][0],obj.
                        list_new_strings[i]).ratio() <= 0.7:
                    string += Fore.RED + obj.list_new_strings[i] + '\n'
                else:
                    adding = ''''''
                    split1 = obj.list_new_strings[i].split(' ')
                    split2 = change_need_strings[i][0].split(' ')
                    count_space1 = 0
                    count_space2 = 0
                    space_message = ''
                    for i in split1:
                        if i == '':
                            count_space1 += 1
                        else:
                            break

                    for i in split2:
                        if i == '':
                            count_space2 += 1
                        else:
                            break
                    if count_space1 == count_space2:
                        pass
                    elif count_space1 - count_space2 > 0:
                        space_message = f'# количество пробелов увелечено на {count_space1 - count_space2}'
                    elif count_space1 - count_space2 < 0:
                        space_message = f'# количество пробелов уменьшено на {count_space2 - count_space1}'
                    for i in split1:
                        if i == '':
                            adding += Style.RESET_ALL + ' '
                            continue
                        if i in split2:
                            adding += Style.RESET_ALL + i + ' '
                        else:
                            adding += Fore.RED + i + ' '

                    string += adding + Fore.BLUE + space_message  + '\n'
        else:
            string += Style.RESET_ALL + obj.list_new_strings[i] + '\n'
        # print(string)
    return string


