from game.main import Table, Robot, Game

from unittest import TestCase

class TestGame(TestCase):
    def test_game(self):
        test_table = Table()
        test_robot = Robot()

        # Test Case: test ignore commands before place
        game = Game(test_table, test_robot)
        game.rotate_left()
        game.rotate_right()
        game.move()
        self.assertEqual(game.report(), None)

        # Test Case: test place out of bounds
        game.place(-2,-2,"EAST")
        game.rotate_left()
        game.rotate_right()
        game.move()
        self.assertEqual(game.report(), None)

        # Test Case: test exit boundaries at 0,0
        game.place(0,0,"SOUTH")
        game.move()
        game.rotate_right()
        game.report()
        self.assertEqual(game.report(), "0,0,WEST")

        # Test Case: test exit boundaries at 4,4
        game.place(4,4,"NORTH")
        game.move()
        game.rotate_right()
        game.report()
        self.assertEqual(game.report(), "4,4,EAST")

        # Test Case: test traverse from midpoint
        game.place(2,2,"NORTH")
        game.move()
        game.rotate_right()
        game.move()
        game.rotate_left()
        game.move()
        game.move()
        game.report()
        self.assertEqual(game.report(), "3,4,NORTH")

        # Test Case: sample 1 in challenge
        game.place(0,0,"NORTH")
        game.move()
        self.assertEqual(game.report(), "0,1,NORTH")

        # Test Case: sample 2 in challenge
        game.place(0,0,"NORTH")
        game.rotate_left()
        self.assertEqual(game.report(), "0,0,WEST")

        # Test Case: sample 3 in challenge
        game.place(1,2,"EAST")
        game.move()
        game.move()
        game.rotate_left()
        game.move()
        self.assertEqual(game.report(), "3,3,NORTH")
