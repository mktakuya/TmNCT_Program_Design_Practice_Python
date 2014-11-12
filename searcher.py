class Searcher:
    def __init__(self):
        pass

    @staticmethod
    def liner_search(li, target):
        for index, value in enumerate(li):
            if li[index] == target:
                return index
        return False

    @staticmethod
    def sentinel_search(li, target):
        li.append(x)

        for index, value in enumerate(li):
            if value == target:
                return index
        return False

    @staticmethod
    def binary_search(li, target):
        pass

