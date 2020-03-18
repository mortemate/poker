import random


class Poker(object):

    def __init__(self):
        self.number_of_dices = 5

    def roll(self):
        result = []
        for dice in range(self.number_of_dices):
            result.append(random.randint(1, 6))
        return result

    def check_result(self, result):
        unique_result = list(set(result))
        result_dict = {}
        for i in unique_result:
            result_dict[i] = result.count(i)
        return result_dict
