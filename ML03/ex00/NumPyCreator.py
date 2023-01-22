import numpy as np
from typing import Iterable


class NumPyCreator:
    def __init__(self):
        pass

    def from_list(self, lst: list, dtype=None) -> np.ndarray:
        if not isinstance(lst, list):
            return None
        if not all(isinstance(x, list) for x in lst):
            return None
        if not all(len(x) == len(lst[0]) for x in lst):
            return None
        return np.array(lst, dtype=dtype)

    def from_tuple(self, tpl: tuple, dtype=None) -> np.ndarray:
        return np.array(tpl, dtype=dtype) if isinstance(tpl, tuple) else None

    def from_iterable(self, itr: Iterable, dtype=None) -> np.ndarray:
        return np.array(itr, dtype=dtype) if isinstance(itr, Iterable) else None

    def from_shape(self, shape: tuple, value=0, dtype=None) -> np.ndarray:
        return np.full(shape, value, dtype=dtype) if isinstance(shape, tuple) else None

    def random(self, shape: tuple, dtype=None) -> np.ndarray:
        return np.random.rand(*shape) if isinstance(shape, tuple) else None

    def identity(self, n: int, dtype=None) -> np.ndarray:
        return np.identity(n, dtype=dtype) if isinstance(n, int) else None
