# -*- coding: utf-8 -*-
#
# Requires:
#   Platform C language compiler   
#   Python packages: numpy
#
"""Setup up script for outputapi python extension."""

# Standard library imports
import os
import sys
import ast

HERE = os.path.abspath(os.path.dirname(__file__))
PY2 = sys.version_info.major == 2

def get_version(module='src'):
    """Get version."""
    with open(os.path.join(HERE, module, '__init__.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version

try:
    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext
except ImportError:
    from distutils.core import setup, Extension
    from distutils.command.build_ext import build_ext

class CustomBuildExtCommand(build_ext):
    """build_ext command for use when numpy headers are needed."""
    def run(self):
        # Import numpy here, only when headers are needed
        import numpy

        # Add numpy headers to include_dirs
        try:
            numpy_include = numpy.get_include()
        except AttributeError:
            numpy_include = numpy.get_numpy_include()

        self.include_dirs.append(numpy_include)
        
        # Call original build_ext command
        build_ext.run(self)    

setup(
    name = "outputapi", 
    cmdclass = {'build_ext': CustomBuildExtCommand}, 
    version = get_version(),
    ext_modules = [
        Extension("_outputapi", 
            sources = ['src/outputapi.i', 'src/outputapi.cpp', 'src/errormanager.cpp'],
            swig_opts=['-modern'],
            language='C++'
        )
    ],
    package_dir = {'':'src'},  
    py_modules = ['outputapi'],
      
    install_requires = [
        'numpy>=1.6.0'
    ],
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: C",
        "Development Status :: 4 - Beta",
    ])
