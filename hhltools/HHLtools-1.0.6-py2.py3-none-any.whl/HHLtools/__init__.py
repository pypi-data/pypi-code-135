import datetime

def fibonacci(n):
    if n < 1 or int(n) != n:
        return "error, n should be a positive number which is greater than 1"
    if n < 3:
        return 1
    a, b = 1, 1

    for i in range(2, n):
        a = a + b if i % 2 == 0 else a
        b = a + b if i % 2 == 1 else b
    return a if a > b else b


def fibonacci_list(n):
    if n < 1 or int(n) != n:
        return "error, n should be a positive number which is greater than 1"
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    list = [1, 1]
    for i in range(2, n):
        list.append(list[i - 2] + list[i - 1])
    return list


class Queue():
    def __init__(self):
        self.__queue = []

    def show(self):
        print(self.__queue)

    def push(self, content):
        try:
            self.__queue.append(content)
        except:
            print('invalid input')

    def pop(self):
        try:
            del self.__queue[0]
        except IndexError:
            print('warning : no value in the queue,try add(content) to add one')


class Stack():
    def __init__(self):
        self.__stack = []

    def show(self):
        print(self.__stack)

    def push(self, content):
        try:
            self.__stack.insert(0, content)
        except:
            print('invalid input')

    def pop(self):
        try:
            del self.__stack[0]
        except IndexError:
            print('warning : no value in the stack,try add(content) to add one')




class Hmath():
    class Functions():
        def __init__(self, expression: str, variable: str):
            self.__expression = expression
            self.__var = variable

        def evaluate(self, value: (int, float)):
            expression = self.__expression.replace(self.__var, str(value))
            return eval(expression)

        def gradient(self, accuracy, value: (int, float)):
            x1 = value
            x2 = value + 10 ** -accuracy
            y1 = self.evaluate(x1)
            y2 = self.evaluate(x2)
            res = (y2 - y1) / (x2 - x1)
            return round(res, 1) if res - int(res) > 0.999 or res - int(res) < 0.001 else round(res, 3)



