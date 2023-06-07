import re

while True:
    #получение строки с задачей
    math_str = input("Input your math task or 'exit':")
    if 'exit' in math_str.lower():
        break
    #разделение строки на список цифр и математических операторов
    variables = re.findall(r'\d+|\D', math_str)
    #получение списка математических операторов из введенной задачи
    math_operators = re.findall(r'\D', math_str)

    #Возвращает индекс математического оператора и сам оператор из списка, в первую очередь умножение и деление
    def operation_queue(math_s: list, operators: list) -> tuple[int, str]:
        if '*' in math_s:
            return math_s.index('*'), '*'
        if '/' in math_s:
            return math_s.index('/'), '/'
        if operators[0] in math_s:
            return math_s.index(operators[0]), operators[0]
    #запускается цикл, пока список с математическими операторами не опустеет
    while math_operators:
        index, operator = operation_queue(variables, math_operators)

        #в зависимости от оператора получает результат подсчета
        if operator == '*':
            var = float(variables[index - 1]) * float(variables[index + 1])
        if operator == '/':
            var = float(variables[index - 1]) / float(variables[index + 1])
        if operator == '-':
            var = float(variables[index - 1]) - float(variables[index + 1])
        if operator == '+':
            var = float(variables[index - 1]) + float(variables[index + 1])

        #удаляет из списка отработанные элементы и вставляет на их место результат подсчета
        del variables[index - 1:index + 2]
        variables.insert(index - 1, str(var))
        #удаляет из списка использованные оператор
        math_operators.remove(operator)

    print(variables[0])