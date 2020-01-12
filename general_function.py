import numpy as np
import pandas as pd

# get basic functions like shape, info, describe, null and outlier for every column
def general_function(df):
    print("row:{},columns:{}".format(str(df.shape[0]),str(df.shape[1])))
    print(df.info())
    print(df.describe(include='all'))
    print("Describe categorical df:")
    print(df.describe(include='object'))
    print('Null DF')
    null_df = pd.DataFrame(df.isnull().sum())
    null_df.columns = ['count']
    print('Null DF')
    print(null_df[null_df['count']>0])
    df_num = df.select_dtypes(exclude='object')
    df_num_col = df_num.columns
    for column in  df_num_col:
        print('column : '+column)
        print(iqr_outlier(df_num[column]))           

#function to get outlier values for given data/array
def iqr_outlier(arr):
    iqr75 = np.nanpercentile(arr, 75)
    iqr25 = np.nanpercentile(arr, 25)
    iqr = iqr75-iqr25
    upper_bound = iqr75 + (iqr*1.5)
    lower_bound = iqr25 - (iqr*1.5)
    return [i for i in arr if (upper_bound<i or lower_bound>i)]

#df = pd.read_csv('C:\\Users\\purni\\Downloads\\GLabs_DS\\GLabs_DSMP_New-master\\titanic.csv')
#basic_exploration(df)

#df = pd.read_csv('C:\\greyatom\\python\\mall_data.txt')
#basic_exploration(df)

if __name__ == "__main__":
    df = pd.read_csv('mall_data.txt')
    general_function(df)
    