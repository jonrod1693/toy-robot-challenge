class Table:
    def __init__(self, min_x=0, min_y=0, max_x=4, max_y=4):
        self._min_x = min_x
        self._min_y = min_y
        self._max_x = max_x
        self._max_y = max_y

    def is_within_bounds(self, x, y):
        return self._min_x <= x <= self._max_x and self._min_y <= y <= self._max_y
