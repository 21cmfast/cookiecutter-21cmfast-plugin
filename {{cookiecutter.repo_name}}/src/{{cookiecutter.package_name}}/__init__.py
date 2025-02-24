from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("{{ cookiecutter.package_name }}")
except PackageNotFoundError:
    # package is not installed
    pass

{%- if cookiecutter.c_extension_support == 'yes' %}

from .{{ cookiecutter.c_extension_module }} import ffi as _ffi
from .{{ cookiecutter.c_extension_module }} import lib as _lib


def my_c_function(args):
    args = [_ffi.new('char[]', arg) for arg in args]
    result = _lib.my_c_function(len(args), _ffi.new('char *[]', args))
    if result == _ffi.NULL:
        return ''
    else:
        return _ffi.string(result)

{%- if cookiecutter.c_extension_optional == 'yes' %}
try:
    from .{{ cookiecutter.c_extension_module }} import my_c_function  # noqa
except ImportError:
    def {{ cookiecutter.c_extension_function }}(args):
        return max(args, key=len)
{%- else %}
from .{{ cookiecutter.c_extension_module }} import my_c_function  # noqa
{%- endif %}
{%- endif %}
