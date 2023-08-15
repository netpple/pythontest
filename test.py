import unittest
from timeit import default_timer
from trapping_rain_water import *
from two_sum import *
from three_sum import *
from array_partition_1 import *
from product_of_array_except_self import *
from best_time_stock import *
from palindrome_linked_list import *
from merge_two_sorted_list import *
from reverse_linked_list import *
from add_two_numbers import *
from swap_nodes_in_pairs import *


class MyTestCase(unittest.TestCase):

    def test_two_sum1(self):
        result = twosum_sol1([2, 7, 11, 15, 5, 4, 3], 9)
        self.assertEqual([(0, 1), (4, 5)], result)  # add assertion here

    def test_trapping_rain_water1(self):
        result = traprain_sol1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, result)

    def test_trapping_rain_water2(self):
        result = traprain_sol2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, result)

    def test_trapping_rain_water3(self):
        result = traprain_sol2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, result)

    def test_three_sum2(self):
        result = threesum_sol3([-1, 0, 1, 2, -1, -4], 0)
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], result)

    def test_three_sum3(self):
        result = threesum_sol3([-1, 0, 1, 2, -1, -4], 0)
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], result)

    def test_array_partition1(self):
        result = arraypart_sol1([1, 4, 2, 3])
        self.assertEqual(4, result)

    def test_array_partition2(self):
        result = arraypart_sol2([1, 4, 2, 3])
        self.assertEqual(4, result)

    def test_product_except_self(self):
        result = productexceptself_sol2([1, 2, 3, 4])
        self.assertEqual([24, 12, 8, 6], result)

    def test_best_time_stock(self):
        result = max_profit3([7, 1, 5, 3, 6, 4])
        self.assertEqual(5, result)

    def test_palindrome_linked_list(self):
        head = get_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])

        stime = default_timer()
        result = is_palindrome4(head)
        elaspsed = (default_timer() - stime) * 1000
        print(f'elapsed time: {elaspsed}')

        stime = default_timer()
        result = is_palindrome3(head)
        elaspsed = (default_timer() - stime) * 1000
        print(f'elapsed time: {elaspsed}')

        stime = default_timer()
        result = is_palindrome5(head)
        elaspsed = (default_timer() - stime) * 1000
        print(f'elapsed time: {elaspsed}')

        stime = default_timer()
        result = is_palindrome6(head)
        elaspsed = (default_timer() - stime) * 1000
        print(f'elapsed time: {elaspsed}')

        self.assertEqual(True, result)

    def test_merge_two_sorted_list1(self):
        result = merge_two_lists2(get_linked_list([1, 2, 4]), get_linked_list([1, 3, 4]))
        self.assertEqual("112344", print_linked_list(result))

    def test_reverse_linked_list1(self):
        result = reverse_linked_list1(get_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual("54321", print_linked_list(result))

    def test_add_two_numbers1(self):
        result = two_sum(get_linked_list([2, 4, 3]), get_linked_list([5, 6, 4]))
        self.assertEqual("708", print_linked_list(result))

    def test_bin_longest_count(self):
        num = 120003
        binary = bin(num)
        print(binary)
        longest, count = 0, 0
        for i in range(2, len(binary)):
            if binary[i] == "1":
                longest = max(longest, count)
                count = 0
            else:
                count = count + 1

        self.assertEqual(4, longest)

    def test_swap_pairs(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
