import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertIs(queue.tail.next_node, None)
        with self.assertRaises(AttributeError):
            print(queue.tail.next_node.data)

    def test_str(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        self.assertEqual(str(queue), "data1\ndata2")

    def test_dequeue(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertIs(queue.dequeue(), None)
