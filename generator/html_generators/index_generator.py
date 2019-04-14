#!/usr/bin/python3
"""
Generate index.html code
"""


class IndexGenerator():
    """
    Class for generating html files
    """

    FOLDER_IN_HTDOCS = ""


    def __init__(self, env):
        self.jinja = env
        self.filename = "index.html"



    def execute(self, header_data):
        """
        Main method of class. Generates html code.
        """
        return self.filename, self.generate_html_code(header_data)



    def generate_html_code(self, header_data):
        """
        Use jinja2 to generate html files
        """
        template = self.jinja.get_template("index.html")
        return template.render(**header_data)



if __name__ == "__main__":
    pass
