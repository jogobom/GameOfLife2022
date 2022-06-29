import unittest
from assertpy import assert_that
from grid import count_neighbours


class NeighbourCounting(unittest.TestCase):
    @staticmethod
    def test_a_singleton_cell_has_zero_neighbours():
        assert_that(count_neighbours(0, [False])).is_zero()

    @staticmethod
    def test_a_grid_with_single_row_of_two_cells_has_one_neighbour():
        assert_that(count_neighbours(0, [False, False])).is_equal_to(0)
        assert_that(count_neighbours(0, [False, True])).is_equal_to(1)
        assert_that(count_neighbours(0, [True, True])).is_equal_to(1)
        assert_that(count_neighbours(0, [True, False])).is_equal_to(0)
        assert_that(count_neighbours(1, [False, False])).is_equal_to(0)
        assert_that(count_neighbours(1, [False, True])).is_equal_to(0)
        assert_that(count_neighbours(1, [True, True])).is_equal_to(1)
        assert_that(count_neighbours(1, [True, False])).is_equal_to(1)


if __name__ == '__main__':
    unittest.main()
