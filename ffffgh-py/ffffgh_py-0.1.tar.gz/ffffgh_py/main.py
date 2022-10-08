def factorial(n):
	factorial = 1
	for i in range(2, n+1):
	    factorial *= i
	return factorial


def arms(n):
	s = str(n)
	l = len(s)
	suma = 0
	for i in range(l):
		suma += int(s[i]) ** l
	if n == suma:
		return True
	else:
		return False


def friendly_numbers(a, b):
	suma = 0

	for i in range(1, a):
		if a % i == 0:
			suma += i

	sumb = 0

	for i in range(1, b):
		if b % i == 0:
			sumb += i

	if suma == b and sumb == a:
		return True
	else:
		return False


def abc(n):
	return n == factorial(int(str(n)[0])) + factorial(int(str(n)[1])) + factorial(int(str(n)[2]))



def help():
	print('help() - вывести подсказки по функциям.\nfactorial() - вывести факториал числа.\nfriendly_numbers() - проверить являются ли числа дружественными.\nabc() - abc = a! + b! + c!\nprime_number() - проверка числа простое ли оно.')


def prime_number(number):
	if number == 1:
		return False
	elif number == 2:
		return True
	elif number <= 0:
		return False
	else:
		for i in range(2, number):
			i = int(i)
			if number % i == 0:
				return False
			else:
				return True
