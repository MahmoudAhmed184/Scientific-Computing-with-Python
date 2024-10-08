# Probability Calculator

In this project, you will create a `Hat` class that simulates drawing balls of different colors from a hat. The program will estimate the probability of drawing certain combinations of balls through repeated experiments.

## Project Structure

The project consists of the following files:

- **`main.py`**: The entry point of the application that demonstrates the functionality of the probability calculator.
- **`prob_calculator.py`**: This file contains the implementation of the `Hat` class and the experiment function.
- **`test_module.py`**: This file includes unit tests to validate the functionality of the probability calculator.

## Assignment

The Probability Calculator allows users to define a hat containing various colored balls and then perform experiments to estimate the probability of drawing specific combinations of those balls.

### Class: `Hat`

The `Hat` class should include:

- **`__init__(**kwargs)`**: Accepts a variable number of arguments specifying the number of balls of each color. It should create a `contents` instance variable that is a list of strings, each representing a ball in the hat.

### Method: `draw(number_of_balls)`

- **`draw(number_of_balls)`**: This method removes and returns a specified number of balls from the `contents` list. If the number of balls to draw exceeds the available quantity, it returns all the balls.

### Function: `experiment(hat, expected_balls, num_balls_drawn, num_experiments)`

This function performs experiments to estimate the probability of drawing certain balls:

- **Parameters**:
  - **`hat`**: A `Hat` object containing the balls.
  - **`expected_balls`**: A dictionary indicating the exact group of balls to attempt to draw (e.g., `{'blue': 2, 'red': 1}`).
  - **`num_balls_drawn`**: The number of balls to draw from the hat in each experiment.
  - **`num_experiments`**: The number of experiments to perform.

- **Returns**: The function returns an approximate probability based on the results of the experiments.

### Example Usage

Here’s an example of how to use the `Hat` class and the `experiment` function:

```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(probability)  # Output: Approximately 0.356
```

### Notes

- The `Hat` class ensures that there is always at least one ball in the hat.
- The `draw` method simulates the drawing of balls without replacement.
- The `experiment` function performs a large number of trials to yield a reliable estimate of the probability.

For more information about the project, visit: [Build a Probability Calculator Project](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-probability-calculator-project/build-a-probability-calculator-project).