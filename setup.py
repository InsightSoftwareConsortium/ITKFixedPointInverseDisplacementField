# -*- coding: utf-8 -*-
from __future__ import print_function
from os import sys

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

setup(
    name='itk-fixedpointinversedisplacementfield',
    version='1.0.0',
    author='Insight Software Consortium',
    author_email='itk+community@discourse.itk.org',
    packages=['itk'],
    package_dir={'itk': 'itk'},
    download_url=r'https://github.com/InsightSoftwareConsortium/ITKFixedPointInverseDisplacementField',
    description=r'Takes a displacement field as input and computes the displacement field that is its inverse.',
    long_description='itk-fixedpointinversedisplacementfield takes a '
                     'displacement field as input and computes the '
                     'displacement field that is its inverse with a simple '
                     'fixed-point approach.\n'
                     'Please refer to:\n'
                     'M. Luethi, "Inverting deformation fields using a fixed point iteration scheme.", '
                     'Insight Journal, July-December 2010, https://hdl.handle.net/10380/3222.',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: C++",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
    license='Apache',
    keywords='ITK InsightToolkit Spatial-Transforms',
    url=r'https://github.com/InsightSoftwareConsortium/ITKFixedPointInverseDisplacementField',
    install_requires=[
        r'itk>=5.2rc1'
    ]
    )
