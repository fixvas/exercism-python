import math


class Allergies(object):
    a_list = {1: 'eggs',
              2: 'peanuts',
              4: 'shellfish',
              8: 'strawberries',
              16: 'tomatoes',
              32: 'chocolate',
              64: 'pollen',
              128: 'cats'
              }

    def __init__(self, score):
        self.score = score
        self.lst = []

        if self.score > sum(Allergies.a_list):
            self.score -= 2**math.floor(math.log2(self.score))

        for i in sorted(Allergies.a_list, reverse=True):
            if self.score == i:
                self.lst.append(Allergies.a_list[i])
                break
            elif not self.score - i < 0:
                self.lst.append(Allergies.a_list[i])
                self.score -= i
        self.lst.reverse()

        self.score = score

    def is_allergic_to(self, name):
        return True if name in self.lst else False
