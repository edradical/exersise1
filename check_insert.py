from algoritms1 import Node
from algoritms1 import LinkedList
import unittest

class NameTestCase(unittest.TestCase):

    def test_insert(self):
        A = LinkedList()
        A.insert(None, 11)
        self.assertEqual(A.head.value, 11)
        self.assertEqual(A.tail.value, 11)
        self.assertEqual(A.len(), 1)




if __name__ == '__name__':
    unittest.main()



