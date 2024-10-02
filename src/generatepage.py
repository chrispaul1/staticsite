import os, shutil
from markdown_block import markdown_to_html_nodes
from extractheader import extract_header

def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if os.path.exists(from_path):
        with open(from_path,"r") as file:
            file_content = file.read()
    if os.path.exists(template_path):
        with open(template_path,"r") as file:
            template_content = file.read()
    markdown_node = markdown_to_html_nodes(file_content)
    file_html = markdown_node.to_html()
    title_header = extract_header(file_content)
    template_header = template_content.replace("{{ Title }}",title_header)
    print(template_header)
    template_content = template_content.replace("{{ Content }}",file_html)
    dirs = os.path.dirname(dest_path)
    with open(dest_path,"w+") as file:
        file.write(template_content)
