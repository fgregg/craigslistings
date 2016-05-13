#!/usr/bin/python
# -*- coding: utf-8 -*-

setup(
    name='listings',
    url='https://github.com/fgregg/listings_scraper',
    version='0.0.1',
    description='Craigslist rental housing listings scraper',
    packages=['listings'],
    install_requires=['psycopg2', 'raven'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Cython', 
        'Topic :: Software Development :: Libraries :: Python Modules']
    )

