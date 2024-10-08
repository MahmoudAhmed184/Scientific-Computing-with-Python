# Time Calculator

In this project, you will build an `add_time` function that calculates a new time by adding a duration to a starting time in 12-hour format. This function will also handle the addition of days and return the correct day of the week if specified.

## Project Structure

The project consists of the following files:

- **`main.py`**: The entry point of the application that demonstrates the functionality of the time calculator.
- **`time_calculator.py`**: This file contains the implementation of the `add_time` function.
- **`test_module.py`**: This file includes unit tests to validate the functionality of the time calculator.

## Assignment

The Time Calculator allows users to add a duration to a specified starting time and optionally include the starting day of the week. The result will display the new time along with any changes in the day, indicating if the new time falls on the next day or subsequent days.

### Function: `add_time`

The `add_time` function takes two required parameters and one optional parameter:

- **`start_time`**: A string representing the starting time in 12-hour format (ending in AM or PM).
- **`duration`**: A string representing the duration to add, formatted as "hours:minutes".
- **`day_of_week`** (optional): A string representing the day of the week (case insensitive).

The function returns a string that indicates the new time and any relevant day information.

### Example Usage

Here are some examples of how to use the `add_time` function:

```python
add_time('3:00 PM', '3:10')
# Returns: '6:10 PM'

add_time('11:30 AM', '2:32', 'Monday')
# Returns: '2:02 PM, Monday'

add_time('11:43 AM', '00:20')
# Returns: '12:03 PM'

add_time('10:10 PM', '3:30')
# Returns: '1:40 AM (next day)'

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: '12:03 AM, Thursday (2 days later)'

add_time('6:30 PM', '205:12')
# Returns: '7:42 AM (9 days later)'
```

### Handling Edge Cases

The `add_time` function should properly handle the following scenarios:

- If the result time falls on the next day, it will append "(next day)".
- If more than one day later, it will append "(n days later)" where "n" is the number of days.
- If a starting day of the week is provided, it will include the day in the result.

### Notes

- Do not import any Python libraries.
- Assume that all start times are valid times.
- The duration minutes will always be a whole number less than 60, but hours can be any whole number.


For more information about the project, visit: [Build a Time Calculator Project](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-time-calculator-project/build-a-time-calculator-project).