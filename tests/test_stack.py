import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')  # data3
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            print(stack.top.next_node.next_node.next_node.data)

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop()
        self.assertIs(stack.top, None)
        self.assertEqual(data, 'data1')
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(data, 'data2')

    def test_str(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(str(stack), f'data3\ndata2\ndata1')
