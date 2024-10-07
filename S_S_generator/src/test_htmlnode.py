import unittest

from htmlnode import *

properties = {"href": "https://www.google.com", "target": "_blank"}
testnode1 = HTMLNode(html_hyperlink, "This is the HTML text", None, properties)
testnode2 = HTMLNode("a", "This is the HTML text", None, properties)

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        test_node = HTMLNode("a", "This is the HTML text", None, properties)
        self.assertEqual(repr(test_node), repr(testnode2))
        
        
    def test_noteq(self):
        self.assertNotEqual(testnode1, testnode2)

    def test_props_to_html(self):
        props_test = testnode1.props_to_html()
        print("TEST3PROP_HTML",repr(props_test))



if __name__ == "__main__":
    unittest.main()
