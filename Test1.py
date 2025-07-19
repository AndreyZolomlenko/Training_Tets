
def main(input: str): #Реализация функции main()
    stroka = input.split() #Присвоение перменной stroka значения введенной строки поэлементно (.split())

    if len(stroka) != 3:  #Проверка количества эл-в строки: 2 операнда и 1 оператор
        raise Exception("Выражение не подходит под условие: 2 операнда, 1 оператор")

    oper1 = stroka[0] #Присвоение переменной oper1 значение первого элемента строки
    oper2 = stroka[2] #Присвоение переменной oper2 значение третьего элемента строки

    if oper1.isdigit() and oper2.isdigit(): #Проверка значение на целое число
        oper1 = int(oper1)
        oper2 = int(oper2)
    else:
        raise Exception("Операнды должны быть целыми числами от 1 до 10")

    if not (1 <= oper1 <= 10) or not (1 <= oper2 <= 10): #Проверка чисел на вхождение в диапазон от 1 до 10
        raise Exception("Неверно введены данные: числа должны быть в диапазоне от 1 до 10")

    oper = stroka[1]

    if oper == "+": #Проверка введенного операнда
        res = oper1 + oper2
    elif oper == "-":
        res = oper1 - oper2
    elif oper == "*":
        res = oper1 * oper2
    elif oper == "/":
        res = oper1 // oper2
    else:
        raise Exception("Операнд не совпадает с возможными: +, -, *, /")

    return str(res)

stroka = input("Введите выражение для вычисления: ") #Ввод выражения для вычисления
print(main(stroka))