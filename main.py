import sys
import string
import random

# Метод подсчета повторов символов
def ReplaceCount(_str, _fs, _sn):

    # Массив с количеством повторов
    result = [0,0]
    for c in _str:
        # Если символ соответствует первому символу
        if(c == _fs):
            result[0] += 1
        # Если символ соответствует второму символу
        if(c == _sn):
            result[1] += 1

    return result


# Метод замены символов в строке
def ReplaceCharInString(_str, _fs, _sn):

    # Строка - результат
    result = ''
    for c in _str:
        # Если символ цифра => замена на первый символ
        # Иначе => замена на второй
        if(c.isdigit()):
            result += _fs
        else:
            result += _sn

    return result


# Метод генерирует строку из случайных символов длиной N
def StringGenerator(N):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))


# Метод проверки ввода на число
def SetNValue():
    while True:
        try:
            N = int(input('Введите число N: '))
        except ValueError:
            print('Введите число')
        else:
            break
    return N


def main():

    # Присвоение значения переменной N
    N = SetNValue()

    # Генерация строки из N символов и ее вывод
    _string = StringGenerator(N)
    print('Сгенерированная строка: ' + _string, end='\n\n')

    print('Ввод пары символов для замены (будут использованы первые введенные символы)')
    # Ввод первого символа на замену
    _first = input('Введите символ для замены всех букв в строке: ')[0]

    # Ввод второго символа на замену
    _second = input('Введите символ для замены всех цифр в строке: ')[0]

    # Замена символов в строке и ее вывод
    _string = ReplaceCharInString(_string, _first, _second)
    print('\nСтрока после обработки: ' + _string, end='\n\n')

    # Подсчет количества замен и вывод результатов
    result = ReplaceCount(_string, _first, _second)
    print('Количество повторов: ')
    print(_first + ' = ' + str(result[0]))
    print(_second + ' = ' + str(result[1]))


if __name__ == '__main__':
    main()