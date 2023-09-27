import copy
import random

# Consider using the modules imported above.


# kwargs stands for "keyword arguments". It is a Python feature that allows you to pass arguments to a function by keyword,
#  instead of by position. This can be useful when you have a function with many arguments, or when you want to explicitly specify the values of certain arguments.
# To use kwargs, you simply pass a dictionary of arguments to the function. The keys of the dictionary are the names of the arguments,
# and the values of the dictionary are the values of the arguments.
class Hat:
    def __init__(self, **kwargs):
        # This line initializes the contents attribute of the Hat object.
        # The contents attribute is a list of the balls in the hat,
        # with each ball represented by the key of the corresponding keyword argument.
        # The number of times each ball appears in the list is equal to the value
        # of the corresponding keyword argument.
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, n):
        # This line ensures that the number of balls drawn is not greater than
        # the number of balls in the hat.
        n = min(n, len(self.contents))

        # This line draws n balls from the hat at random and returns them as a list.
        return [
            self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)
        ]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # This variable will store the number of experiments in which the expected number of balls are drawn.
    m = 0

    # This loop iterates over the number of experiments.
    for _ in range(num_experiments):
        # This line creates a copy of the hat object.
        # This is necessary to ensure that the original hat object is not modified
        # during the experiment.
        another_hat = copy.deepcopy(hat)

        # This line draws num_balls_drawn balls from the copied hat object.
        balls_drawn = another_hat.draw(num_balls_drawn)

        # This line counts the number of balls drawn that meet the expected criteria.
        balls_req = sum(
            [1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v]
        )

        # If the number of balls drawn that meet the expected criteria is equal to the
        # number of expected balls, then the experiment is considered a success.
        m += 1 if balls_req == len(expected_balls) else 0

    # This line returns the fraction of experiments that were successful.
    return m / num_experiments
