import sys

from tokenizer import tokenize_equation
from parser_eq import parse_equation
from solver import reduce_equation, format_equation, solve_equation

from math_functions import OPERATORS

def infer(ast):
    if ast.operator is True:
        res_left = infer(ast.left)
        res_right = infer(ast.right)
        print("operand left right:", res_left, res_right)
        print("result: ", OPERATORS[ast.value](res_left, res_right))
        return OPERATORS[ast.value](res_left, res_right)
    return float(ast.value)

def main():
    tokens = tokenize_equation(sys.argv[1])
    try:
        root_of_equation = parse_equation(tokens)
        root_of_equation, degree_equation = reduce_equation(root_of_equation)
    except Exception as error:
        sys.exit(str(error))
    print(infer(root_of_equation.left))
    print("Reduced form: %s" %format_equation(root_of_equation))
    print("Polynomial degree: %d" %degree_equation)
    if degree_equation > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve")
    else:
        solve_equation(root_of_equation, degree_equation)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.exit("too much arguments")
    if len(sys.argv) < 2:
        sys.exit("missing equation to solve")
    main()