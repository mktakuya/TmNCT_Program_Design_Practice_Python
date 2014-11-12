from random import randint

class ListGenerater(object):
    @staticmethod
    def generate(length, minimum, maximum):
        li = []
        for i in range(length):
            li.append(randint(minimum, maximum))

        return li
