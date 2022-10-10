# Tool to merge complex dictionaries
def Merge(in1Dict, in2Dict):
    """
    Сливать словарь in2Dict в in1Dict. В случае конфликта вывести исключение

    :param in1Dict: Исходный словарь. В него будет производится запись. Ссылка на него будет активна
    :param in2Dict: Изменяющий словарь. Новые данные, которые будут скопированы в in1Dict
    :return: Обновленный словарь in1Dict
    """
    lPathList=None
    if lPathList is None: lPathList = []
    for lKeyStr in in2Dict:
        if lKeyStr in in1Dict:
            if isinstance(in1Dict[lKeyStr], dict) and isinstance(in2Dict[lKeyStr], dict):
                Merge(in1Dict[lKeyStr], in2Dict[lKeyStr])
            elif in1Dict[lKeyStr] == in2Dict[lKeyStr]:
                pass  # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(lPathList + [str(lKeyStr)]))
        else:
            in1Dict[lKeyStr] = in2Dict[lKeyStr]
    return in1Dict

# Tool to merge complex dictionaries - no exceptions, just overwrite dict 2 in dict 1
def MergeNoException(in1Dict, in2Dict):
    """
    Сливать словарь in2Dict в in1Dict. В случае конфликта перезаписать на значение из in2Dict

    :param in1Dict: Исходный словарь. В него будет производится запись. Ссылка на него будет активна
    :param in2Dict: Изменяющий словарь. Новые данные, которые будут скопированы в in1Dict
    :return: Обновленный словарь in1Dict
    """
    lPathList=None
    if lPathList is None: lPathList = []
    for lKeyStr in in2Dict:
        if lKeyStr in in1Dict:
            if isinstance(in1Dict[lKeyStr], dict) and isinstance(in2Dict[lKeyStr], dict):
                MergeNoException(in1Dict[lKeyStr], in2Dict[lKeyStr])
            else:
                in1Dict[lKeyStr] = in2Dict[lKeyStr]
        else:
            in1Dict[lKeyStr] = in2Dict[lKeyStr]
    return in1Dict
