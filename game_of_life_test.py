import unittest
from assertpy import assert_that
from game_of_life_rules import should_live
from hypothesis import given
from hypothesis.strategies import integers


class GameOfLifeRules(unittest.TestCase):
    @staticmethod
    def test_cell_with_no_live_neighbours_dies():
        assert_that(should_live(True, 0)).is_false()
        assert_that(should_live(False, 0)).is_false()

    @staticmethod
    def test_cell_with_3_live_neighbours_lives():
        assert_that(should_live(True, 3)).is_true()
        assert_that(should_live(False, 3)).is_true()

    @given(integers(min_value=4))
    def test_cell_with_more_than_3_live_neighbours_dies(self, i):
        assert_that(should_live(True, i)).is_false()
        assert_that(should_live(False, i)).is_false()

    @staticmethod
    def test_any_live_cell_with_two_or_three_live_neighbours_lives():
        assert_that(should_live(True, 2)).is_true()
        assert_that(should_live(True, 3)).is_true()

    @staticmethod
    def test_any_live_cell_with_two_or_three_live_neighbours_lives():
        assert_that(should_live(True, 2)).is_true()
        assert_that(should_live(True, 3)).is_true()


if __name__ == '__main__':
    unittest.main()
