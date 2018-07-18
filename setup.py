import sys

from pyjsg.parser_impl import __version__, __license__, __url__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ["antlr4-python3-runtime>=4.7", "jsonasobj>=1.2.0", "requests"]

if sys.version_info < (3, 7):
    requires.append("dataclasses")


setup(
    name='PyJSG',
    version=__version__,
    packages=['pyjsg.jsglib', 'pyjsg.parser', 'pyjsg.parser_impl'],
    url=__url__,
    license=__license__,
    author='Harold Solbrig',
    author_email='solbrig.harold@mayo.edu',
    description='"PyJSG - Python JSON Schema Grammar bindings',
    long_description='A tool to create Python classes that represent JSON objects defined in JSG',
    install_requires=requires,
    tests_require = ["yadict-compare>=1.1.2"],
    scripts=['scripts/generate_parser'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7']
)
