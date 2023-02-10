import pandas as pd


def how_many_medals(df: pd.DataFrame, name: str) -> dict:
    '''
    A function that will return a dictionary of dictio-
    naries giving the number and type of medals for each year during which the participant
    won medals.

    Parameters:
        df (pd.DataFrame): The data frame containing the data.
        name (str): The name of the athlete.

    Returns:
        dict: A dictionary of dictionaries giving the number and type of medals for each year during which the participant won medals.
    '''
    # Filter the data frame to only include the athlete's name.
    df = df[df['Name'] == name]
    # Filter the data frame to only include the athlete's name and the year and the medal.
    df = df[['Year', 'Medal']]
    # Group the data frame by the year and the medal.
    df = df.groupby(['Year', 'Medal']).size()
    # Rename the medals.
    df = df.rename({'Gold': 'G', 'Silver': 'S', 'Bronze': 'B'})
    # Convert the data frame to a dictionary.
    df = df.to_dict()
    # Create a dictionary to store the results.
    result = {}
    # Loop through the dictionary.
    for key, value in df.items():
        # If the year is not in the results dictionary, add it.
        if key[0] not in result:
            result[key[0]] = {'G': 0, 'S': 0, 'B': 0}
        # Add the medal type and the number of medals.
        result[key[0]][key[1]] = value
    # Return the results.
    return result

# https://realpython.com/pandas-groupby/
