import unittest

from htmlnode import *
html_hyperlink = "a"

properties = {"href": "https://www.google.com", "target": "_blank"}
testnode1 = HTMLNode(html_hyperlink, "This is the HTML text", None, properties)
testnode2 = HTMLNode("a", "This is the HTML text", None, properties)
leafnode1 = LeafNode("p", "This is a paragraph of text.")
leafnode2 = LeafNode("b", "This is some bold text")

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        test_node = HTMLNode("a", "This is the HTML text", None, properties)
        self.assertEqual(repr(test_node), repr(testnode2))
        
        
    def test_noteq(self):
        self.assertNotEqual(testnode1, testnode2)

    def test_props_to_html(self):
        props_test = testnode1.props_to_html()


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        test_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(repr(test_node), repr(leafnode1))

    def test_to_html(self):
        expected = "<b>This is some bold text</b>"
        testleafnode2 = leafnode2.to_html()
        self.assertEqual(testleafnode2, expected)

if __name__ == "__main__":
    unittest.main()
