import os
import markdown
import logging

from post import Post


TEMPLATE_FILE = 'template.html'
OUTPUT_DIR = 'output'
logging.basicConfig(level=logging.DEBUG)


class PostGenerator:
    "Class to generate blog posts"
    def __init__(self):
        if os.path.isdir(OUTPUT_DIR):
            return 

        logging.info('Output directory did not exist')
        logging.info('Creating output directory....')
        os.mkdir(OUTPUT_DIR)
        logging.info('Done.')

        self.posts = []

    def generate(self):
        pass 

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
        pass

    

