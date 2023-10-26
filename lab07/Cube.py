from CubeInterface import CubeInterface
from Asserter import assertInt, assertPosInt


class Cube(CubeInterface):
    def __init__(self, m: int, n: int, page: int) -> None:
        super().__init__(m, n, page)
