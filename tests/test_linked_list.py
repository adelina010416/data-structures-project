import unittest
from src.linked_list import LinkedList


class TestLl(unittest.TestCase):
    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 1})
        ll.insert_beginning({'id': 0})
        self.assertIs(ll.tail.next_node, None)
        with self.assertRaises(Exception):
            ll.insert_beginning('idusername')
            ll.insert_beginning([1, 2, 3])

    def test_str(self):
        ll = LinkedList()
        self.assertEqual(str(ll), 'None')
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> None")

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        self.assertEqual(ll.tail.data, {'id': 2})
        self.assertEqual(ll.head.data, {'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertIs(ll.tail.next_node, None)
        with self.assertRaises(Exception):
            ll.insert_at_end('idusername')
            ll.insert_at_end([1, 2, 3])

    def test_to_list(self):
        ll = LinkedList()
        self.assertEqual(ll.to_list(), "None")
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(ll.to_list(), [{'id': 0, 'username': 'serebro'},
                                        {'id': 1, 'username': 'lazzy508509'},
                                        {'id': 2, 'username': 'mik.roz'}])

    def test_get_by_id(self):
        ll = LinkedList()
        with self.assertRaises(TypeError):
            ll.get_data_by_id('ds')
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll.get_data_by_id(2), 'DataNotFound')

