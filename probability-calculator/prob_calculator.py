import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, number_of_balls: int):
        if number_of_balls > len(self.contents):
            drawn_balls = copy.deepcopy(self.contents)
            self.contents.clear()
            return drawn_balls
        
        return [
            self.contents.pop(random.randrange(len(self.contents)))
            for _ in range(number_of_balls)
        ]


def experiment(hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    successful_experiments = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        success = all(drawn_balls.count(color) >= count for color, count in expected_balls.items())

        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments
