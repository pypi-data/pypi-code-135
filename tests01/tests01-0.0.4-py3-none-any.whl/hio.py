def hinput(a = '',type = "str"):
    l = input(f'{a}').split()
    if type == 'str':
        return l
    elif type == 'int':
        for i in range(len(l)):
            l[i] = int(l[i])
        return l
    elif type == 'float':
        for i in range(len(l)):
            l[i] = float(l[i])
        return l
