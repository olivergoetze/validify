"""Setup for the validify package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Oliver Götze",
    author_email="oliver.goetze@mailbox.org",
    name='validify',
    license="MIT",
    description='validify is a rule-based validation module for assessing the structure of an xml tree, built on top of the lxml library. It currently covers '
                'a subset of the XML Schema 1.1 Definition.',
    version='v0.0.1',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/olivergoetze/validify',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['lxml', 'logzero'],
    tests_require=["pytest"],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
