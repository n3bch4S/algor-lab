from abc import ABC, abstractmethod
from Asserter import assertPosInt


class MatrixInterface(ABC):
    def __init__(self, m: int, n: int) -> None:
        assertPosInt(m)
        assertPosInt(n)

        self.row = m
        self.column = n
        self.matrix: list[list] = []
        for i in range(m):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(0.0)

    def __str__(self) -> str:
        if self.row == 0 or self.column == 0:
            return "No matrix"

        txt = ""
        for tRow in self.matrix:
            for ele in tRow:
                txt += f"{ele} "
            txt += "\n"
        return txt

    def __repr__(self) -> str:
        return self.__str__()
