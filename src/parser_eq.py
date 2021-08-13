from typing import Tuple

class AST():

    def __init__(self, value: str, operator: bool, left: 'AST', right: 'AST'):
        self.value = value
        self.operator = operator
        self.left = left
        self.right = right

def operand_is_valid(to_check: str) -> bool:
    if to_check.isdigit() is True:
        return True
    if len(to_check) == 1 and to_check[0] == 'X':
        return True
    tmp = to_check.split('.')
    if len(tmp) == 2 and tmp[0].isdigit() is True and tmp[1].isdigit() is True:
        return True
    return False

def parse_operand(tokens: list) -> Tuple[AST, int]:
    if not tokens:
        raise Exception("Unexcepted EOF")
    if tokens[0] == '-' and len(tokens) >= 2 and operand_is_valid(tokens[1]) is True:
        return AST(tokens[0] + tokens[1], False, None, None), 2
    if operand_is_valid(tokens[0]) is False:
        raise Exception("Invalid char in token %s" %tokens[0])
    return AST(tokens[0], False, None, None), 1

def parse_power(tokens: list) -> Tuple[AST, int]:
    left, current = parse_operand(tokens)
    if current < len(tokens) and tokens[current] == '^':
        right, current_r = parse_power(tokens[current + 1: ])
        return AST(tokens[current], True, left, right), current + current_r + 1
    return left, current

def parse_div(tokens: list) -> Tuple[AST, int]:
    left, current = parse_power(tokens)
    if current < len(tokens) and tokens[current] == '/':
        right, current_r = parse_div(tokens[current + 1: ])
        return AST(tokens[current], True, left, right), current + current_r + 1
    return left, current

def parse_dot(tokens: list) -> Tuple[AST, int]:
    left, current = parse_div(tokens)
    if current < len(tokens) and tokens[current] == '*':
        right, current_r = parse_dot(tokens[current + 1: ])
        return AST(tokens[current], True, left, right), current + current_r + 1
    return left, current

def parse_sub(tokens: list) -> Tuple[AST, int]:
    left, current = parse_dot(tokens)
    if current < len(tokens) and tokens[current] == '-':
        right, current_r = parse_sub(tokens[current + 1: ])
        right.value = '-' + right.value
        return AST(tokens[current], True, left, right), current + current_r + 1
    return left, current

def parse_add(tokens: list) -> Tuple[AST, int]:
    left, current = parse_sub(tokens)
    if current < len(tokens) and tokens[current] == '+':
        right, current_r = parse_add(tokens[current + 1: ])
        return AST(tokens[current], True, left, right), current + current_r + 1
    return left, current

def parse_equation(tokens: list) -> AST:
    left_part, current = parse_add(tokens)
    if current >= len(tokens):
        raise Exception("Missing assignation and right part of equation")
    if tokens[current] != '=':
        raise Exception("Unexcepted char before assignation, must be assignation but got %s" %tokens[current])
    if current + 1 > len(tokens):
        raise Exception("Missing right part of equation")
    right_part, current_r = parse_add(tokens[current + 1: ])
    if current + current_r + 1 < len(tokens):
        raise Exception("Unexcepted char at end of equation %s" %tokens[current + current_r + 1])
    return AST(tokens[current], True, left_part, right_part)