import unittest
from idlelib.sidebar import LineNumbers

from src.linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    def test_append_single_node(self):
        ll = LinkedList()
        ll.append("a")

        self.assertIsNotNone(ll.head)
        self.assertEqual(ll.head.data, "a")
        self.assertIsNone(ll.head.next)

    def test_append_multiple_nodes(self):
        ll = LinkedList()
        ll.append("a")
        ll.append("b")
        ll.append("c")

        self.assertEqual(ll.head.data, "a")
        self.assertEqual(ll.head.next.data, "b")
        self.assertEqual(ll.head.next.next.data, "c")
        self.assertIsNone(ll.head.next.next.next)

    def test_delete_existing_node(self):
        ll = LinkedList()
        ll.append("a")
        ll.append("b")
        ll.append("c")
        ll.delete("b")

        self.assertEqual(ll.head.data, "a")
        self.assertEqual(ll.head.next.data, "c")
        self.assertIsNone(ll.head.next.next)

    def test_delete_head_node(self):
        ll = LinkedList()
        ll.append("x")
        ll.append("y")
        ll.delete("x")

        self.assertEqual(ll.head.data, "y")
        self.assertIsNone(ll.head.next)

    def test_delete_non_existing_node(self):
        ll = LinkedList()
        ll.append("a")
        ll.append("b")
        ll.delete("x")

        self.assertEqual(ll.head.data, "a")
        self.assertEqual(ll.head.next.data, "b")

    def test_find_existing_node(self):
        ll = LinkedList()
        ll.append("a")
        ll.append("b")
        result = ll.find("b")

        self.assertIsNotNone(result)
        self.assertEqual(result.data, "b")

    def test_find_non_existing_node(self):
        ll = LinkedList()
        ll.append("a")
        ll.append("b")
        result = ll.find("y")

        self.assertIsNone(result)