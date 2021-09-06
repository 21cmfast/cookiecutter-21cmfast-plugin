========
Overview
========
.. start-badges

.. list-table::
    :stub-columns: 1
{% if cookiecutter.sphinx_docs == "yes" %}
    * - docs
      - |docs|
{%- endif %}
    * - tests
          |codecov|
        {{ '' }}
{{ '' }}
    * - package
      - {% if cookiecutter.pypi_badge == "yes" %}| |version| |wheel| |supported-versions| |supported-implementations|
        {{ '' }}{% endif %}
        |commits-since|
{{ '' }}
{%- if cookiecutter.sphinx_docs == "yes" -%}
{%- if 'readthedocs' in cookiecutter.sphinx_docs_hosting -%}
.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/
    :alt: Documentation Status
{% endif %}
{% endif %}
.. |codecov| image:: https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
{%- if cookiecutter.codeclimate == 'yes' %}
.. |codeclimate| image:: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badges/gpa.svg
   :target: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
   :alt: CodeClimate Quality Status
{% endif %}
{%- if cookiecutter.pypi_badge == "yes" %}
.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported versions
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}
{% endif %}
.. |commits-since| image:: https://img.shields.io/github/commits-since/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter.version }}.svg
    :alt: Commits since latest release
    :target: https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter.version }}...master

.. end-badges

{{ cookiecutter.project_short_description|wordwrap(100) }}
* Free software: MIT

Installation
============

::

    pip install {{ cookiecutter.distribution_name }}

You can also install the in-development version with::
    pip install https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/archive/master.zip

Documentation
=============

{% if cookiecutter.sphinx_docs == "yes" %}
{{ cookiecutter.sphinx_docs_hosting }}
{% else %}
To use the project:

.. code-block:: python

    import {{ cookiecutter.package_name }}
    {{ cookiecutter.package_name }}.{{ cookiecutter.c_extension_function }}()
{% endif %}

Development
===========

Clone the repo and install with::

    pip install -e {{  cookiecutter.distribution_name }}[dev]