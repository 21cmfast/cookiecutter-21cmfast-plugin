from __future__ import print_function

import os
import shutil
import sys
from os.path import join

try:
    from click.termui import secho
except ImportError:
    warn = note = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)

    def note(text):
        for line in text.splitlines():
            secho(line, fg="yellow", bold=True)


def unlink_if_exists(path):
    if os.path.exists(path):
        os.unlink(path)

if __name__ == "__main__":
{% if cookiecutter.sphinx_docs == "no" %}
    shutil.rmtree('docs')
    os.unlink('.readthedocs.yml')
{%- elif 'readthedocs' not in cookiecutter.sphinx_docs_hosting %}
    os.unlink('.readthedocs.yml')
{% endif %}

{%- if cookiecutter.command_line_interface == 'no' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '__main__.py'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', 'cli.py'))
{% endif %}

{% if cookiecutter.c_extension_support == 'no' %}
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}.c'))
    os.unlink(join('src', '{{ cookiecutter.package_name }}', '{{ cookiecutter.c_extension_module }}_build.py'))
{% endif %}


    print("""
################################################################################
################################################################################

    You have succesfully created `{{ cookiecutter.repo_name }}`.

################################################################################

    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

    See .cookiecutterrc for instructions on regenerating the project.

################################################################################

    To get started run these:

        cd {{ cookiecutter.repo_name }}
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git tag v{{ cookiecutter.version }}
        git remote add origin git@github.com:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git
        git push -u origin master v{{ cookiecutter.version }}

    Then make a new isolated Python environment and then run

        pip install -e .[dev]
        pre-commit install
    {%- if cookiecutter.use_commitizen %}
        pre-commit install --hook-type commit-msg
    {%- endif %}
        pre-commit run -a

    {% if 'readthedocs' in cookiecutter.sphinx_docs_hosting %}
    To host your documentation on RTD, you need to import your project at
    https://readthedocs.org/dashboard/import/?
    {%- endif %}

    To automatically deploy to PyPI and TestPyPI in your CI, you'll need to get a 
    PyPI/TestPyPI token here: https://test.pypi.org/manage/account/token/ and then
    add it as a repo or organization secret on GitHub. If you've already got such a 
    token that has full project scope and have it as an organization secret, you can 
    skip this step.

    You are encouraged to go to https://github.com/apps/pre-commit-ci/installations/new
    to install pre-commit CI to do your CI linting, unless your org has already been
    added.
""")


    command_line_interface_bin_name = '{{ cookiecutter.command_line_interface_bin_name }}'
    while command_line_interface_bin_name.endswith('.py'):
        command_line_interface_bin_name = command_line_interface_bin_name[:-3]

        if command_line_interface_bin_name == '{{ cookiecutter.package_name }}':
            warn("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!                                                                            !!
!!      ERROR:                                                                !!
!!                                                                            !!
!!          Your result package is broken. Your bin script named              !!
!!          {0} !!
!!                                                                            !!
!!          Python automatically adds the location of scripts to              !!
!!          `sys.path`. Because of that, the bin script will fail             !!
!!          to import your package because it has the same name               !!
!!          (it will try to import itself as a module).                       !!
!!                                                                            !!
!!          To avoid this problem you have two options:                       !!
!!                                                                            !!
!!          * Remove the ".py" suffix from the `command_line_interface_bin_name`.                    !!
!!                                                                            !!
!!          * Use a different `package_name` {1} !!
!!                                                                            !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""".format(
                '"{{ cookiecutter.command_line_interface_bin_name }}" will shadow your package.'.ljust(65),
                '(not "{0}").'.format(command_line_interface_bin_name).ljust(32)))
            sys.exit(1)
        break
