import sys

from pyjsg.parser_impl import __version__, __license__, __url__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# typing library was introduced as a core module in version 3.5.0
requires = ["antlr4-python3-runtime>=4.7", "jsonasobj>=1.1.2", "requests"]
test_requires = ["yadict-compare>=1.1.2"]
if sys.version_info < (3, 5):
    requires.append("typing")

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
    extras_require={
        'testing' : test_requires
    },
    scripts=['scripts/generate_parser'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only']
)
