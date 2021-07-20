
import logging 
from typing import Dict

from post import Post 
from postGenerator import PostGenerator


BASE_TEMPLATE = 'template.html'
POSTS_DIR = 'posts'


if __name__ == '__main__':
    generator = PostGenerator()