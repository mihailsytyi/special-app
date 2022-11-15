
def additions(N):
	string = ''
	result = 0
	for count in range(1, N + 1):
		print('Введите операнд', count, ': ', end = '')
		x = int(input())
		result += x
		if count == N:
			string += str(x)
			break
		string += str(x) + '+'
	print(string + '=', end = '')
	print(result)

def subtraction(N):
	string = ''
	result = 0
	for count in range(1, N + 1):
		print('Введите операнд', count, ': ', end='')
		x = int(input())
		if count == 1:
			result += x
			string += str(x) + '-'
		elif count == N:
			string += str(x)
			result -= x
			break
		else:
			result -= x
			string += str(x) + '-'
	print(string + '=', end='')
	print(result)

def division(N):
	string = ''
	result = 0
	for count in range(1, N + 1):
		print('Введите операнд', count, ': ', end='')
		x = int(input())
		if count == 1:
			result += x
			string += str(x) + '/'
		elif count == N:
			string += str(x)
			result /= x
			break
		else:
			result /= x
			string += str(x) + '/'
	print(string + '=', end='')
	print(round(result, 2))

def multiplication(N):
	string = ''
	result = 1
	for count in range(1, N + 1):
		print('Введите операнд', count, ': ', end='')
		x = int(input())
		result *= x
		if count == N:
			string += str(x)
			break
		string += str(x) + '*'
	print(string + '=', end='')
	print(float(round(result, 3)))
while True:

	question = input('Выберите операцию: ')

	if question == '+':
		N = int(input('Количество операндов: '))
		additions(N)
	elif question == '-':
		N = int(input('Количество операндов: '))
		subtraction(N)
	elif question == '*':
		N = int(input('Количество операндов: '))
		multiplication(N)
	elif question == '/':
		N = int(input('Количество операндов: '))
		division(N)
	else:
		print('Нет такой операции')

