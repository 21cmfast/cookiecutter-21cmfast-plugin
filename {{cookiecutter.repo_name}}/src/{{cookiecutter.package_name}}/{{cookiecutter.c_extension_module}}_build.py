from os.path import dirname
from os.path import join

from cffi import FFI

ffi = FFI()
ffi.cdef('''
    char* my_c_function();
''')

ffi.set_source(
    '{{ cookiecutter.package_name }}.{{ cookiecutter.c_extension_module }}',
    open(join(dirname(__file__), '{{ cookiecutter.c_extension_module }}.c')).read()
)

if __name__ == '__main__':
    ffi.compile()
