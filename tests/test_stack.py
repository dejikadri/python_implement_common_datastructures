import unittest
from collections import deque
from python_implement_common_datastructures import py_stack

class TestStack(unittest.TestCase):

    def setUp(self):
        # empty Stack
        self.pse = py_stack.Stack()

        self.ps = py_stack.Stack()
        self.ps.push('tatooine')
        self.ps.push('naboo')
        self.ps.push('kamino')

    def test_isempty_when_empty(self):
        self.assertEqual(self.pse.isempty(), True)

    def test_isempty_when_not_empty(self):
        self.assertEqual(self.ps.isempty(), False)

    def test_push_when_empty(self):
        self.pse.push('hoth')
        self.assertEqual(self.pse.peek(), 'hoth')
        self.assertEqual(self.pse.size(), 1)

    def test_push_when_not_empty(self):
        self.ps.push('hoth')
        self.assertEqual(self.ps.peek(), 'hoth')
        self.assertEqual(self.ps.size(), 4)

    def test_pop_when_empty(self):
        self.assertEqual(self.pse.pop(), 'Stack is empty!')

    def test_pop_when_not_empty(self):
        self.assertEqual(self.ps.pop(), 'kamino')

    def test_peek_when_empty(self):
        self.assertEqual(self.pse.peek(), "Stack is empty!")

    def test_peek_when_not_empty(self):
        self.assertEqual(self.ps.peek(), 'kamino')

    def test_size_when_empty(self):
        self.assertEqual(self.pse.size(), 0)

    def test_size_when_not_empty(self):
        self.assertEqual(self.ps.size(), 3)

    def test_show_when_empty(self):
        self.assertEqual(self.pse.show(), deque([]))

    def test_show_when_not_empty(self):
        print(self.ps.show())

        self.assertEqual(self.ps.show(), deque(['kamino', 'naboo', 'tatooine']) )
