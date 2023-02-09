import pandas as pd


def proportion_by_sport(df: pd.DataFrame, year: int, sport: str, gender: str) -> float:
    '''
    A function displaying the proportion of participants
    who played a given sport, among the participants of a given genders.

    Parameters:
        df (pd.DataFrame): A pandas DataFrame containing the dataset.
        year (int): The year of the Olympic games.
        sport (str): The name of the sport.
        gender (str): The participant's gender

    Returns:
        a float corresponding to the proportion (percentage) of participants
        who played the given sport among the participants of the given gender.
    '''
    if not isinstance(df, pd.DataFrame) or not isinstance(year, int) or \
            not isinstance(gender, str) or not isinstance(sport, str):
        raise TypeError('Invalid argument type')
    nominator = df.loc[(df['Year'] == year) & (df['Sex']
                       == gender) & (df['Sport'] == sport)].drop_duplicates(subset=['ID']).shape[0]
    denominator = df.loc[(df['Year'] == year) & (df['Sex'] == gender)].drop_duplicates(subset=['ID']).shape[0]
    try:
        res = nominator / denominator
    except ZeroDivisionError:
        return 0
    return res
