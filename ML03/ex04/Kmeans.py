import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4, filepath='../resources/solar_system_census.csv'):
        '''
        Parameters:
            ncentroid: has to be an int, the number of centroids.
            max_iter: has to be an int, the number of iterations done before you stop the optimization.
        '''
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X: np.ndarray) -> None:
        '''
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.

        Parameters:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
            None.
        '''
        # Randomly initialize centroids
        self.centroids = X[np.random.choice(
            X.shape[0], self.ncentroid, replace=False), :]
        # Update centroids
        for _ in range(self.max_iter):
            # Assign each point to the closest centroid
            labels = self.predict(X)
            for j in range(self.ncentroid):
                # Update centroid to be the mean of all points assigned to it
                self.centroids[j] = np.mean(X[labels == j], axis=0)

    def predict(self, X: np.ndarray) -> np.ndarray:
        '''
        Predict from wich cluster each datapoint belongs to.

        Parameters:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.

        Return:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        '''
        # Calculate distance from each point to each centroid
        dist = np.sqrt(
            ((X[:, np.newaxis, :] - self.centroids) ** 2).sum(axis=2))
        # Return the index of the closest centroid for each point
        return np.argmin(dist, axis=1)


def check_datafile(filename: str) -> None:
    '''
    Check if filename exists and is a non empty .csv file.

    Parameters:
        filename (str): name of file to check

    Raises:
        FileNotFoundError: if file does not exist
        TypeError: if file is not a .csv file
        ValueError: if file is empty
    '''
    if not os.path.exists(filename):
        raise FileNotFoundError('File ' + filename + ' does not exist')
    if not filename.endswith('.csv'):
        raise TypeError('File ' + filename + ' is not a CSV file')
    if os.stat(filename).st_size == 0:
        raise ValueError('File ' + filename + ' is empty')


def check_dataset(df: pd.DataFrame) -> None:
    '''
    Check if dataset is four columns of numbers with no null values.

    Parameters:
        df (pd.DataFrame): dataset to check

    Raises:
        Exception: if dataset is not four columns of numbers with no null values
    '''
    if len(df.columns) != 4:
        raise Exception('Dataset must have four columns')
    if df.isnull().values.any():
        raise Exception('Dataset must not have null values')
    for col in df.columns:
        if not np.issubdtype(df[col].dtype, np.number):
            raise Exception(f'Column {col} is not numeric')


def check_args(args: list) -> None:
    '''
    Check if arguments are valid.

    Parameters:
        args (list): list of arguments

    Raises:
        Exception: if arguments are not valid
    '''
    if len(args) != 4:
        raise Exception
    for arg in args[1:]:
        if '=' not in arg:
            raise Exception
        key, value = arg.split('=')
        if key not in ['filepath', 'max_iter', 'ncentroid']:
            raise Exception
        if key == 'max_iter' or key == 'ncentroid':
            try:
                int(value)
            except ValueError:
                raise Exception


def main():
    '''
    A program that performs K-means clustering on a dataset.
    '''
    # Default parameters
    Parameters = {'filepath': '../resources/solar_system_census.csv',
                  'max_iter': 20, 'ncentroid': 4}

    # Parse arguments
    try:
        if (len(sys.argv) >1):
            check_args(sys.argv)
            for arg in sys.argv:
                if '=' in arg:
                    key, value = arg.split('=')
                    if key == 'filepath':
                        Parameters['filepath'] = value
                    elif key == 'max_iter':
                        Parameters['max_iter'] = int(value)
                    elif key == 'ncentroid':
                        Parameters['ncentroid'] = int(value)
        check_datafile(Parameters['filepath'])
        df = pd.read_csv(Parameters['filepath'])
        df = df.dropna()
        check_dataset(df)
    except Exception as e:
        print(e)
        print('Usage: python Kmeans.py filepath=<filepath> max_iter=<max_iter> ncentroid=<ncentroid>')
        sys.exit(1)

    # Run K-means
    km = KmeansClustering(
        max_iter=Parameters['max_iter'], ncentroid=Parameters['ncentroid'])
    km.fit(df[['height', 'weight', 'bone_density']].values)
    labels = km.predict(df[['height', 'weight', 'bone_density']].values)

    # Plot results
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['height'], df['weight'], df['bone_density'], c=labels)
    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    ax.set_zlabel('Density')
    plt.show()


if __name__ == "__main__":
    main()
