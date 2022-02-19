# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('_themes'))
sys.path.append(os.path.abspath('..'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'jpexample',
    'sitemap'
]
templates_path = ['_templates']
source_suffix = '.rst'
# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'JMESPath'
copyright = u'2014-2015, James Saryerwinnie'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

html_theme = 'jmespath'
html_title = 'JMESPath'
html_theme_path = ['_themes']

html_theme_options = {
    "base_url": "https://jmespath.org",
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'JMESPathdoc'

html_sidebars = {
    'index': ['mainlinks.html', 'searchbox.html'],
    #'examples': ['logo-sidebar.html', 'searchbox.html'],
    '**': ['logo-sidebar.html', 'localtoc.html', 'searchbox.html']
}
html_additional_pages = {'index': 'index.html'}
