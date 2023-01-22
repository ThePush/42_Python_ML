#!/usr/bin/env bash

python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade build
python3 -m build
python3 setup.py sdist bdist_wheel
pip3 install ./dist/my_minipack-1.0.0.tar.gz
#pip3 install ./dist/my_minipack-1.0.0-py3-none-any.whl