from unittest import TestCase, main

from List.extended_list import IntegerList


class TestIntiger(TestCase):

    def setUp(self):
        self.intigers_list = IntegerList(1, 2, 3, "4", "five")

    def test_correct_init(self):
        correct_list = [1, 2, 3]

        self.assertEqual(correct_list, self.intigers_list.get_data())

    def test_add_not_intiger_value_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.intigers_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_raises_index_error(self):

        with self.assertRaises(IndexError) as ie:
            self.intigers_list.remove_index(100)

        self.assertEqual("Index is out of range", str(ie.exception))


    def test_get_raises_index_error(self):

        with self.assertRaises(IndexError) as ie:
            self.intigers_list.get(5)

        self.assertEqual("Index is out of range", str(ie.exception))


    def test_insert_raises_index_error(self):

        with self.assertRaises(IndexError) as ie:
            self.intigers_list.insert(5, 25)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_value_error_when_element_not_found(self):

        with self.assertRaises(ValueError) as ve:
            self.intigers_list.insert(1, 5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))


    def test_get_biggest_return_biggest_el(self):
        self.assertEqual(3, self.intigers_list.get_biggest())

    def test_get_intex(self):
        self.assertEqual(1, self.intigers_list.get_index(2))


    def test_add_element_add_the_element_to_the_list(self):
        correct_list  = [1, 2, 3, 4]
        self.assertEqual(correct_list, self.intigers_list.add(4))

    def


if __name__ == "__main__":
    main()