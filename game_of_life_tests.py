import unittest
from assertpy import assert_that
from game_of_life_rules import should_live


class GameOfLifeRules(unittest.TestCase):
    @staticmethod
    def test_cell_with_no_live_neighbours_dies():
        assert_that(should_live(0)).is_false()

    @staticmethod
    def test_cell_with_3_live_neighbours_lives():
        assert_that(should_live(3)).is_true()


if __name__ == '__main__':
    unittest.main()
