import unittest
from assertpy import assert_that


def should_live(live_neighbours):
    return False


class GameOfLifeRules(unittest.TestCase):
    @staticmethod
    def test_cell_with_no_live_neighbours_dies():
        assert_that(should_live(0)).is_false()


if __name__ == '__main__':
    unittest.main()
