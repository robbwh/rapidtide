#!/bin/env python
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

addtidepool = True

modules_list= ['tide_funcs']
if addtidepool:
    modules_list.append('tidepoolTemplate')
    modules_list.append('OrthoImageItem')

script_list = ['scripts/rapidtide2',
               'scripts/rapidtide2std',
               'scripts/showxcorr',
               'scripts/resamp1tc',
               'scripts/resamplenifti',
               'scripts/simdata',
               'scripts/pixelcomp',
               'scripts/showtc',
               'scripts/showhist']
if addtidepool:
    script_list.append('scripts/tidepool')

setup(
    name='rapidtide',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.2',

    description='Tools for performing correlation analysis on fMRI data.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/bbfrederick/rapidtide',

    # Author details
    author="Blaise Frederick",
    author_email="bbfrederick@mclean.harvard.edu",

    # Choose your license
    license='Apache Software License',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords=['fMRI', 
        'correlation',
        'RIPTiDe',
        'noise'],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],
    #py_modules=['tide_funcs'],
    #
    #if addtidepool:
    #    py_modules.append('tidepoolTemplate.py')
    #    py_modules.append('OrthoImageItem.py')
    py_modules=modules_list,

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy', 'scipy', 'sklearn', 'nibabel', 'matplotlib'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'jit': ['numba'],
        'gui': ['pyqtgraph'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    include_package_data = True,
    zip_safe=False,
    #packages = find_packages(['reference', 'examples']),
    #package_dir = {'': 'rapidtide'},
    package_data={
        'example':  ['examples/src/fmri.nii.gz',
                     'examples/src/timecourse1.txt',
                     'examples/src/timecourse2.txt',
                     'examples/src/nirs.txt'],
        'reference': ['reference/*.nii.gz'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    scripts=script_list,
)
