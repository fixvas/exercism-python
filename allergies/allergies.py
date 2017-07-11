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
        for scr, allergen in sorted(self.a_list.items()):
            if scr & self.score:
                self.lst.append(allergen)

    def is_allergic_to(self, name):
        return name in self.lst
