
import os
from postGenerator import PostGenerator
from postParser import parse 

import logging
logging.basicConfig(level=logging.DEBUG)


POSTS_DIR = 'posts'

def main():
    if not os.path.isdir(POSTS_DIR):
        print(f"Could not find '{POSTS_DIR}' directory")
        return 

    posts = []
    for post_file in os.listdir(POSTS_DIR):
        path = os.path.join(POSTS_DIR, post_file)
        logging.info(f'Parsing {post_file}...')
        posts.append(parse(path))
        logging.info('Done.')

    logging.info(f'Generating posts.')
    generator = PostGenerator()
    generator.generate(posts)
    logging.info('Done')

if __name__ == '__main__':
    main()