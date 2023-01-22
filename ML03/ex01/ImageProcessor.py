import numpy as np
from PIL import Image
import os


class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path: str) -> np.ndarray:
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f'No such file or directory')
            if os.stat(path).st_size == 0:
                raise OSError(f'None')
            img = Image.open(path)
            print(f'Loading image of dimensions {img.width} x {img.height}')
            return np.array(img)
        except Exception as e:
            print(f'Exception: {type(e).__name__} -- strerror: {e}')
            return None

    def display(self, array: np.ndarray) -> None:
        try:
            Image.fromarray(array).show()
        except Exception as e:
            print(e)
