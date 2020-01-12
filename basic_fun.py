import numpy as np
import pandas as pd

def basic_df_exploration(df):
    """
    Provides basic data exploration details
    Params:
    -------
    df: pandas dataframe
    Returns:
    --------
    None
    Prints the following output:
    - Shape
    - Column name and respective types
    - Descriptive stats
    - Columns with null values and respective count
    - Outliers per column if any
    """
    print('\n====================BASIC EXPLORATION====================\n')
    # Printing rows and columns
    print('Dataframe has {} rows and {} columns\n'.format(str(df.shape[0]), str(df.shape[1])))
    # Printing column name and its respective dtypes
    print('Column names and its respective types')
    print('-------------------------------------\n')
    print(df.info())
    print('')
    # Printing Descriptive stats for numeric columns
    print('Descriptive stats for numeric columns')
    print('-------------------------------------\n')
    print(df.describe())
    print('')
    # Printing Descriptive stats for categorical columns
    print('Descriptive stats for categorical columns')
    print('-----------------------------------------\n')
    print(df.describe(include='object'))
    print('')
    # Printing column with null values
    print('Columns with null values and respective counts\n')
    print('----------------------------------------------\n')
    print(df.isnull().sum()[df.isnull().sum() > 0])
    print('')
    # Printing outliers for columns
    print('Checking for outliers in numeric columns')
    print('----------------------------------------')
    for c in df.select_dtypes(exclude='object').columns:
        print('Outliers in column {}:'.format(c))
        outliers = iqr_outliers(df[c])
        if outliers:
            print(set(outliers))
            print('')
        else:
            print('No outliers\n')
    print('\n====================DONE====================\n')

def iqr_outliers(arr):
    iqr75 = np.nanpercentile(arr, 75)
    iqr25 = np.nanpercentile(arr, 25)
    iqr = iqr75-iqr25
    upper_bound = iqr75 + (iqr*1.5)
    lower_bound = iqr25 - (iqr*1.5)
    return [i for i in arr if (upper_bound<i or lower_bound>i)]


if __name__ == "__main__":
    df = pd.read_csv('mall_data.txt')
    basic_df_exploration(df)