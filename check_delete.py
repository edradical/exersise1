from algoritms1 import Node
from algoritms1 import LinkedList
import unittest

class NameTestCase(unittest.TestCase):

    def test_delete_all_false(self):
        B = LinkedList()
        B.add_in_tail(Node(77))
        B.add_in_tail(Node(88))
        B.add_in_tail(Node(99))
        B.add_in_tail(Node(11))
        B.add_in_tail(Node(88))
        B.delete(88)
        x = B.add_in_list()
        y = [77, 99, 11, 88]
        self.assertEqual(x, y)

        B.delete(88)
        y = [77, 99, 11]
        x = B.add_in_list()
        self.assertEqual(x, y)

        B.delete(77)
        y = [99, 11]
        x = B.add_in_list()
        self.assertEqual(x, y)

        B.delete(99)
        B.delete(11)
        x = B.add_in_list()
        y = []
        self.assertEqual(x, y)


if __name__ == '__name__':
    unittest.main()



