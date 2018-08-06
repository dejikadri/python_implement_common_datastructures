import unittest
from collections import deque
from python_implement_common_datastructures import py_queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        #empty Queue
        self.pqe = py_queue.Queue()

        self.pq = py_queue.Queue()
        self.pq.enqueue('corusant')
        self.pq.enqueue('umbara')
        self.pq.enqueue('geonosis')


    def test_peek_empty(self):
        self.assertEqual(self.pqe.peekfirstin(), "Empty")
        self.assertEqual(self.pqe.peeklastin(), "Empty")

    def test_peek_not_empty(self):
        self.assertEqual(self.pq.peekfirstin(), 'corusant')
        self.assertEqual(self.pq.peeklastin(), 'geonosis')

    def test_size_empty(self):
        self.assertEqual(self.pq.size(), 3)

    def test_size_not_empty(self):
        self.assertEqual(self.pqe.size(), 0)

    def test_isempty_when_empty(self):
        self.assertEqual(self.pqe.isempty(), True)

    def test_isempty_when_not_empty(self):
        self.assertEqual(self.pq.isempty(), False)

    def test_enqueue_empty(self):
        self.pqe.enqueue("endor")
        self.assertEqual(self.pqe.peeklastin(), "endor")

    def test_enqueue_not_empty(self):
        self.pq.enqueue("yavin")
        self.assertEqual(self.pq.peeklastin(), "yavin")

    def test_dequeue_empty(self):
        self.assertEqual(self.pqe.dequeue(), "Queue already empty!")

    def test_dequeue_not_empty(self):
        self.assertEqual(self.pq.dequeue(), "corusant")

    def test_size_empty(self):
        self.assertEqual(self.pqe.size(), 0)

    def test_size_not_empty(self):
        self.assertEqual(self.pq.size(), 3)

    def test_show_empty(self):
        self.assertEqual(self.pqe.show(), deque([]))

    def test_show_not_empty(self):
        self.assertEqual(self.pq.show(), deque(['geonosis', 'umbara', 'corusant']))



