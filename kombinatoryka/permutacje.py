from itertools import permutations
from typing import List


def _permute(num: List[int]) -> List[List[int]]:
    x = permutations(num)
    return list(x)


def kon(wej):
    print(wej)


if __name__ == "__main__":
    num = [1, 2, 3]
    permutacja = _permute(num)
    print(list(permutacja))
