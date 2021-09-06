# -*- coding: utf-8 -*-
from __future__ import unicode_literals

{% if cookiecutter.sphinx_theme == 'sphinx-rtd-theme' -%}
import os
{% endif -%}
import traceback
{%- if cookiecutter.sphinx_theme != 'sphinx-rtd-theme' -%}
import {{ cookiecutter.sphinx_theme|replace('-', '_') }}
{% endif %}

extensions = [
    'sphinx.ext.autodoc',
    "sphinx.ext.intersphinx",
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    "sphinx.ext.mathjax",
    "sphinx.ext.autosectionlabel",
    "numpydoc",
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
]
source_suffix = '.rst'
master_doc = 'index'
project = {{ '{0!r}'.format(cookiecutter.project_name) }}
year = '{% if cookiecutter.year_from == cookiecutter.year_to %}{{ cookiecutter.year_from }}{% else %}{{ cookiecutter.year_from }}-{{ cookiecutter.year_to }}{% endif %}'
author = {{ '{0!r}'.format(cookiecutter.full_name) }}
copyright = '{0}, {1}'.format(year, author)
try:
    from pkg_resources import get_distribution
    version = release = get_distribution('{{ cookiecutter.package_name }}').version
except Exception:
    traceback.print_exc()
    version = release = {{ '{0!r}'.format(cookiecutter.version) }}

pygments_style = 'trac'
templates_path = ['_templates']
extlinks = {
    'issue': ('https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues/%s', '#'),
    'pr': ('https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/pull/%s', 'PR #'),
}

{%- if cookiecutter.sphinx_theme != 'sphinx-rtd-theme' %}
html_theme = "{{ cookiecutter.sphinx_theme|replace('-', '_') }}"
html_theme_path = [{{ cookiecutter.sphinx_theme|replace('-', '_') }}.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/'
}
{%- else %}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = 'sphinx_rtd_theme'
{%- endif %}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False


autosectionlabel_prefix_document = True

autosummary_generate = True
numpydoc_show_class_members = False


exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "templates",
    "**.ipynb_checkpoints",
]

# -- External mapping ------------------------------------------------------------
python_version = ".".join(map(str, sys.version_info[0:2]))
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "python": ("https://docs.python.org/" + python_version, None),
    "matplotlib": ("https://matplotlib.org", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "sklearn": ("https://scikit-learn.org/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "21cmfast": ("https://21cmfast.readthedocs.io/en/latest/", None),
    "21cmmc": ("https://21cmmc.readthedocs.io/en/latest/", None),   
}
