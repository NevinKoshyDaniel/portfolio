# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Nevin's Sphinx Profile"
copyright = '2023-2025, Nevin K Daniel'
author = 'Nevin K Daniel'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

project = "Portfolio"
extensions = ['myst_parser', 'notfound.extension']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','.venv']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']

# Enable numref
numfig = True

# html_css_files = [
#     'css/output.css',
# ]

html_additional_pages = {
    'index': 'html/homepage.html',
}

import os
import shutil
def copy_files():
    print(os.listdir())
    print(os.path)
    shutil.copyfile('_static/css/output.css','build/_static/css/output.css')