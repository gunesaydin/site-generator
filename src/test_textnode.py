import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_link_eq(self):
        node1 = TextNode("", TextType.LINK, None)
        node2 = TextNode("", TextType.LINK)
        self.assertEqual(node1, node2)

    def test_types_not_eq(self):
        node1 = TextNode("", TextType.IMAGE)
        node2 = TextNode("", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_texts_not_eq(self):
        node1 = TextNode("", TextType.ITALIC)
        node2 = TextNode(" ", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()