# Simple Site Generator

## Introductin 
Simple Site Generator is a simple static site generator written 
in Python. It's purpose is to learn how static site generators
work and to create a personal blog and portfolio site. 

It is composed of a single script `build.py`. `build.py`
looks for a folder called `posts`. Inside of `posts` are several
Markdown files that will be generated and placed inside of another
folder called `output`.

`build.py` uses a file called `template.html` to as a base template
for the site. Inside of `template.html` you include other files such as
css and javascript. 

At the top of each Markdown file are a list of headers. Each header is 
a name, followed by a : followed by it's value. Everything from the : to 
the end of the line is the value for the header. Metadata is stored in 
the header. 

The following headers are required: 
* author
* date
* title 

After the headers are completed, insert a blank line. The rest of the file will
be interpreted as markdown. The generated html will be inserted into the 
body of the template web page. 

## Installation 

Make sure you have Pyhton 3.9 installed. Install `pipenv` as the package manager. 
Run `pipenv update` to install all of the dependencies and `pipenv shell` to activate
the virtual environment. 

## Usage
Run `python generate.py`. Make sure you have a posts directory with at least one post