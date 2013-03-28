# -*- coding: utf-8 -*-
import sys, os

# -- General configuration -----------------------------------------------------
extensions = ['sphinx.ext.todo', 'sphinxcontrib.spelling']

spelling_lang='en_AU'
spelling_word_list_filename='OK_wordlist.txt'
spelling_show_suggestions=True

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'SAR-Scenarios'
copyright = u'2013, CanberraUAV'

version = '0.1'
release = '0.1'
exclude_trees = ['_build']
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'SARScenarioDoc'

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
  ('index', 'SARScenarios.tex', u'Scenarios for employing UAVs in Search And Rescue situations',
   u'CanberraUAV', 'manual'),
]


