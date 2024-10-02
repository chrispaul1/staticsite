import shutil
from textnode import TextNode
import os
from extractheader import extract_header
from generatepage import generate_page

def copy_dir_recursive(src_path,dst_path):
   
    if os.path.isdir(src_path):
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)

        for filename in os.listdir(src_path):
            src_file_path = os.path.join(src_path,filename)
            dst_dir_path = os.path.join(dst_path,filename)
            if os.path.isfile(src_file_path):
                shutil.copy(src_file_path,dst_path)
            elif os.path.isdir(src_file_path):
                copy_dir_recursive(src_file_path,dst_dir_path)

content_path = "./content/index.md"
template_path = "./template.html"
dest_path = "./public/index.html"

def main():
    src_dir = "./static"
    dst_dir = "./public"
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    copy_dir_recursive(src_dir,dst_dir)
    generate_page(content_path,template_path,dest_path)

main()