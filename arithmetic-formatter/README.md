# Arithmetic Formatter

In this project, you will build an `arithmetic_arranger` function that formats arithmetic problems for easier reading and solving. Students in primary school often arrange arithmetic problems vertically, making it easier to solve them. For example, the expression "235 + 52" would be formatted as:

```
  235
+  52
-----
```

## Project Structure

The project consists of the following files:

- **`main.py`**: The entry point of the application that demonstrates the functionality of the arithmetic formatter.
- **`arithmetic_arranger.py`**: This file contains the implementation of the `arithmetic_arranger` function.
- **`test_module.py`**: This file includes unit tests to validate the functionality of the `arithmetic_arranger` function.

## Assignment

The `arithmetic_arranger` function receives a list of strings, each representing an arithmetic problem, and returns them arranged vertically and side-by-side. An optional second argument allows the display of answers.

### Example

**Function Call Without Answers:**
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```
**Output:**
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

**Function Call With Answers:**
```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```
**Output:**
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

### Error Handling

The function will return the correctly formatted problems if they are properly arranged. If there are issues with the input, it will return a meaningful error message. The following conditions will trigger an error:

1. **Too Many Problems**: If more than five problems are supplied, the function will return: **"Error: Too many problems."**
2. **Invalid Operators**: The function only accepts addition (`+`) and subtraction (`-`). If other operators are provided, it will return: **"Error: Operator must be '+' or '-'."**
3. **Non-Digit Characters**: Each operand must contain only digits. If any operand contains non-digit characters, the function will return: **"Error: Numbers must only contain digits."**
4. **Operand Length**: Each operand can have a maximum width of four digits. If an operand exceeds this limit, the function will return: **"Error: Numbers cannot be more than four digits."**

### Formatting Rules

When formatting the problems, the following rules apply:

- There should be a single space between the operator and the longest of the two operands.
- The operator should be on the same line as the second operand.
- Both operands should maintain the order as provided (the first operand is on top).
- Numbers should be right-aligned.
- There should be four spaces between each problem.
- Dashes should appear at the bottom of each problem, extending along the entire length of each individual problem.


For more information about the project, visit: [Build an Arithmetic Formatter Project](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project)