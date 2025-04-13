import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("<p>", "Test paragraph", props={"test_prop": "test_value"})
        node2 = HTMLNode("<p>", "Test paragraph", props={"test_prop": "test_value"})
        self.assertEqual(node1, node2)

        node3 = HTMLNode("<ul>", children=[HTMLNode("<ol>", "Item")])
        node4 = HTMLNode("<ul>", children=[HTMLNode("<ol>", "Item")])
        self.assertEqual(node3, node4)

    def test_not_eq(self):
        node1 = HTMLNode("<p>", "Test paragraph", props={"test_prop": "test_value"})
        node2 = HTMLNode("<p>", "Test paragraph", props={"test_prop": "test_value2"})
        self.assertNotEqual(node1, node2)

        node3 = HTMLNode("<ul>", children=[HTMLNode("<ol>", "Item")])
        node4 = HTMLNode("<ul>", children=[HTMLNode("<ol>", "Item2")])
        self.assertNotEqual(node3, node4)

    def test_prop_to_html(self):
        node1 = HTMLNode("<p>", "Test paragraph", props={"test_prop": "test_value"})
        html_with_props1 = node1.props_to_html()
        control_html1 = f" test_prop=\"test_value\""
        self.assertEqual(html_with_props1, control_html1)

        node2 = HTMLNode("<p>", "Test paragraph", props={"test_prop": "test_value", "test_prop_2": "test_value_2"})
        html_with_props2 = node2.props_to_html()
        control_html2 = " test_prop=\"test_value\" test_prop_2=\"test_value_2\""
        self.assertEqual(html_with_props2, control_html2)

if __name__ == "__main__":
    unittest.main()