from abc import ABC, abstractmethod
from Matrix import Matrix
from Asserter import assertPosInt


class CubeInterface(ABC):
    def __init__(self, m: int, n: int, page: int) -> None:
        assertPosInt(m)
        assertPosInt(n)
        assertPosInt(page)

        self.row = m
        self.column = n
        self.page = page
        self.cube: list[Matrix] = []
        for k in range(page):
            self.cube.append(Matrix(m, n))

    def __str__(self) -> str:
        if self.row == 0 or self.column == 0 or self.page == 0:
            return "No Cube"

        txt = ""
        for matrix in self.cube:
            txt += f"{matrix}\n"
        return txt

    def __repr__(self) -> str:
        return self.__str__()
