from typing import Dict
from datetime import date

class Post:
    def __init__(self, filename, headers: Dict, body: str):
        self.title = headers['title'] 
        self.author = headers['author']
        self.date = date.fromisoformat(headers['date'])
        self.filename = filename

        self.body = body

    def __str__(self) -> str: 
        return f'{self.title} by {self.author}' 