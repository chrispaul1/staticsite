import re
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"
from htmlnode import HTMLNode,ParentNode
from textnode import (
    TextNode, 
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node
)
from markdown_convert_line import text_to_textnode

def markdowns_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    blocks = [i for i in blocks if i != ""]
    blocks = list(map(lambda x: x.strip(),blocks))
    return blocks

def block_to_block_type(text):
    text_lines = text.splitlines()
    text_lines = [i for i in text_lines if i != ""]
    if len(text_lines) > 0:
        if re.match(r"^#{1,6} \w",text_lines[0]):
            return block_type_heading
        code_line = " ".join(text_lines)
        if re.match(r"^```(.*)```$",code_line):
            return block_type_code
    
    for i in range(0,len(text_lines)):
        if re.match(r"^>",text_lines[i]):
            if i == len(text_lines)-1:
                return block_type_quote
            continue
        else:
            break
    
    for i in range(0,len(text_lines)):
        if re.match(r"^(\* |- )",text_lines[i]):
            if i == len(text_lines)-1:
                return block_type_ulist
            continue
        else:
            break
    
    order_num = 0
    for i in range(0,len(text_lines)):
        if re.match(r"^\d{1}. ",text_lines[i]):
            number = int(re.search(r"^\d{1}",text_lines[i]).group())
            if number <= order_num:
                break
            else:
                order_num = number
            if i == len(text_lines)-1:
                return block_type_olist
            continue
        else:
            break
    
    return block_type_paragraph

def markdown_to_html_nodes(markdown):
    markdown_blocks = markdowns_to_blocks(markdown)
    children_nodes = []
    for block in markdown_blocks:
        node = return_html_node(block)
        children_nodes.append(node)
    return ParentNode("div",children_nodes)


def return_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        lines = block.split("\n")
        lines = map(str.strip,lines)
        paragraph_line = " ".join(lines)
        child_nodes = text_textnode_htmlnodes(paragraph_line)
        return ParentNode("p",child_nodes)
    
    if block_type == block_type_heading:
        headerCount = 0
        for char in block:
            if char == "#":
                headerCount+=1
            else:
                break
        block = block[headerCount+1:]
        child_nodes = text_textnode_htmlnodes(block)
        
        return ParentNode(f"h{headerCount}",child_nodes)
    
    if block_type == block_type_code:
        lines = block.split("\n")
        if lines[0].startswith("```") and lines[-1].startswith("```"):
            code_lines = " ".join(lines[1:-1])
        else:
            raise Exception("Invalid Code Markdown")
        child_nodes = ParentNode("code",text_textnode_htmlnodes(code_lines))
        return ParentNode("pre",[child_nodes])
    
    if block_type == block_type_quote:
        lines = block.split("\n")
        for line in lines:
            if line.startswith(">"):
                continue
            else:
                raise Exception("Invalid Quote Markdown")
        
        new_lines = [line[1:].strip() for line in lines]
        new_text = " ".join(new_lines)
        child_nodes = text_textnode_htmlnodes(new_text)
        return ParentNode("blockquote",child_nodes)

    if block_type == block_type_ulist:
        lines = block.split("\n")
        for line in lines:
            if line.startswith("* ") or line.startswith("- "):
                continue
            else:
                raise Exception("Invalid Unordered list")
        new_lines = [line[2:] for line in lines]
        child_nodes = []
        for line in new_lines:
            node = text_textnode_htmlnodes(line)
            child_nodes.append(ParentNode("li",node))
        return ParentNode("ul",child_nodes)
    
    if block_type == block_type_olist:
        lines = block.split("\n")
        child_nodes = []
        for line in lines:
            node = text_textnode_htmlnodes(line[3:])
            child_nodes.append(ParentNode("li",node))
        return ParentNode("ol",child_nodes)

def text_textnode_htmlnodes(text):
    textnodes = text_to_textnode(text)
    new_nodes = []
    for textnode in textnodes:
        html_node = text_node_to_html_node(textnode)
        new_nodes.append(html_node)
    return new_nodes
