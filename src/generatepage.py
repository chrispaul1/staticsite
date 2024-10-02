import os, shutil
from markdown_block import markdown_to_html_nodes
def extract_header(markdown):
        lines = markdown.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("# "):
                return line.lstrip("#").strip()
        raise Exception("No Valid Header")

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
    template_content = template_content.replace("{{ Title }}",title_header)
    template_content = template_content.replace("{{ Content }}",file_html)
    dest_path_dirs = os.path.dirname(dest_path)
    if dest_path_dirs != "":
        os.makedirs(dest_path_dirs,exist_ok=True)
    with open(dest_path,"w+") as file:
        file.write(template_content)
    
def generate_page_recursive(dir_path_content,template_path,dest_dir_path):

    if os.path.exists(dir_path_content):
        dir_files = os.listdir(dir_path_content)
        for file in dir_files:
            file_path = os.path.join(dir_path_content,file)
            if os.path.isfile(file_path) and file.endswith(".md"):
                file_name = file.split(".")
                new_dest_file_path = os.path.join(dest_dir_path,file_name[0]+".html")
                generate_page(file_path,template_path,new_dest_file_path)
            elif os.path.isdir(file_path):
                new_dest_dir_path = os.path.join(dest_dir_path,file)
                generate_page_recursive(file_path,template_path,new_dest_dir_path)
        

