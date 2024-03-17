from game.table import Table, InvalidTableDimensionException
from unittest import TestCase


class TestTable(TestCase):
    def test_init(self):
        # Test Case: test default init
        table = Table()
        self.assertEqual(table._min_x, 0)
        self.assertEqual(table._min_x, 0)
        self.assertEqual(table._max_x, 4)
        self.assertEqual(table._max_y, 4)

        # Test Case: min and max x y defined
        table = Table(-2, -2, 2, 2)
        self.assertEqual(table._min_x, -2)
        self.assertEqual(table._min_x, -2)
        self.assertEqual(table._max_x, 2)
        self.assertEqual(table._max_y, 2)

        # Test Case: min x and y greater than max
        with self.assertRaisesRegex(
            InvalidTableDimensionException,
            "Table max x/y values should be bigger than or equal to min values."
        ):
            table = Table(1, 1, -1, -1)
    
    def test_is_within_bounds(self):
        table = Table()

        # Test Case: test squares inside table
        self.assertTrue(table.is_within_bounds(0,0))
        self.assertTrue(table.is_within_bounds(4,0))
        self.assertTrue(table.is_within_bounds(0,4))
        self.assertTrue(table.is_within_bounds(4,4))
        self.assertTrue(table.is_within_bounds(2,2))

        # Test Case: test out of bounds squares
        self.assertFalse(table.is_within_bounds(0,-1))
        self.assertFalse(table.is_within_bounds(5,0))
        self.assertFalse(table.is_within_bounds(5,4))
        self.assertFalse(table.is_within_bounds(4,-1))
