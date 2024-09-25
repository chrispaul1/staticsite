import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node_props = {
            "href": "www.yett.com", 
            "target": "_blank",
        }

        node2_props = {
            "href": "www.yett.com", 
            "target": "_blank",
        }
        node = HTMLNode("p","test string",["hello"],node_props)
        node2 = HTMLNode("p","test string",["hello"],node2_props)
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node_props = {
            "href": "www.yett.com", 
            "target": "_blank",
        }

        node = HTMLNode("p","test string",["hello"],node_props)
        node.props_to_html()
        self.assertEqual(node.props_to_html(),' href="www.yett.com" target="_blank"')
    
    def test_repr(self):
        node_props = {
            "href": "www.yett.com", 
            "target": "_blank",
        }

        node = HTMLNode("p","test string",["hello"],node_props)
        self.assertEqual(node.__repr__(),
                         "tag: p, value: test string, children: ['hello'], props: {'href': 'www.yett.com', 'target': '_blank'}")

    def test_Leaf_to_html(self):
        node = LeafNode("p","This is a paragraph of Text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node.to_html(),"<p>This is a paragraph of Text.</p>")
        self.assertEqual(node2.to_html(),'<a href="https://www.google.com">Click me!</a>')
    
    def test_Leaf_no_tag(self):
        node = LeafNode(None,"This is a paragraph of Text.")
        self.assertEqual(node.to_html(),"This is a paragraph of Text.")
    
    def test_Leaf_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_Parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_multiple_parent(self):
        test_parent = ParentNode(
            "h1",
            [
                LeafNode("b","Bold Text"),
                LeafNode("i","italic text")
            ]
        )
        node = ParentNode(
            "p",
            [
                test_parent,
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
         

if __name__ == "__main__":
    unittest.main()