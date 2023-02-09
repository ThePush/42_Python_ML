import numpy as np


class ColorFilter:
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None or len(array.shape) != 3:
            return None
        new_array = array.copy()
        new_array[:, :, 0] = 255 - new_array[:, :, 0]
        new_array[:, :, 1] = 255 - new_array[:, :, 1]
        new_array[:, :, 2] = 255 - new_array[:, :, 2]
        return new_array
    
    def to_blue(self, array):
        """
        Turns the image received as a numpy array into a blue filter.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None or len(array.shape) != 3:
            return None
        new_array = array.copy()
        new_array[:, :, 0] = 0
        new_array[:, :, 1] = 0
        return new_array
    
    def to_green(self, array):
        """
        Turns the image received as a numpy array into a green filter.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None or len(array.shape) != 3:
            return None
        new_array = array.copy()
        new_array[:, :, 0] = 0
        new_array[:, :, 2] = 0
        return new_array
    
    def to_red(self, array):
        """
        Turns the image received as a numpy array into a red filter.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if array is None or len(array.shape) != 3:
            return None
        new_array = array.copy()
        new_array[:, :, 1] = 0
        new_array[:, :, 2] = 0
        return new_array