import unittest
from markdown_block import (
    markdowns_to_blocks,
    block_to_block_type,
    block_type_paragraph ,
    block_type_heading ,
    block_type_code ,
    block_type_quote,
    block_type_olist ,
    block_type_ulist,
    markdown_to_html_nodes
)

class TestSplitMarkdown(unittest.TestCase):
    def test_split_markdown_to_blocks(self):
        test_string = """ 
# This is a heading 

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item 
"""
        block_list = markdowns_to_blocks(test_string)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ],block_list)
    
    def test_block_type(self):

        paragraph_text = "This is just a paragraph"
        heading_text = "## This is a heading"
        code_text = """
```code text
whast up yall
```
"""

        quote_text = """
> This a quote
> Another quote
> Last quote
"""

        unordered_list = """
* first text
^ second text
* third text
"""

        ordered_list = """
1. First
2. Second
3. Third
"""
        self.assertEqual(block_to_block_type(paragraph_text),"paragraph")
        self.assertEqual(block_to_block_type(heading_text),"heading")
        self.assertEqual(block_to_block_type(code_text),"code")
        self.assertEqual(block_to_block_type(quote_text),"quote")
        self.assertNotEqual(block_to_block_type(unordered_list),"unordered_list")
        self.assertEqual(block_to_block_type(ordered_list),"ordered_list")

    def test_markdown_paragraph(self):

        test_paragraph = """
This is a **test** paragraph 
yeet

# Heading 1

## Heading 2
"""
        test_node = markdown_to_html_nodes(test_paragraph)

        self.assertEqual(
            test_node.to_html(),
            "<div><p>This is a <b>test</b> paragraph yeet</p><h1>Heading 1</h1><h2>Heading 2</h2></div>"
            )
        
        test_paragraph2 = """
Another Paragraph **bold** text

This has *italic* and `code` words
"""

        test_node = markdown_to_html_nodes(test_paragraph2)
        self.assertEqual(
            test_node.to_html(),
            "<div><p>Another Paragraph <b>bold</b> text</p><p>This has <i>italic</i> and <code>code</code> words</p></div>"
        )

        test_lists = """
- This is a list
- yeet
- yep *man*

1. Ordered list
2. Item 2 `code block`
3. Item 3
""" 
        test_node = markdown_to_html_nodes(test_lists)
        self.assertEqual(test_node.to_html(),
                        "<div><ul><li>This is a list</li><li>yeet</li><li>yep <i>man</i></li></ul><ol><li>Ordered list</li><li>Item 2 <code>code block</code></li><li>Item 3</li></ol></div>")
        
        test_quote ="""
> Quote section
> Another one

Paragraph text

"""
        test_node = markdown_to_html_nodes(test_quote)
        self.assertEqual(test_node.to_html(),
                        "<div><blockquote>Quote section Another one</blockquote><p>Paragraph text</p></div>")

        test_code ="""
```
This is a test code block
whats up
```
"""
        test_node = markdown_to_html_nodes(test_code)
        self.assertEqual(test_node.to_html(),
                "<div><pre><code>This is a test code block whats up</code></pre></div>")