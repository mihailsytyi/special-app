def addition(num, result):
	result += num
	print(result)
	return result


def subtraction(num, result):
    result -= num
    print(result)
    return result

def multiplication(num, result):
    result *= num
    print(result)
    return result

def division(num, result):
    result /= num
    print(result)
    return result

def menu(num, result):
	num_1 = int(input('Введите первое число: '))
	num_2 = int(input('Введите второе число: '))

#def operands(operands):

operation = str(input('Введите операцию: '))
operands = int(input('Сколько операндов: '))
string = ''
result = 0

num = int(input('Введите операнд ' + str(1) + ':'))
if operation == '+':
	result = addition(num, result)
	string += str(result)
	for i in range(2, operands + 1):
		num = int(input('Введите операнд ' + str(i) + ':'))
		string += '+'
		result = addition(num, result)
		string += str(num)

elif operation == '-':
	result = subtraction(num, result)
	string += str(result)
	for i in range(2, operands + 1):
		num = int(input('Введите операнд ' + str(i) + ':'))
		string += '-'
		result = subtraction(num, result)
		string += str(num)
#


print(string + '=' + str(result))



