import os
import markdown
import logging
from typing import List

from post import Post


TEMPLATE_FILE = 'template.html'
OUTPUT_DIR = 'output'

logging.basicConfig(level=logging.DEBUG)


class PostGenerator:
    "Class to generate blog posts"
    def __init__(self):
        self.posts = []

        if os.path.isdir(OUTPUT_DIR):
            return 

        logging.info('Output directory did not exist')
        logging.info('Creating output directory....')
        os.mkdir(OUTPUT_DIR)
        logging.info('Done.')

        
    def generate(self, posts: List[Post]):
        for post in posts:
            self.generate_post(post)
            self.posts.append(post)
        self.generate_index() 
            

    def generate_post(self, post: Post):
        content = markdown.markdown(post.body)
        filename, _ = os.path.splitext(post.filename)
        
        with open(TEMPLATE_FILE) as file:
            template = file.read()

        template = template.replace('{{ title }}', post.title)
        template = template.replace('{{ content }}', content)
        
        html_filename = f'{filename}.html'
        path = os.path.join(OUTPUT_DIR, html_filename)
        with open(path, 'w') as html_file:
            html_file.write(template)

    def generate_index(self):
        # TODO: Look at jinja to see how generating 
        # index can be done. 
        # Might end up writing a templating library before
        # it is all over with
        print("Can't generate index yet")  
