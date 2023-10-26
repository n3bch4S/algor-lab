from typing import Any


def assertInt(x: Any) -> None:
    if type(x) != int:
        raise TypeError("This parameter is not int")


def assertFloat(x: Any) -> None:
    if type(x) != float:
        raise TypeError("This parameter is not float")


def assertString(x: Any) -> None:
    if type(x) != str:
        raise TypeError("This parameter is not string")


def assertList(x: Any) -> None:
    if type(x) != list:
        raise TypeError("This parameter is not list")


def assertTuple(x: Any) -> None:
    if type(x) != tuple:
        raise TypeError("This parameter is not tuple")


def assertDict(x: Any) -> None:
    if type(x) != dict:
        raise TypeError("This parameter is not dictionary")


def assertPosInt(x: Any) -> None:
    assertInt(x)
    if x <= 0:
        raise ValueError("This parameter is not positive")
