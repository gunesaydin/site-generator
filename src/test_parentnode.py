import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        child_node = LeafNode("p", "This is a child node")
        child_node_2 = LeafNode("p", "This is another child node")
        parent_node = ParentNode("ul", [child_node, child_node_2])
        control_string = "<ul><p>This is a child node</p><p>This is another child node</p></ul>"
        self.assertEqual(control_string, parent_node.to_html())

    def test_to_html_alt(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        control_string = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        self.assertEqual(node.to_html(), control_string)

    def test_to_html_nested_nodes(self):
        nested_parent_node = ParentNode("ol", [LeafNode("p", "This is nested paragraph", { "href" : "https://boot.dev" })])
        parent_node_1 = ParentNode("ul", [nested_parent_node])
        control_string = "<ul><ol><p href=\"https://boot.dev\">This is nested paragraph</p></ol></ul>"

        self.assertEqual(parent_node_1.to_html(), control_string)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )