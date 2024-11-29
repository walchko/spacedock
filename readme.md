![](docs/ship.jpg)

# Spacedock

**under development**

- `project`: string
- `year`: string
- `author`: string
- `git_repo`: url
- `python_versions`: list
- `python_modules`: list

## Tools

```
spacedock --yaml [cpp|python] --build [cpp|python] --help
```


## Layout

- `.gitignore`
- cpp
    - `CMakeLists.txt`
    - examples
        - `CMakeLists.txt`
        - `example.cpp`
    - gtests
        - `CMakeLists.txt`
        - `test.cpp`
    - `readme.md`
    - src
        - `file.cpp`
- data
- docs
- `LICENSE`
- notebooks
- pico
    - `CMakeLists.txt`
    - examples
        - `CMakeLists.txt`
        - `example.cpp`
    - `readme.md`
    - src
        - `file.cpp`
- python
    - module
        - `__init__.py`
        - `file.py`
    - `pyproject.toml`
    - `readme.md`
    - tests
        `test.py`
- `readme.md`

# MIT License

**Copyright (c) 2023 Kevin Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.