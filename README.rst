============================
cookiecutter-21cmfast-plugin
============================

Cookiecutter_ template for a 21cmFAST/MC plugin. 

.. contents:: Table of Contents

Features
--------

This is an opinionated template that helps code have a consistent style and easy deployment.

* Pytest_ for testing
* Github Actions for CI
* Coveralls_ for code coverage
* Documentation with Sphinx_, ready for ReadTheDocs_.
* Support for C extensions (including coverage measurement for the C code). See c_extension_support_.
* Packaging and code quality checks. 

Requirements
------------

Just do::

  pip install cookiecutter

Usage and options
-----------------

First generate your project::

  cookiecutter gh:21cmfast/cookiecutter-21cmfast-plugin
  

You will be asked for these fields:

.. note:: Fields that work together usually use the same prefix. If you answer "no" on the first one then the rest
   won't have any effect so just ignore them. Maybe in the future cookiecutter will allow option hiding or something
   like a wizard.

.. list-table::
    :header-rows: 1

    * - Field
      - Default
      - Description

    * - ``full_name``
      - .. code:: python

            "Ionel Cristian Maries"
      - Main author of this library or application (used in ``AUTHORS.rst`` and ``setup.py``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``email``
      - .. code:: python

            "contact@ionelmc.ro"
      - Contact email of the author (used in ``AUTHORS.rst`` and ``setup.py``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``website``
      - .. code:: python

            "https://blog.ionelmc.ro"
      - Website of the author (used in ``AUTHORS.rst``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``repo_username``
      - .. code:: python

            "ionelmc"
      - GitHub user name of this project (used for GitHub link).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``project_name``
      - .. code:: python

            "Nameless"
      - Verbose project name, used in headings (docs, readme, etc).

    * - ``repo_hosting_domain``
      - .. code:: python

            "github.com"
      - Use ``"no"`` for no hosting (various links will disappear). You can also use ``"gitlab.com"`` and such but various
        things will be broken (like Travis configuration).

    * - ``repo_name``
      - .. code:: python

            "python-nameless"
      - Repository name on GitHub (and project's root directory name).

    * - ``package_name``
      - .. code:: python

            "nameless"
      - Python package name (whatever you would import).

    * - ``distribution_name``
      - .. code:: python

            "nameless"
      - PyPI distribution name (what you would ``pip install``).

    * - ``project_short_description``
      - .. code:: python

            "An example package [...]"
      - One line description of the project (used in ``README.rst`` and ``setup.py``).

    * - ``release_date``
      - .. code:: python

            "today"
      - Release date of the project (ISO 8601 format) default to today (used in ``CHANGELOG.rst``).

    * - ``year``
      - .. code:: python

            "now"
      - Copyright year (used in Sphinx ``conf.py``).

    * - ``version``
      - .. code:: python

            "0.1.0"
      - Release version (see ``.bumpversion.cfg`` and in Sphinx ``conf.py``).

    * - ``legacy_python``
      - .. code:: python

            "no"
      - Allow for legacy python versions, like ``python2.7``. If you do not especially need to support (depreciated) python
        versions you should keep it as is.

    * - ``c_extension_support``
      - .. code:: python

            "no"
      - .. _c_extension_support:

        Support C extensions (will slighly change the outputted ``setup.py``). Available options:

        * ``"yes"`` - to generate a Python C extension
        * ``"cffi"`` - to generate CFFI bindings against a C library
        * ``"cython"`` - to generate a Cython extension


    * - ``c_extension_optional``
      - .. code:: python

            "no"
      - Make C extensions optional (will allow your package to install even if extensions can't be compiled)
    * - ``c_extension_test_pypi``
      - .. code:: python

            "no"
      - Enables wheel publishing to https://test.pypi.org/ by using `tox-wheel <https://pypi.org/project/tox-wheel/>`_
        and `manylinux1 <https://hub.docker.com/r/ionelmc/manylinux>`_.

        You should only use this with ``c_extension_support``. If your project produces universal wheels this won't work
        well.
    * - ``test_matrix_configurator``
      - .. code:: python

            "no"
      - Enable the test matrix generator script. If you don't have a huge number of test environments then probably you
        don't need this.

    * - ``test_matrix_separate_coverage``
      - .. code:: python

            "no"
      - Enable this to have a separate env for measuring coverage. Indicated if you want to run doctests or collect tests
        from ``src`` with pytest.

        Note that ``test_matrix_separate_coverage == 'no'`` only works if you also have ``test_matrix_configurator == 'no'``.

    * - ``test_runner``
      - .. code:: python

            "pytest"
      - Test runner to use. Available options: ``pytest`` or ``nose``.

    * - ``setup_py_uses_test_runner``
      - .. code:: python

            "no"
      - Whether to use the test_runner for python setup.py test.
        Note that this will also add to ``setup_requires`` if a test-runner is needed.
    * - ``setup_py_uses_setuptools_scm``
      - .. code:: python

            "no"
      - Enables the use of `setuptools-scm <https://pypi.org/project/setuptools-scm/>`_. You can continue using
        bumpversion_ with this enabled.

        Recommended if you use ``c_extension_test_pypi == 'yes'`` as it will publish unique wheels for each commit.
    * - ``allow_tests_inside_package``
      - .. code:: python

            "no"
      - Collect tests that are inside the package (in other works, tests that are installed with the package).

        The outside of package `tests` directory will still exist and be collected.
    * - ``linter``
      - .. code:: python

        "flake8"
      - Linter to use for ``tox -e check``. Available options: ``flake8`` or ``pylama``
    * - ``pre_commit``
      - .. code:: python

        "no"
      - Enable basic `pre-commit <https://pre-commit.com/>`_ configuration.
    * - ``command_line_interface``
      - .. code:: python

            "plain"
      - Option to enable a CLI (a bin/executable file). Available options:

        * ``plain`` - a very simple command.
        * ``argparse`` - a command implemented with ``argparse``.
        * ``click`` - a command implemented with `click <http://click.pocoo.org/>`_ - which you can use to build more complex commands.
        * ``no`` - no CLI at all.

    * - ``command_line_interface_bin_name``
      - .. code:: python

            "nameless"
      - Name of the CLI bin/executable file (set the console script name in ``setup.py``).

    * - ``license``
      - .. code:: python

            "BSD license"
      - License to use. Available options:

        * BSD license
        * MIT license
        * ISC license
        * Apache Software License 2.0

        What license to pick? https://choosealicense.com/

    * - ``coveralls``
      - .. code:: python

            "no"
      - Enable pushing coverage data to Coveralls_ and add badge in ``README.rst``.

    * - ``codecov``
      - .. code:: python

            "yes"
      - Enable pushing coverage data to Codecov_ and add badge in ``README.rst``.

        **Note:** Doesn't support pushing C extension coverage yet.

    * - ``scrutinizer``
      - .. code:: python

            "no"
      - Add a Scrutinizer_ badge in ``README.rst``.

    * - ``codacy``
      - .. code:: python

            "no"
      - Add a Codacy_ badge in ``README.rst``.

        **Note:** After importing the project in Codacy, find the hexadecimal project ID from settings and replace it in badge URL

    * - ``codeclimate``
      - .. code:: python

            "no"
      - Add a CodeClimate_ badge in ``README.rst``.

    * - ``sphinx_docs``
      - .. code:: python

            "yes"
      - Have Sphinx documentation.

    * - ``sphinx_theme``
      - .. code:: python

            "sphinx-rtd-theme"
      - What Sphinx_ theme to use.

        Suggested alternative: `sphinx-py3doc-enhanced-theme
        <https://pypi.org/project/sphinx_py3doc_enhanced_theme>` for a responsive theme based on
        the Python 3 documentation.

    * - ``sphinx_doctest``
      - .. code:: python

            "no"
      - Set to ``"yes"`` if you want to enable doctesting in the `docs` environment. Works best with
        ``test_matrix_separate_coverage == 'no'``.

        Read more about `doctest support in Sphinx <http://www.sphinx-doc.org/en/stable/ext/doctest.html>`_.

    * - ``sphinx_docs_hosting``
      - .. code:: python

            "repo_name.readthedocs.io"
      - Leave as default if your documentation will be hosted on readthedocs.
        If your documentation will be hosted elsewhere (such as GitHub Pages or GitLab Pages),
        enter the top-level URL.

    * - ``pypi_badge``
      - .. code:: python

            "yes"
      - By default, this will insert links to your project's page on PyPI.org.
        Note that if your package is not (yet) on PyPI, this will cause tox -e docs to fail.
        If you choose "no", then these links will not be created.

    * - ``pypi_disable_upload``
      - .. code:: python

            "no"
      - If you specifically want to be sure your package will never be
        accidentally uploaded to PyPI, you can pick "yes".

    * - ``travis``
      - .. code:: python

            "yes"
      - If you want the Travis-CI_ badge and configuration.
    * - ``travis_osx``
      - .. code:: python

            "no"
      - Enables OSX support in the Travis-CI_ configuration. To keep things simple and easy to understand only Brew
        Python 2 and 3 will be used.

        You probably want to enable this if you use ``c_extension_test_pypi == 'yes'``.
    * - ``appveyor``
      - .. code:: python

            "yes"
      - If you want the AppVeyor_ badge and configuration.

    * - ``requiresio``
      - .. code:: python

            "yes"
      - If you want the `requires.io`_ badge and configuration.

The testing (``tox.ini`` and ``.travis.yml``) configuration is generated from templates. For your convenience there's an
initial bootstrap ``tox.ini``, to get the initial generation going just run::

  tox

You can later regenerate ``tox.ini`` and ``.travis.yml`` by running (if you enabled the ``test_matrix_configurator``
option)::

  tox -e bootstrap

After this you can create the initial repository (make sure you `create <https://github.com/new>`_ an *empty* Github
project)::

  git init .
  git add .
  git commit -m "Initial skel."
  git remote add origin git@github.com:ionelmc/python-nameless.git
  git push -u origin master

Then:

* `Enable the repository in your Travis CI account <https://travis-ci.com/account/migrate>`_.
* `Enable the repository in your Coveralls account <https://coveralls.io/repos/new>`_.
* `Add the repo to your ReadTheDocs account <https://readthedocs.org/dashboard/import/>`_ + turn on the ReadTheDocs
  service hook. Don't forget to enable virtualenv and specify ``docs/requirements.txt`` as the requirements file in
  `Advanced Settings`.

Developing the project
``````````````````````

To run all the tests, just run::

  tox

To see all the tox environments::

  tox -l

To only build the docs::

  tox -e docs

To build and verify that the built package is proper and other code QA checks::

  tox -e check

Releasing the project
`````````````````````
Before releasing your package on PyPI you should have all the tox environments passing.

Version management
''''''''''''''''''

This template provides a basic bumpversion_ configuration. It's as simple as running:

* ``bumpversion patch`` to increase version from `1.0.0` to `1.0.1`.
* ``bumpversion minor`` to increase version from `1.0.0` to `1.1.0`.
* ``bumpversion major`` to increase version from `1.0.0` to `2.0.0`.

You should read `Semantic Versioning 2.0.0 <http://semver.org/>`_ before bumping versions.

Building and uploading
''''''''''''''''''''''

Before building dists make sure you got a clean build area::

    rm -rf build
    rm -rf src/*.egg-info

Note:

    Dirty ``build`` or ``egg-info`` dirs can cause problems: missing or stale files in the resulting dist or
    strange and confusing errors. Avoid having them around.

Then you should check that you got no packaging issues::

    tox -e check

And then you can build the ``sdist``, and if possible, the ``bdist_wheel`` too::

    python setup.py clean --all sdist bdist_wheel

To make a release of the project on PyPI, assuming you got some distributions in ``dist/``, the most simple usage is::

    twine upload --skip-existing dist/*.whl dist/*.gz dist/*.zip

In ZSH you can use this to upload everything in ``dist/`` that ain't a linux-specific wheel (you may need ``setopt extended_glob``)::

    twine upload --skip-existing dist/*.(whl|gz|zip)~dist/*linux*.whl

For making and uploading `manylinux1 <https://github.com/pypa/manylinux>`_ wheels you can use this contraption::

    docker run --rm -itv $(pwd):/code quay.io/pypa/manylinux1_x86_64 bash -c 'set -eux; cd code; rm -rf wheelhouse; for variant in /opt/python/*; do rm -rf dist build *.egg-info && $variant/bin/python setup.py clean --all bdist_wheel; auditwheel repair dist/*.whl; done; rm -rf dist build *.egg-info'
    twine upload --skip-existing wheelhouse/*.whl
    docker run --rm -itv $(pwd):/code quay.io/pypa/manylinux1_i686 bash -c 'set -eux; cd code; rm -rf wheelhouse; for variant in /opt/python/*; do rm -rf dist build *.egg-info && $variant/bin/python setup.py clean --all bdist_wheel; auditwheel repair dist/*.whl; done; rm -rf dist build *.egg-info'
    twine upload --skip-existing wheelhouse/*.whl

Note:

    `twine <https://pypi.org/project/twine>`_ is a tool that you can use to securely upload your releases to PyPI.
    You can still use the old ``python setup.py register sdist bdist_wheel upload`` but it's not very secure - your PyPI
    password will be sent over plaintext.

Changelog
---------

See `CHANGELOG.rst <https://github.com/ionelmc/cookiecutter-pylibrary/blob/master/CHANGELOG.rst>`_.

Questions & answers
-------------------

There's no Makefile?

  Sorry, no ``Makefile`` yet. The Tox_ environments stand for whatever you'd have in a ``Makefile``.

Why does ``tox.ini`` have a ``passenv = *``?

  Tox 2.0 changes the way it runs subprocesses - it no longer passes all the environment variables by default. This causes
  all sorts of problems if you want to run/use any of these with Tox: SSH Agents, Browsers (for Selenium), Appengine SDK,
  VC Compiler and so on.

  `cookiecutter-pylibrary` errs on the side of convenience here. You can always remove ``passenv = *`` if you like
  the strictness.

Why is the version stored in several files (``pkg/__init__.py``, ``setup.py``, ``docs/conf.py``)?

  We cannot use a metadata/version file [#]_ because this template is to be used with both distributions of packages (dirs
  with ``__init__.py``) and modules (simple ``.py`` files that go straigh in ``site-packages``). There's no good place
  for that extra file if you're distributing modules.

  But this isn't so bad - bumpversion_ manages the version string quite
  neatly.

.. [#] Example, an ``__about__.py`` file.

Not Exactly What You Want?
--------------------------

No way, this is the best. :stuck_out_tongue_winking_eye:


If you have criticism or suggestions please open up an Issue or Pull Request.

.. _Travis-CI: http://travis-ci.com/
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _Coveralls: https://coveralls.io/
.. _ReadTheDocs: https://readthedocs.org/
.. _Setuptools: https://pypi.org/project/setuptools
.. _Pytest: http://pytest.org/
.. _AppVeyor: http://www.appveyor.com/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Nose: http://nose.readthedocs.org/
.. _isort: https://pypi.org/project/isort
.. _bumpversion: https://pypi.org/project/bump2version
.. _bump2version: https://github.com/c4urself/bump2version
.. _Codecov: http://codecov.io/
.. _Scrutinizer: https://scrutinizer-ci.com/
.. _Codacy: https://codacy.com/
.. _CodeClimate: https://codeclimate.com/
.. _`requires.io`: https://requires.io/
