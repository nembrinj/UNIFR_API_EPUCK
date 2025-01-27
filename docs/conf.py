# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../unifr_api_epuck'))


# -- Project information -----------------------------------------------------

project = 'UNIFR API E-puck'
copyright = '2022, David Roman Frischer & Vincent Carrel'
author = 'David Roman Frischer & Vincent Carrel'

# The full version, including alpha/beta/rc tags
release = '1.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosectionlabel'
]
add_module_names = False

autodoc_member_order = 'bysource'
autodoc_mock_imports = ['PIL',
                        'socket',
                        'time',
                        'sys',
                        'smbus2',
                        'VL53L0X',
                        'subprocess',
                        'cv2',
                        'threading',
                        'math',
                        'numpy',
                        'os',
                        'torch',
                        '.models',
                        'struct',
                        'logging',
                        'warnings',
                        'random',
                        'torchvision',
                        'copy', 
                        'Flask-Cors',
                        'Flask-SocketIO',
                        'simple-websocket',
                        'socket',
                        'socketio',
                        'controller']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'Icon']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']