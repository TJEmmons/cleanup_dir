import os
import pandas as pd
import glob


def delete_file(file):
    """
    Deletes the file at the given file path if it exists.

    Parameters:
    file (str): The file path of the file to delete.

    Returns:
    None
    """
    if os.path.exists(file):
        os.remove(file)


# create a list of all ".tmpzzz" and ".session" files in the home directory that end with an 8 character string of integers
files = pd.Series(
    glob.glob("~/*.tmpzzz") +
    glob.glob("~/*[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].session")
)

# delete the files using the apply() function and the delete_file() function
files.apply(delete_file)

print(
    "Deleted all '.tmpzzz' and '.session' files in the home directory that end with an 8 character string of integers")