## my-minipack

An exercise of 42 AI's Python Bootcamp (ML02/ex05)


## Description
 The library contains the following functions:

- ft_progress: a progress bar

- logger: a decorator to log the execution time of a function in a file

## Usage

```python
from my_minipack.progressbar import ft_progress
from my_minipack.logger import logger
```

## Example

```python
from my_minipack.progressbar import ft_progress
from my_minipack.logger import log
from time import sleep


@log
def main():
    listy = range(100)

    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)


if __name__ == '__main__':
    main()
```