from setuptools import setup, find_packages

# package information
NAME = "my-minipack"
DESCRIPTION = "Howto create a package in python."
AUTHOR = "jsemel"
AUTHOR_EMAIL = "jsemel@student.42.fr"
#URL = "https://github.com/yourusername/your_package_name"
VERSION = "1.0.0"
LICENCE = "GPLv3"

# package dependencies
#INSTALL_REQUIRES = [
#    "dependency1>=version",
#    "dependency2>=version",
#    # ...
#]

# package classifiers
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers :: Students",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Education :: HowTo :: Package",
]

# package keywords
#KEYWORDS = ["your", "package", "keywords"]

# package setup
setup(
    name='my_minipack',
    version='1.0.0',
    description='Howto create a package in python.',
    author='jsemel',
    author_email='jsemel@student.42.fr',
    license='GPLv3',
    #url=URL,
    packages=find_packages(),
    #install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    #keywords=KEYWORDS,
)
