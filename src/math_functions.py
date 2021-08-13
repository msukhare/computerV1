
def add(first_operand: float, second_operand: float) -> float:
    return first_operand + second_operand

def sub(first_operand: float, second_operand: float) -> float:
    return first_operand - second_operand

def div(first_operand: float, second_operand: float) -> float:
    return first_operand / second_operand

def dot(first_operand: float, second_operand: float) -> float:
    return first_operand * second_operand

def power(first_operand: float, second_operand: float) -> float:
    return first_operand**second_operand

OPERATORS = {'+': add, '-': sub, '/': div, '*': dot, '^': power, '=': None}