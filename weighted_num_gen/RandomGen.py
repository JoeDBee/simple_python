import random


class RandomGen(object):
    """
    The RandomGen object contains a list of numbers and
    associated probability weights.

    Return a weighted random number using the next_num() method.

    Attributes:
        _probabilities (list): random number weights.
        _random_nums (list): numbers which can be generated
    """

    def __init__(self, random_nums, probabilities):
        if len(random_nums) != len(probabilities):
            raise ValueError('Inputs not equal size')

        if any(num < 0 for num in probabilities):
            raise ValueError('Negative weight entered')

        self._random_nums = random_nums
        self._probabilities = self.normalise_weights(probabilities)

    @staticmethod
    def normalise_weights(probabilities):
        '''Normalise probabilities such that they sum to one.'''
        weight_sum = sum(probabilities)
        weights = [weight / weight_sum for weight in probabilities]
        return weights

    def weighted_selection(self, n):
        '''Select number to generate using probability weights.'''
        for num, weight in zip(self._random_nums, self._probabilities):
            if n <= weight:
                return num
            n -= weight

    def next_num(self):
        '''Generate a weighted random number.'''
        random_num = random.random()
        return self.weighted_selection(random_num)
