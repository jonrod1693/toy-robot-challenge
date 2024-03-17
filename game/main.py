import re

from table import Table
from robot import Direction, Position, Robot


class Game():
    def __init__(self, table: Table, robot: Robot):
        """Represents game that can be played with Robot on Table object.

        Args:
            table (Table): Represents table to play game on.
            robot (Robot): Represents robot that will traverse the table.
        """
        self._table = table
        self._robot = robot

    def place(self, x: int, y: int, direction: Direction):
        """Places a robot on the table.

        Args:
            x (int): x coordinate of where to place robot object on table.
            y (int): y coordinate of where to place robot object on table.
            direction (Direction): what direction robot will be facing upon table placement.
        """
        if self._table.is_within_bounds(x, y):
            self._robot.position = Position(x, y, direction)

    def rotate_left(self):
        """Rotates robot object 90 degrees left from where it is currently facing.
        """
        if self._robot.position:
            self._robot.position.direction = Direction(self._robot.position.direction).rotate_left()

    def rotate_right(self):
        """Rotates robot object 90 degrees left from where it is currently facing.
        """
        if self._robot.position:
            self._robot.position.direction = Direction(self._robot.position.direction).rotate_right()

    def move(self):
        """Moves robot object 1 step forward to where it is currently facing.
        """
        if self._robot.position:
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
        """Returns current robot position.

        Returns:
            string: Returns current robot position in 'X,Y,D' format.
        """
        if self._robot.position:
            return str(self._robot.position)


def main():
    table = Table()
    robot = Robot()
    game = Game(table, robot)
    try:
        while True:
            command = input().strip().upper()
            if command.startswith("PLACE "):
                _, position_input = command.split(" ", 1)
                position_pattern = re.compile(
                    r"^(\d+)\s*,\s*(\d+)\s*,\s*(NORTH|EAST|SOUTH|WEST)$", re.IGNORECASE
                )
                match = position_pattern.match(position_input.strip())
                if match:
                    x = int(match.group(1))
                    y = int(match.group(2))
                    direction = match.group(3)
                    game.place(x, y, direction)
            elif command == "MOVE" and robot.is_placed():
                game.move()
            elif command == "LEFT" and robot.is_placed():
                game.rotate_left()
            elif command == "RIGHT" and robot.is_placed():
                game.rotate_right()
            elif command == "REPORT" and robot.is_placed():
                print(f"Output: {game.report()}")
            else:
                pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
