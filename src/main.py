import re

from table import Table
from robot import Direction, Position, Robot


class Moves():
    def __init__(self, table, robot):
        self._table = table
        self._robot = robot

    def place(self, x, y, direction):
        if self._table.is_within_bounds(x, y):
            self._robot.position = Position(x, y, direction)

    def rotate_left(self):
        if self._robot.position:
            self._robot.position.direction = Direction(self._robot.position.direction).rotate_left()

    def rotate_right(self):
        if self._robot.position:
            self._robot.position.direction = Direction(self._robot.position.direction).rotate_right()

    def move(self):
        robot_x_position = self._robot.position.x
        robot_y_position = self._robot.position.y

        if self._robot.position.direction == Direction.NORTH and self._table.is_within_bounds(robot_x_position, robot_y_position + 1):
            self._robot.position.y += 1
        elif self._robot.position.direction == Direction.EAST and self._table.is_within_bounds(robot_x_position + 1, robot_y_position):
            self._robot.position.x += 1
        elif self._robot.position.direction == Direction.SOUTH and self._table.is_within_bounds(robot_x_position, robot_y_position - 1):
            self._robot.position.y -= 1
        elif self._robot.position.direction == Direction.WEST and self._table.is_within_bounds(robot_x_position - 1, robot_y_position):
            self._robot.position.x -= 1

    def report(self):
        return str(self._robot.position)


def main():
    table = Table()
    robot = Robot()
    moves = Moves(table, robot)
    try:
        while True:
            command = input().upper()
            if command.startswith("PLACE "):
                _, position_input = command.split(" ", 1)
                position_pattern = re.compile(
                    r"^(\d+),\s*(\d+),\s*(NORTH|EAST|SOUTH|WEST)$", re.IGNORECASE
                )
                match = position_pattern.match(position_input)
                if match:
                    x = int(match.group(1))
                    y = int(match.group(2))
                    direction = match.group(3)
                    moves.place(x, y, direction)
            elif command == "MOVE" and robot.is_placed():
                moves.move()
            elif command == "LEFT" and robot.is_placed():
                moves.rotate_left()
            elif command == "RIGHT" and robot.is_placed():
                moves.rotate_right()
            elif command == "REPORT" and robot.is_placed():
                print(f"Output: {moves.report()}")
            else:
                pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
