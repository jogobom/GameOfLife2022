import unittest
from assertpy import assert_that
from rules import should_live
from hypothesis import given
from hypothesis.strategies import integers


class CellIsCurrentlyAlive(unittest.TestCase):
    @staticmethod
    def test_with_two_or_three_live_neighbours_survives():
        assert_that(should_live(True, 2)).is_true()
        assert_that(should_live(True, 3)).is_true()

    @given(integers().filter(lambda x: x != 2 and x != 3))
    def test_with_any_other_number_of_neighbours_dies(self, i):
        assert_that(should_live(True, i)).is_false()


class CellIsCurrentlyDead(unittest.TestCase):
    @staticmethod
    def test_with_three_live_neighbours_comes_alive():
        assert_that(should_live(False, 3)).is_true()

    @staticmethod
    def test_with_two_live_neighbours_stays_dead():
        assert_that(should_live(False, 2)).is_false()

    @given(integers().filter(lambda x: x != 2 and x != 3))
    def test_with_any_other_number_of_neighbours_stays_dead(self, i):
        assert_that(should_live(False, i)).is_false()


if __name__ == '__main__':
    unittest.main()
