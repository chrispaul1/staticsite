import os

def extract_header(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line.lstrip("#").strip()
    raise Exception("No Valid Header")
