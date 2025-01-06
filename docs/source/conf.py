import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Quantum-NFL'
copyright = '2025, G. & C.'
author = 'G. & C.'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_title = "Quantum-NFL Documentation"
html_favicon = '_static/favicon.ico'
html_logo = '_static/logo.png'

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
