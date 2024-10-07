import unittest

from textnode import (TextNode, 
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq_two(self):
        node = TextNode("This should be text", "italic","www.Bootsrules.com")
        node2 = TextNode("This should be text", "italic","www.Bootsrules.com") 
        self.assertEqual(node, node2)
    def test_noteq_(self):
        node = TextNode("This is different", "code", "www.cars.com")
        node2 = TextNode("This is also different", "image", "www.ucla.com")
        self.assertNotEqual(node, node2)
    def test_eq_3(self):
        node = TextNode("This should be text", "italic")
        node2 = TextNode("This should be text", "italic", None) 
        self.assertEqual(node, node2)
    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
        print("TESTTEXTNODE", repr(node))


if __name__ == "__main__":
    unittest.main()
