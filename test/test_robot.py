from game.robot import Direction, Position, Robot
from unittest import TestCase


class TestDirection(TestCase):
    def test_shift_direction_queue(self):
        # Test Case: test internal shift implementation
        self.assertEqual(Direction.NORTH._shift_direction_queue(1), Direction.WEST)
        self.assertEqual(Direction.EAST._shift_direction_queue(-1), Direction.SOUTH)
    
    def test_rotate_left(self):
        # Test Case: test all left rotations
        self.assertEqual(Direction.NORTH.rotate_left(), Direction.WEST)
        self.assertEqual(Direction.EAST.rotate_left(), Direction.NORTH)
        self.assertEqual(Direction.SOUTH.rotate_left(), Direction.EAST)
        self.assertEqual(Direction.WEST.rotate_left(), Direction.SOUTH)

    def test_rotate_right(self):
        # Test Case: test all right rotations
        self.assertEqual(Direction.NORTH.rotate_right(), Direction.EAST)
        self.assertEqual(Direction.EAST.rotate_right(), Direction.SOUTH)
        self.assertEqual(Direction.SOUTH.rotate_right(), Direction.WEST)
        self.assertEqual(Direction.WEST.rotate_right(), Direction.NORTH)

class TestPosition(TestCase):
    def test_position(self):
        position = Position(1,1,Direction.NORTH)
        self.assertEqual(position.x, 1)
        self.assertEqual(position.y, 1)
        self.assertEqual(position.direction, Direction.NORTH)
        self.assertEqual(str(position), "1,1,NORTH")

class TestRobot(TestCase):
    def test_robot(self):
        robot = Robot()

        # Test Case: test values on init
        self.assertEqual(robot.position, None)
        self.assertFalse(robot.is_placed())

        # Test Case: test setting position
        robot.position = Position(2,2,Direction.EAST)
        self.assertEqual(str(robot.position), "2,2,EAST")
        self.assertTrue(robot.is_placed())
