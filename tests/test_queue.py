import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        assert queue.head.data == 'data1'
        assert queue.head.next_node.data == 'data2'
        assert queue.tail.data == 'data3'
        assert queue.tail.next_node is None
        with self.assertRaises(AttributeError):
            print(queue.tail.next_node.data)

    def test_str(self):
        queue = Queue()
        assert str(queue) == "data1\ndata2\ndata3"
