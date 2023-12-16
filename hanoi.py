import copy


class HanoiConfiguration(list):
    def __init__(self, nbStacks, nbDisks):
        list.__init__(self, [[(nbDisks - i) for i in range(nbDisks)]] + [[] for _ in range(nbStacks - 1)])

    def __hash__(self):
        return 1

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if len(self[i]) != len(other[i]):
                return False
            for j in range(len(self[i])):
                if other[i][j] != self[i][j]:
                    return False
        return True


