# Python

## Build and Publish

```bash
pip install -U build twine pip setuptools
python -m build

# test all is good
twine check dist/*
twine upload --repository testpypi dist/*

# upload
twine upload dist/*   
```

## Install

```bash
pip install squaternion   # pull from pypi
pip install -e .          # development
```
