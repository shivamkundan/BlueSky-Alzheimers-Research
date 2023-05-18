# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os
# import kivy
sys.path.insert(0,os.path.abspath('./../'))


# sys.path.append(os.path.abspath('../pics/'))
# sys.path.append(os.path.abspath('../fonts/'))
# sys.path.append(os.path.abspath('../layout_files/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "BlueSky Alzheimer's Research"
copyright = '2023, Shivam Kundan'
author = 'Shivam Kundan'
release = '0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['sphinx.ext.autodoc']
# extensions = ['sphinx.ext.autodoc']
extensions = ['autoapi.extension']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autoapi_dirs = ['../']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'
html_static_path = ['_static']
