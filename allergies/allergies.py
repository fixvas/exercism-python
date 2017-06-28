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
        some = sum(Allergies.a_list)

        if self.score > some:
            self.score -= 2**(math.floor(math.log2(self.score)))

        if self.score <= some:
            for i in sorted(Allergies.a_list, reverse=True):
                if self.score == i:
                    self.lst.append(Allergies.a_list[i])
                    break
                elif self.score - i < 0:
                    continue
                else:
                    self.lst.append(Allergies.a_list[i])
                    self.score -= i
            self.lst.reverse()

        if self.score > some:
            k = (self.score % (some + 1))
            if k in Allergies.a_list:
                self.lst.append(Allergies.a_list[k])
            else:
                tmp = abs(k - some)
                if tmp in Allergies.a_list:
                    for j in Allergies.a_list:
                        if j != tmp:
                            self.lst.append(Allergies.a_list[j])

    def is_allergic_to(self, name):
        return True if name in self.lst else False
