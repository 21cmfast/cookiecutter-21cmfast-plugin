#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup

{%- if cookiecutter.c_extension_support == 'yes' %}
CFLAGS = ''
LFLAGS = ''



{%- if cookiecutter.c_extension_optional == 'yes' %}
class optional_build_ext(build_ext):
    """Allow the building of C extensions to fail."""
    def run(self):
        try:
            build_ext.run(self)
        except Exception as e:
            self._unavailable(e)
            self.extensions = []  # avoid copying missing files (it would fail).

    def _unavailable(self, e):
        print('*' * 80)
        print('''WARNING:

    An optional code optimization (C extension) could not be compiled.

    Optimizations for this package will not be available!
        ''')

        print('CAUSE:')
        print('')
        print('    ' + repr(e))
        print('*' * 80)
{%- endif %}
{% endif %}


setup(
{%- if cookiecutter.c_extension_support != 'no' -%}
{%- if cookiecutter.c_extension_optional == 'yes' %}
    cmdclass={'build_ext': optional_build_ext},
{%- endif %}
    cffi_modules=[i + ':ffi' for i in glob('src/*/_*_build.py')],
{%- endif %}
    use_scm_version=True
)
