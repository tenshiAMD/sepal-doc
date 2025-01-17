# -*- coding: utf-8 -*-

"""
ReST directive for dynamically change the value of the "edit this page btn". only compatblie with the current theme.
The directive require the complete raw file path (from github).
Example::
    .. custom-edit:: https://raw.githubusercontent.com/openforis/sepal-doc/custom_edit/README.rst
"""

from docutils import nodes
from docutils.parsers.rst import Directive, directives

class CustomEdit(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    html = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            var div = document.getElementsByClassName("tocsection editthispage")[0];
            var link = div.getElementsByTagName("a")[0];
            link.href = "{}";
        }});  
    </script>
    """
    
    def run(self):
        
        # get the raw link 
        raw_link = directives.uri(self.arguments[0])
        
        # transform it into an edit link 
        raw = "raw.githubusercontent.com"
        github = "github.com"
        edit = "edit"
        list_ = raw_link.replace(raw, github).split("/")
        list_.insert(5, edit)
        link = "/".join(list_)
        
        return [nodes.raw('', self.html.format(link), format='html')]
    
def setup(builder):
    directives.register_directive('custom-edit', CustomEdit)
        
