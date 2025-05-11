# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
# This file does only contain a selection of the most common options. For a# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory, add these directories to sys.path here.
# If the directory is relative to the documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
import mock
import package_variables as variables

# -- Project information -----------------------------------------------------

project = variables.long_name
copyright = variables.author_copyright
author = variables.author
title = variables.pdf_title

version = variables.short_version  # short X.Y version
release = variables.long_version  # full version, including alpha/beta/rc tags

DOC_SOURCES_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(DOC_SOURCES_DIR))
sys.path.insert(0, DOC_SOURCES_DIR)

# Hack for lacking git-lfs support ReadTheDocs
if os.environ.get('READTHEDOCS', None):
    from git_lfs import fetch
    fetch(PROJECT_ROOT_DIR)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be # extensions coming with Sphinx (named
# 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinxarg.ext'
]

# The master toc tree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_favicon = 'images/plugin_logo.PNG'

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples (source start file, name, description, authors, manual section).
man_pages = [(master_doc, project, title, author, 1)]

# -- Other

MOCK_MODULES = ['cqp_resources_rc', 'osgeo', 'qgis', 'qgis.core', 'qgis.gui', 'qgis.utils',
                'qgis.PyQt.uic', 'qgis.PyQt.QtWidgets', 'qgis.PyQt.QtGui', 'qgis.PyQt.QtCore', 'PyQt5']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()
