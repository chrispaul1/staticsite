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
from markdown_convert import (
    split_nodes_delimiter, 
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image
)

class TestMarkdownToTextNode(unittest.TestCase):
    def test_new_nodes(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        test_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        self.assertListEqual(new_nodes,test_nodes)
    
    def test_bold_node(self):
        node = TextNode("This is a **Bold Text** test",text_type_text)
        new_nodes = split_nodes_delimiter([node],"**",text_type_bold)
        test_nodes = [
            TextNode("This is a ", text_type_text),
            TextNode("Bold Text",text_type_bold),
            TextNode(" test",text_type_text)
        ]
        self.assertListEqual(new_nodes,test_nodes)
    
    def test_multiple_words(self):
        node = TextNode("This is a **Bold word** and a *italic word*",text_type_text)
        test_nodes = [
            TextNode("This is a ", text_type_text),
            TextNode("Bold word",text_type_bold),
            TextNode(" and a ",text_type_text),
            TextNode("italic word",text_type_italic)
        ]
        new_nodes = split_nodes_delimiter([node],"**",text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes,"*",text_type_italic)
        self.assertListEqual(new_nodes,test_nodes)
    
class TestExtractMarkdown(unittest.TestCase):
    def test_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertListEqual(extract_markdown_images(text),[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_markdown_link(self):
        text = " Test link for function [test text](www.yeet.com) and [link text](www.whatsup.com)"
        self.assertListEqual(extract_markdown_links(text),[("test text","www.yeet.com"),("link text","www.whatsup.com")])

class TestSplitImageAndLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,)
        new_nodes = split_nodes_link([node])
        return_nodes = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(new_nodes,return_nodes)

    def test_split_image(self):
        node = TextNode("This is a image test ![image name](www.img.com) and ![another image](www.yeet.com)",
                    text_type_text)
        new_nodes = split_nodes_image([node])
        return_nodes = [
            TextNode("This is a image test ",text_type_text),
            TextNode("image name",text_type_image,"www.img.com"),
            TextNode(" and ",text_type_text),
            TextNode("another image",text_type_image,"www.yeet.com")
        ]
        self.assertListEqual(new_nodes,return_nodes)
        