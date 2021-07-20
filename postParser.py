from post import Post
import os
from typing import Dict
    
def parse(path) -> Post:
    "Parses file and returns a Post"
    
    with open(path) as file:
        headers = parse_headers(file)
        content = parse_content(file)
        filename = os.path.basename(path)
        return Post(filename, headers, content)
    
def parse_headers(file) -> Dict:
    "Parses headers from file. Call before parse_content"
    headers = {}
    headerLine = file.readline().strip()
    while headerLine: 
        name, value = headerLine.split(':')
        name = name.strip()
        value = value.strip()
        headers[name] = value
        headerLine = file.readline().strip()
    return headers 

def parse_content(file) -> str:
    "Parses markdown content. Call after parse_headers"
    return file.read()