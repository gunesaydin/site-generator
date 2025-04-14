import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_p(self):
        test_string = LeafNode("p", "This is a test").to_html()
        control_string = "<p>This is a test</p>"
        self.assertEqual(test_string, control_string)

    def test_to_html_p_with_single_prop(self):
        test_string = LeafNode("p", "This is a test", { "href" : "https://boot.dev"}).to_html()
        control_string = "<p href=\"https://boot.dev\">This is a test</p>"
        self.assertEqual(test_string, control_string)

    def test_to_html_p_with_multiple_props(self):
        test_string = LeafNode("p", "This is a test", { "href" : "https://boot.dev", "test_prop" : "test-value"}).to_html()
        control_string = "<p href=\"https://boot.dev\" test_prop=\"test-value\">This is a test</p>"
        self.assertEqual(test_string, control_string)

    def test_to_html_no_tag(self):
        test_string = LeafNode(None, "This is a test").to_html()
        control_string = "This is a test"
        self.assertEqual(test_string, control_string)

if __name__ == "__main__":
    unittest.main()