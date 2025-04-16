import os
import shutil
import sys

from textnode import TextNode, TextType
from markdown_blocks import markdown_to_html_node, extract_title

def main():
    basepath = sys.argv[1]
    if basepath == "":
        basepath = "/"

    dummy_node = TextNode("****** RUNNING ******", TextType.LINK, "https://boot.dev")
    print(dummy_node)
    copy_content_from_to("./static", "./docs")
    generate_pages_recursive('./content', './template.html', './docs', basepath)

def copy_content_from_to(src_path, dest_path):
    if not os.path.exists(src_path):
        print("ERROR: Source directory does not exist!")
        return
    if os.path.exists(dest_path):
        print(f"Removing: {dest_path}")
        shutil.rmtree(dest_path)
    print(f"Creating New: {dest_path}")
    os.mkdir(dest_path)

    source_files = os.listdir(src_path)
    print(f"Source Files ({src_path}): {source_files}")
    print(f"Copying files from: ({src_path}, to: ({dest_path}))")
    for path in source_files:
        print(f"PATH: {path}")
        if os.path.isfile(os.path.join(src_path, path)):
            print(f"FILE: {path}")
            shutil.copy(os.path.join(src_path, path), os.path.join(dest_path, path))
        else:
            print(f"DIR: {path}")
            copy_content_from_to(os.path.join(src_path, path), os.path.join(dest_path, path))
        
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    html_template = ""
    with open(from_path, 'r') as file:
        markdown = file.read()
    with open(template_path, 'r') as file:
        html_template = file.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    site_html = html_template.replace("{{ Title }}", title).replace("{{ Content }}", content).replace("href=\"/", f"href=\"{basepath}").replace("src=\"/", f"src=\"{basepath}")
    
    paths = dest_path.split("/")
    current_path = ""
    for i in range(0, len(paths) - 1):
        current_path = os.path.join(current_path, paths[i])
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(dest_path, 'a') as file:
        file.write(site_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    source_files = os.listdir(dir_path_content)
    for path in source_files:
        print(f"PATH: {path}")
        if os.path.isfile(os.path.join(dir_path_content, path)):
            if path.split('.')[1] == 'md':
                generate_page(os.path.join(dir_path_content, path), template_path, os.path.join(dest_dir_path, f"{path.split('.')[0]}.html"), basepath)
        else:
            print(f"DIR: {path}")
            generate_pages_recursive(os.path.join(dir_path_content, path), template_path, os.path.join(dest_dir_path, path), basepath)

main()