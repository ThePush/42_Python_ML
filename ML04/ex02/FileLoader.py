import pandas as pd
import os


class FileLoader:
    '''
    FileLoader class.

    Methods:
        load(path: str) -> pd.DataFrame
        display(df: pd.DataFrame, n: int) -> None
    '''

    def load(self, path: str) -> pd.DataFrame:
        '''
        Takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
        returns the dataset loaded as a pandas.DataFrame

        Parameters:
            path (str): path to the dataset to load

        Returns:
            pd.DataFrame: dataset loaded as a pandas.DataFrame
        '''
        try:
            if not isinstance(path, str) or not os.path.exists(path) or not path.endswith('.csv'):
                raise Exception
            df = pd.read_csv(path)
            print(
                f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
        except:
            print("Error: could not load dataset")
            return None
        return df

    def display(self, df: pd.DataFrame, n: int) -> None:
        '''
        Takes a pandas.DataFrame and an integer as arguments and displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.

        Parameters:
            df (pd.DataFrame): dataset to display
            n (int): number of rows to display

        Returns:
            None
        '''
        if not isinstance(df, pd.DataFrame):
            print("Error: " + str(type(df)) + " is not a pandas.DataFrame")
            return
        if not isinstance(n, int):
            print("Error: " + str(type(n)) + " is not an integer")
            return
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
