import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a joke node", TextType.ITALIC)
        node5 = TextNode("This is a joke node", TextType.ITALIC)
        node6 = TextNode("This is a joke node", TextType.ITALIC, "https://www.whoops.org")
        
        # Tests
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node1, node4)
        self.assertNotEqual(node2, node4)
        self.assertNotEqual(node3, node4)
        self.assertEqual(node4, node5)
        self.assertNotEqual(node4, node6)
        self.assertNotEqual(node5, node6)
        
        
if __name__ == "__main__":
    unittest.main()