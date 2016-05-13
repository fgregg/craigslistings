#!/usr/bin/python
# -*- coding: utf-8 -*-

setup(
    name='craigslistings',
    url='https://github.com/fgregg/craigslistings',
    version='0.0.1',
    description='Craigslist rental housing listings scraper',
    packages=['craigslistings'],
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

