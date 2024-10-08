# Polygon Area Calculator

In this project, you will create a `Rectangle` class and a `Square` class using object-oriented programming principles. The `Square` class will be a subclass of `Rectangle`, inheriting its methods and attributes.

## Project Structure

The project consists of the following files:

- **`main.py`**: The entry point of the application that demonstrates the functionality of the polygon area calculator.
- **`shape_calculator.py`**: This file contains the implementation of the `Rectangle` and `Square` classes.
- **`test_module.py`**: This file includes unit tests to validate the functionality of the polygon area calculator.

## Assignment

The Polygon Area Calculator allows users to create rectangle and square objects, calculate their area, perimeter, diagonal, and visualize their shapes using text representation.

### Class: `Rectangle`

The `Rectangle` class should include the following methods:

- **`set_width(width)`**: Sets the width of the rectangle.
- **`set_height(height)`**: Sets the height of the rectangle.
- **`get_area()`**: Returns the area (width * height).
- **`get_perimeter()`**: Returns the perimeter (2 * width + 2 * height).
- **`get_diagonal()`**: Returns the diagonal length ((width ** 2 + height ** 2) ** .5).
- **`get_picture()`**: Returns a string representation of the rectangle using `*`. If either dimension exceeds 50, it returns "Too big for picture.".
- **`get_amount_inside(shape)`**: Returns the number of times the passed shape can fit inside the rectangle without rotation.
- **`__str__()`**: Returns a string representation like `Rectangle(width=5, height=10)`.

### Class: `Square`

The `Square` class inherits from the `Rectangle` class and should include:

- **`__init__(side)`**: Initializes the square with the same value for width and height.
- **`set_side(side)`**: Sets both width and height.
- **`__str__()`**: Returns a string representation like `Square(side=9)`.

### Example Usage

Here are some examples of how to use the classes:

```python
rect = Rectangle(10, 5)
print(rect.get_area())              # Returns: 50
rect.set_height(3)
print(rect.get_perimeter())         # Returns: 26
print(rect)                         # Returns: Rectangle(width=10, height=3)
print(rect.get_picture())           # Returns: String of '*' representing the rectangle

sq = Square(9)
print(sq.get_area())                # Returns: 81
sq.set_side(4)
print(sq.get_diagonal())            # Returns: 5.656854249492381
print(sq)                           # Returns: Square(side=4)
print(sq.get_picture())             # Returns: String of '*' representing the square

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))   # Returns: 8
```


For more information about the project, visit: [Polygon Area Calculator Project](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-polygon-area-calculator-project/build-a-polygon-area-calculator-project).