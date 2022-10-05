def infix_to_polish(list_of_tokens):
    special_tokens = '+-()'
    stack_of_operators = []
    output_list = []
    while list_of_tokens:
        item = list_of_tokens.pop(0)
        if item not in special_tokens:
            output_list.append(item)
        else:
            if item == '(':
                stack_of_operators.append(item)
            if item == ')':
                while stack_of_operators[-1] != '(':
                    output_list.append(stack_of_operators.pop(-1))
            if item in '+-':
                while stack_of_operators and stack_of_operators[-1] != '(':
                    output_list.append(stack_of_operators.pop(-1))
                stack_of_operators.append(item)
    while stack_of_operators:
        item = stack_of_operators.pop(-1)
        if item not in '()':
            output_list.append(item)
    return output_list


def evaluate_polish(list_of_tokens, operators: dict):
    for i, j in enumerate(list_of_tokens):
        if j not in operators:
            list_of_tokens[i] = operators['translate'](j)
    proxy = []
    while list_of_tokens:
        proxy.append(list_of_tokens.pop(-1))
    list_of_tokens = proxy
    objects = []
    while list_of_tokens:
        __obj = list_of_tokens.pop(-1)
        if __obj not in operators:
            objects.append(__obj)
        else:
            second = objects.pop(-1)
            first = objects.pop(-1)
            list_of_tokens.append(operators[__obj](first, second))
    return objects[0]


def test():
    def id(__obj):
        return __obj

    def add(a, b):
        return int(a) + int(b)

    def sub(a, b):
        return int(a) - int(b)

    INFIX = '(5+6+3-2)-9'
    print(list(INFIX))
    print(infix_to_polish(list(INFIX)))
    POLISH = infix_to_polish(list(INFIX))
    print(evaluate_polish(POLISH, {'translate': id, '+': add, '-': sub}))


if __name__ == '__main__':
    test()




