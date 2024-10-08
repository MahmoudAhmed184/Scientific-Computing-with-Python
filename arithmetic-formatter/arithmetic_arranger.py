ALLOWED_ARITHMETIC_OPERATORS = ['+', '-']
MAXIMUM_NUMBER_OF_PROBLEMS = 5
MAXIMUM_DIGITS_PER_OPERAND = 4
SEPARATOR_BETWEEN_PROBLEMS = ' ' * 4
# Define the width adjustment to account for the operator and the separation space
WIDTH_ADJUSTMENT = 2


def validate_problem(problem: str):
    first_operand, operator, second_operand = problem.split(' ')

    if operator not in ALLOWED_ARITHMETIC_OPERATORS:
        return "Error: Operator must be '+' or '-'."

    if not (first_operand.isdigit() and second_operand.isdigit()):
        return "Error: Numbers must only contain digits."

    if len(first_operand) > MAXIMUM_DIGITS_PER_OPERAND or len(second_operand) > MAXIMUM_DIGITS_PER_OPERAND:
        return "Error: Numbers cannot be more than four digits."

    return None


def calculate_result(first_operand: str, operator: str, second_operand: str) -> str:
    match operator:
        case '+':
            return str(int(first_operand) + int(second_operand))
        case '-':
            return str(int(first_operand) - int(second_operand))


def arithmetic_arranger(problems: list[str], results=False):
    if len(problems) > MAXIMUM_NUMBER_OF_PROBLEMS:
        return "Error: Too many problems."

    lines = ['', '', '', '']

    for problem in problems:
        first_operand, operator, second_operand = problem.split(' ')

        error_message = validate_problem(problem)
        if error_message:
            return error_message

        result = calculate_result(first_operand, operator, second_operand)

        width = max(len(first_operand), len(second_operand)) + WIDTH_ADJUSTMENT

        lines[0] += first_operand.rjust(width) + SEPARATOR_BETWEEN_PROBLEMS
        lines[1] += operator + second_operand.rjust(width - len(operator)) + SEPARATOR_BETWEEN_PROBLEMS
        lines[2] += '-' * width + SEPARATOR_BETWEEN_PROBLEMS
        lines[3] += result.rjust(width) + SEPARATOR_BETWEEN_PROBLEMS

    arranged_problems = '\n'.join(line.rstrip() for line in lines[:-1])

    if results:
        arranged_problems += '\n' + lines[3].rstrip()

    return arranged_problems