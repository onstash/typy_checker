# Typy Checker

## Type-Checking Function Arguments for Humans™

Typy_checker is a library that checks the type of the arguments of a given function. It exposes a decorator that you can use to retain your sanity.

## How to install it?

* Python 3

    ```bash
    pip3 install typy_checker
    ```

* Python 2

    ```bash
    pip install typy_checker
    ```

## How to use it?

```py
from typy_checker import type_checker

valid_types = (int, float)
@type_checker(foo=valid_types, scooby=valid_types)
def add(foo, scooby):
    return foo + scooby
```

Calling `add(1, 2)` will give the intended result while calling `add([2], [3])` will throw an error.

## How to contribute?

You can contribute in many ways. Head over to the GitHub repo's issues page [here](https://github.com/onstash/typy_checker/issues), create an issue if it's there and let's discuss. This repo follows Kent Dodds' [all-contributors](https://github.com/kentcdodds/all-contributors) philosophy.