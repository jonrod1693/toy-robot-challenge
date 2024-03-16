from collections import deque
from enum import Enum


class Direction(Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"

    def _shift_direction_queue(self, step: int):
        current_index = DIRECTION_QUEUE.index(self)
        DIRECTION_QUEUE.rotate(step)
        return DIRECTION_QUEUE[current_index]

    def rotate_left(self):
        return self._shift_direction_queue(1)

    def rotate_right(self):
        return self._shift_direction_queue(-1)


DIRECTION_QUEUE = deque([Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST])


class Position():
    def __init__(self, x, y, direction: Direction):
        self.x = x
        self.y = y
        self.direction = Direction(direction)

    def __str__(self) -> str:
        return f"{self.x},{self.y},{self.direction.value}"


class Robot():
    def __init__(self):
        self._position = None

    def is_placed(self):
        return self._position is not None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position
