import pandas as pd


def youngest_fellah(df: pd.DataFrame, n: int) -> dict:
    '''
    Returns a dictionary with the minimum age of the participants of the Olympics held in a given year.

    Parameters:
        df (pd.DataFrame): dataset to analyze
        n (int): year to analyze

    Returns:
        dict: dictionary with the minimum age of the participants of the Olympics held in a given year
    '''
    if not isinstance(df, pd.DataFrame) or not isinstance(n, int) or n < 0:
        raise ValueError("Error: invalid argument type")
    youngest_woman = df.loc[(df['Sex'] == 'F') &
                            (df['Year'] == n), 'Age'].min()
    youngest_man = df.loc[(df['Sex'] == 'M') & (df['Year'] == n), 'Age'].min()
    return {'f': youngest_woman,
            'm': youngest_man}
