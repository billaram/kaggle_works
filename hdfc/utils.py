def select_dtypes(df, types):
    df_num = df.select_dtypes(include=types)
    return list(df_num.columns)

def get_null_columns(df):

    null_counts = df.isna().sum()
    null_columns = null_counts[lambda x: x > 0] 

    return list(null_columns.index)

def get_null_columns(df):

    null_counts = df.isna().sum()
    null_columns = null_counts[lambda x: x > 0] 

    return list(null_columns.index)


def get_50_percent_null_cols(df):

    null_counts = df.isna().sum()
    null_columns = null_counts[lambda x: x > (df.shape[0] / 2)]
    
    columns = list(null_columns.index)
    
    return columns

def zero_varience_cols(df):
    zero_var_columns = df.nunique()[lambda x: x==1]
    columns = list(zero_var_columns.index)
    return columns