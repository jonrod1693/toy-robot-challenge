class InvalidTableDimensionException(Exception):
    pass

class Table:
    def __init__(self, min_x=0, min_y=0, max_x=4, max_y=4):
        """Represents table of size len(min_x to max_x) by len(min_y to max_y)

        Args:
            min_x (int, optional): Defaults to 0.
            min_y (int, optional): Defaults to 0.
            max_x (int, optional): Defaults to 4.
            max_y (int, optional): Defaults to 4.

        Raises:
            InvalidTableDimensionException: if min values are greater than values
        """
        self._min_x = 0
        self._min_y = 0
        self._max_x = 0
        self._max_y = 0

        if min_x > max_x or min_x > max_y:
            raise InvalidTableDimensionException(
                "Table max x/y values should be bigger than or equal to min values."
            )
        else:
            self._min_x = min_x
            self._min_y = min_y
            self._max_x = max_x
            self._max_y = max_y
        

    def is_within_bounds(self, x: int, y: int) -> bool:
        """Checks if coordinate is within table bounds.

        Args:
            x (int): x coordinate to check.
            y (int): y coordinate to check.

        Returns:
            bool: Returns True if within table bounds, False if otherwise.
        """
        return self._min_x <= x <= self._max_x and self._min_y <= y <= self._max_y
