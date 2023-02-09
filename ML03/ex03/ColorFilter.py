import numpy as np


class ColorFilter:
    def invert(self, array):
        '''
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
        '''
        if not isinstance(array, np.ndarray) or len(array.shape) != 3:
            return None
        new_array = array.copy()
        new_array[:, :, 0] = 255 - new_array[:, :, 0]
        new_array[:, :, 1] = 255 - new_array[:, :, 1]
        new_array[:, :, 2] = 255 - new_array[:, :, 2]
        return new_array

    def to_blue(self, array):
        '''
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
        '''
        if not isinstance(array, np.ndarray) or len(array.shape) != 3:
            return None
        new_array = array.copy()
        new_array[:, :, 0] = 0
        new_array[:, :, 1] = 0
        return new_array

    def to_green(self, array):
        '''
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
        '''
        if not isinstance(array, np.ndarray) or len(array.shape) != 3:
            return None
        new_array = array.copy()
        new_array[:, :, 0] = 0
        new_array[:, :, 2] = 0
        return new_array

    def to_red(self, array):
        '''
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
        '''
        if not isinstance(array, np.ndarray) or len(array.shape) != 3:
            return None
        new_array = array.copy()
        new_array[:, :, 1] = 0
        new_array[:, :, 2] = 0
        return new_array

    def to_celluloid(self, array):
        '''
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
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
        '''
        if not isinstance(array, np.ndarray) or len(array.shape) != 3:
            return None
        new_array = array.copy()
        for i in range(3):
            new_array[new_array[:, :, i] < 64, i] = 32
            new_array[(new_array[:, :, i] >= 64) & (
                new_array[:, :, i] < 128), i] = 96
            new_array[(new_array[:, :, i] >= 128) & (
                new_array[:, :, i] < 192), i] = 160
            new_array[new_array[:, :, i] >= 192, i] = 224
        return new_array

    def to_grayscale(self, array, filter, **kwargs):
        '''
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        '''
        if not isinstance(array, np.ndarray) or len(array.shape) != 3:
            return None
        if filter not in ['m', 'mean', 'w', 'weight']:
            return None
        new_array = array.copy()
        if filter in ('mean', 'm'):
            for row in new_array:
                for pixel in row:
                    pixel[0] = pixel[1] = pixel[2] = pixel.sum() / len(pixel)
        elif filter in ('weight', 'w'):
            if 'weights' not in kwargs:
                return None
            weights = kwargs['weights']
            if not isinstance(weights, list) or len(weights) != 3:
                return None
            for row in new_array:
                for pixel in row:
                    pixel[0] = pixel[1] = pixel[2] = (
                        pixel[:-1] * weights).sum()
        return new_array
