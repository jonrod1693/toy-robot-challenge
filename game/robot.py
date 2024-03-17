from collections import deque
from enum import Enum

from typing import Optional


class Direction(Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"

    def _shift_direction_queue(self, step: int):
        """Shifts reference direction deque based on step to simulate change in direction.

        Args:
            step (int): Increment of how much to shift, can be negative.

        Returns:
            Direction: Direction object after shifting by n steps.
        """
        current_index = DIRECTION_QUEUE.index(self)
        DIRECTION_QUEUE.rotate(step)
        return DIRECTION_QUEUE[current_index]

    def rotate_left(self):
        """Rotate 90 degrees left from current direction.

        Returns:
            Direction: Direction object after rotating 90 degrees left from current direction.
        """
        return self._shift_direction_queue(1)

    def rotate_right(self):
        """Rotate 90 degrees right from current direction.

        Returns:
            Direction: Direction object after rotating 90 degrees right from current direction.
        """
        return self._shift_direction_queue(-1)


DIRECTION_QUEUE = deque([Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST])


class Position():
    def __init__(self, x: int, y: int, direction: Direction):
        """Represents position of robot object on the table.

        Args:
            x (int): represents x coordinate of robot position.
            y (int): represents y coordinate of robot position.
            direction (Direction): represents direction where robot is currently facing.
        """
        self.x = x
        self.y = y
        self.direction = Direction(direction)

    def __str__(self) -> str:
        return f"{self.x},{self.y},{self.direction.value}"


class Robot():
    def __init__(self):
        """Represents a robot object to be placed on the table.

        Attributes:
            _position (Optional[Position]): represents position of robot on table, None if not yet set.
        """
        self._position = None

    def is_placed(self) -> bool:
        """Checks whether robot object has been placed on table.

        Returns:
            bool: True if placed, False otherwise.
        """
        return self._position is not None

    @property
    def position(self) -> Optional[Position]:
        return self._position

    @position.setter
    def position(self, position: Position):
        self._position = position
