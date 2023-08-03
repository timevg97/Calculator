def calculator():
    print("Введите математическое выражение, которое хотите вычислить.")
    print("Введите help - для справки, end - для завершения программы.")
    valid_characters = [chr(37), chr(40), chr(41), chr(42), chr(43), ' '] + list(map(chr, range(45, 58)))

    def help_info():
        print(
            "Выражение не должно содержать буквы и спецсимволы."
            "\nДробные числа должны разделяться символом точка."
            "\nДля возведения в степень используйте **"
            "\nДля целочисленного деления используйте //"
            "\nЧтобы узнать остаток от деления используйте %"
            f"\nСписок допустимых значений для ввода: {valid_characters}"
        )

    def checking_correctness(check_expression):
        global symbol
        last_symbol = None

        for symbol in expression:
            if symbol not in valid_characters:  # проверка на допустимые значения
                raise ValueError

            if symbol in ["+", "-"] and last_symbol in ["+", "-"]:  # проверка на повторяющиеся знаки + и -
                raise SyntaxError

            last_symbol = symbol

    def transform(exp: str):
        if exp.count("(") != exp.count(")"):  # проверка на закрытие скобок
            raise SyntaxError

        if exp.find("(") == -1:
            return exp
        else:
            first_part = exp[0:exp.rfind("(")] + str(eval(exp[exp.rfind("(") + 1: exp.find(")", exp.rfind("("))]))
            second_part = str(eval(exp[exp.rfind("(") + 1: exp.find(")", exp.rfind("("))]))
            third_part = exp[exp.find(")", exp.rfind("(")) + 1:]
            exp = first_part + second_part + third_part
            return transform(exp)

    while True:
        try:

            expression = input("> ")
            expression.replace(" ", '')
            if expression.lower() == 'end':
                print("Завершение программы!")
                break
            elif expression.lower() == 'help':
                help_info()
                continue

            checking_correctness(expression)
            transform(expression)

            print(f"Результат: {round(eval(expression), 5)}")

        except(ZeroDivisionError):
            print("На ноль делить нельзя!")
        except(ValueError):
            print(f"Введен недопустимый символ: '{symbol}'.")
        except(SyntaxError):
            print("Введен некорректный оператор! Проверьте правильность ввода.")


calculator()
