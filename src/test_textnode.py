import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_test(self):
        node = TextNode("This is a text node 1","bold")
        node2 = TextNode("This is a text node 2","bold")
        self.assertNotEqual(node,node2)
    
    def test_text_type(self):
        node = TextNode("This is a text node 1","bold","www.yeet.com")
        node2 = TextNode("This is a text node 1","italic","www.yeet.com")
        self.assertNotEqual(node,node2)

    def test_url(self):
        node = TextNode("This is a text node 1","bold","www.yeet.com")
        node2 = TextNode("This is a text node 1","bold","www.yeat.com")
        self.assertNotEqual(node,node2)

class TestTextNodeToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("Test text",text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,None)
        self.assertEqual(html_node.value,node.text)
    
    def test_image(self):
        node = TextNode("Test Image", text_type_image, "www.testimage.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.props,{"src":"www.testimage.com","alt":"Test Image"})
    
    def test_bold(self):
        node = TextNode("Bold Text",text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value,"Bold Text")



if __name__ == "__main__":
    unittest.main()