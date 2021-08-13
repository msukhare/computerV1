from typing import Tuple
from parser_eq import AST

def reduce_equation(root_eq: AST) -> Tuple[AST, int]:
    return root_eq, 0

def format_equation(root_eq: AST) -> str:
    left_part, right_part = "", ""
    if root_eq.left is not None:
        left_part = format_equation(root_eq.left)
    if root_eq.right is not None:
        right_part = format_equation(root_eq.right)
    midle = " {c} ".format(c=root_eq.value) if root_eq.operator is True and\
        root_eq.value != '^' else root_eq.value
    return left_part + midle + right_part

def solve_equation(root_eq: AST, degree: int) -> None:
    pass