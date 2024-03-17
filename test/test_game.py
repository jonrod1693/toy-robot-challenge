from game.main import Table, Robot, Game

from unittest import TestCase

class TestGame(TestCase):
    def test_moves(self):
        test_table = Table()
        test_robot = Robot()

        # Test Case: test ignore moves before place
        moves = Game(test_table, test_robot)
        moves.rotate_left()
        moves.rotate_right()
        moves.move()
        self.assertEqual(moves.report(), None)

        # Test Case: test place out of bounds
        moves.place(-2,-2,"EAST")
        moves.rotate_left()
        moves.rotate_right()
        moves.move()
        self.assertEqual(moves.report(), None)

        # Test Case: test exit boundaries at 0,0
        moves.place(0,0,"SOUTH")
        moves.move()
        moves.rotate_right()
        moves.report()
        self.assertEqual(moves.report(), "0,0,WEST")

        # Test Case: test exit boundaries at 4,4
        moves.place(4,4,"NORTH")
        moves.move()
        moves.rotate_right()
        moves.report()
        self.assertEqual(moves.report(), "4,4,EAST")

        # Test Case: test traverse from midpoint
        moves.place(2,2,"NORTH")
        moves.move()
        moves.rotate_right()
        moves.move()
        moves.rotate_left()
        moves.move()
        moves.move()
        moves.report()
        self.assertEqual(moves.report(), "3,4,NORTH")

        # Test Case: sample 1 in challenge
        moves.place(0,0,"NORTH")
        moves.move()
        self.assertEqual(moves.report(), "0,1,NORTH")

        # Test Case: sample 2 in challenge
        moves.place(0,0,"NORTH")
        moves.rotate_left()
        self.assertEqual(moves.report(), "0,0,WEST")

        # Test Case: sample 3 in challenge
        moves.place(1,2,"EAST")
        moves.move()
        moves.move()
        moves.rotate_left()
        moves.move()
        self.assertEqual(moves.report(), "3,3,NORTH")
