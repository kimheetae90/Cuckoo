from typing import TypeVar

T = TypeVar('T')


class ValueNode:
    def __init__(self, value: T) -> None:
        self._value = value

    def get_value(self) -> T:
        return self._value

    def set_value(self, value: T) -> None:
        self._value = value