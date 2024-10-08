def arithmetic_arranger(problems, results=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = second_line = third_line = fourth_line = ""
    for problem in problems:
        first_operand, operator, second_operand = problem.split(" ")

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            result = str(int(first_operand) + int(second_operand))
        else:
            result = str(int(first_operand) - int(second_operand))

        width = max(len(first_operand), len(second_operand)) + 2
        first_line += " " * (width - len(first_operand)) + first_operand + "    "
        second_line += (
            operator + " " * (width - len(second_operand) - 1) + second_operand + "    "
        )
        third_line += "-" * width + "    "
        fourth_line += " " * (width - len(result)) + result + "    "

    arranged_problems = (
        first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + third_line.rstrip()
    )

    if results:
        arranged_problems += "\n" + fourth_line.rstrip()

    return arranged_problems
