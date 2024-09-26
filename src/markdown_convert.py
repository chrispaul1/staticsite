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
from htmlnode import HTMLNode,LeafNode,ParentNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes=[]
        node_splits = old_node.text.split(delimiter)
        if len(node_splits) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(0,len(node_splits)):
            if node_splits[i] == "":
                continue
            if i%2==0:
                split_nodes.append(TextNode(node_splits[i],text_type_text))
            else:
                split_nodes.append(TextNode(node_splits[i],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    image_list = []
    markdown_matches = re.findall(r"\!\[.*?\)",text)

    for match in markdown_matches:
        alt_text = re.search(r"\[(.*?)\]",match)
        url_text = re.search(r"\((.*?)\)",match)
        image_list.append((alt_text.group(1),url_text.group(1)))
    return image_list

def extract_markdown_links(text):
    link_list = []
    markdown_matches = re.findall(r"\[.*?\)",text)
    for match in markdown_matches:
        anchor_text = re.search(r"\[(.*?)\]",match)
        url_text = re.search(r"\((.*?)\)",match)
        link_list.append((anchor_text.group(1),url_text.group(1)))
    return link_list

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        node_splits = re.split(r"(\!\[.*?\))",old_node.text)
        for i in range(0,len(node_splits)):
            split_nodes=[]
            if node_splits[i] == "":
                continue
            if i%2 == 0:
                split_nodes.append(TextNode(node_splits[i],text_type_text))
            else:
                alt_text = re.search(r"\[(.*?)\]",node_splits[i])
                url_text = re.search(r"\((.*?)\)",node_splits[i])
                split_nodes.append(TextNode(alt_text.group(1),text_type_image,url_text.group(1)))
            new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        node_splits = re.split(r"(\[.*?\))",old_node.text)
        for i in range(0,len(node_splits)):
            split_nodes=[]
            if node_splits[i] == "" or node_splits[i] == '':
                continue
            if i%2 == 0:
                split_nodes.append(TextNode(node_splits[i],text_type_text))
            else:
                anchor_text = re.search(r"\[(.*?)\]",node_splits[i])
                url_text = re.search(r"\((.*?)\)",node_splits[i])
                split_nodes.append(TextNode(anchor_text.group(1),text_type_link,url_text.group(1)))
            new_nodes.extend(split_nodes)
    return new_nodes



