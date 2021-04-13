# Калькулятор
# Разин ПИ223 
while True:
    try:
        a = int(input("Введите первое число:"))
        repeat = "q"
        while repeat == "q":
            try:
                operation, b = input("Введите операцию(+, -, *, /, **, =); НАЖМИТЕ ПРОБЕЛ; Введите чиcло:").split()
                b = int(b)
                if  operation == "+":
                    a = a + b
                elif operation == "-":
                    a = a - b
                elif operation == "*":
                    a = a * b
                elif operation == "/":
                    if b != 0:
                        a = a / b
                    else:
                        print("Ошибка! На ноль делить нельзя!")
                        print("Попробуйте еще раз...")
                elif operation == "**":
                    a = a ** b
                else:
                    print("Ошибка! Такой операции нет!")
                    print("Попробуйте еще раз...")
            except:
                print("Ваш ответ:",a)
                repeat = input("Введите: q - продолжить или любую другую кнопку, чтоб начать сначала:")
    except ValueError:
        print("Ошибка! Вы ввели не чиcло!")
        print("Попробуйте еще раз...")





