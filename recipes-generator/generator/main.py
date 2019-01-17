#!/usr/bin/python3
"""
Generate html-files for recipes
"""
from jinja2 import Environment, FileSystemLoader, select_autoescape

file_loader = FileSystemLoader("templates")
env = Environment(autoescape=select_autoescape(
    disabled_extensions=('txt',),
    default_for_string=True,
    default=True),
                  loader=file_loader
                  )


template = env.get_template("recipe.html")

output = template.render()
print(output)

if __name__ == "__main__":
    pass
