from math_functions import OPERATORS

def check_if_operators(equation: str) -> str:
    for operator in OPERATORS:
        if equation.startswith(operator) is True:
            return operator
    return ""

def tokenize_equation(equation: str) -> list:
    tokens = []
    i = 0
    while (i < len(equation)):
        while (i < len(equation) and
            equation[i].isspace() is True and
            not check_if_operators(equation[i: ])):
            i += 1
        operator = check_if_operators(equation[i: ])
        if operator:
            tokens.append(operator)
            i += len(operator)
        else:
            tmp = ""
            while (i < len(equation) and
                equation[i].isspace() is False and
                not check_if_operators(equation[i: ])):
                tmp += equation[i]
                i += 1
            if tmp:
                tokens.append(tmp)
    return tokens