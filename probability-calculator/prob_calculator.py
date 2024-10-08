import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def draw(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents

        drawn_balls = []
        for _ in range(number_of_balls):
            drawn_balls.append(self.contents.pop(random.randrange(len(self.contents))))

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0.0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        successful_experiment = True
        for key, value in expected_balls.items():
            if drawn_balls.count(key) < value:
                successful_experiment = False
        if successful_experiment:
            probability += 1 / num_experiments

    return probability
