{%- if cookiecutter.command_line_interface == 'yes' %}
from click.testing import CliRunner
from {{ cookiecutter.package_name }}.cli import main
{%- endif %}


def test_main():

{%- if cookiecutter.command_line_interface == 'yes' %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
{%- else %}
    pass
{%- endif %}

