def addition(num, result):
	result += num
	print(result)
	return result


def subtraction(num_1, num_2):
	print(num_1, '-', num_2, '=', num_1 - num_2)

def multiplication(num_1, num_2):
	print(num_1, '*', num_2, '=', num_1 * num_2)

def division(num_1, num_2):
	print(num_1, '/', num_2, '=', num_1 / num_2)

def menu(num_1, num_2):
	num_1 = int(input('Введите первое число: '))
	num_2 = int(input('Введите второе число: '))

#def operands(operands):

operation = str(input('Введите операцию: '))
operands = int(input('Сколько операндов: '))
string = ''
result = 0

num = int(input('Введите операнд ' + str(1) + ':'))
result = addition(num, result)
string += str(result)

for i in range(2, operands + 1):
	num = int(input('Введите операнд ' + str(i) + ':'))
	if operation == '+':
		string += '+'
		result = addition(num, result)
		string += str(result)
		print(result)
print(str(num) + '+' + string, '=', str(result))



