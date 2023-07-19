import pandas as pd

def get_type_column(column_name:str , df:pd.DataFrame, m=None, original_df=None) -> str:

    if df[column_name].dtype == 'O':
        #return 'text'
        return 'categorical'
    try:
        if m is not None and bool(m.get_all(name=column_name)):
            return m.get_all(name=column_name).type[0]
        elif m is not None and bool(m.get_all(name=column_name[:-2])) and original_df is not None:
            #lets check if this is a date:
            original_colname = column_name[:-2]
            atype = original_df[original_colname].dtype
            typ = str(atype)
            if re.search("^date.", typ):
                return 'categorical'
            if atype == 'O':
                row_sample = original_df[original_colname].iloc[0]
                if is_date(row_sample):
                    return 'categorical'

        #if isinstance(row_sample, float):
        #    return 'numerical'
        if df[column_name].dtype in ['float64', 'float32', 'float16']:
            # we have to check if column was wrong catalogued as numerical
            grouped = df[column_name].unique()
            if len(grouped) < 10:
                #check there are no decimals
                for v in grouped:
                    are_decimals = v - int(v)
                    if are_decimals > 0.0:
                        return 'numerical'
                return 'categorical'
            return 'numerical'

        elif df[column_name].dtype in ['int64', 'int32', 'int16', 'int8']:
            max = df[column_name].max()
            min = df[column_name].min()
            diff = max - min
            diff2 = int(max) - int(min)
            if diff == diff2:
                if diff < 10:
                    grouped = df[column_name].unique()
                    if len(grouped)< 10:
                        return 'categorical'
            return "numerical"
        else:
            return "categorical"
    except Exception as e:
        return 'categorical'


def get_type_data(df: pd.DataFrame) -> dict:
    cols = df.columns.to_list()

    num_cols = []
    cat_col = []
    text_col = []

    for col in df.columns:
        column_type = get_type_column(col, df)
        if column_type == "categorical" and col != "fecha":
            cat_col.append(col)
        elif column_type == "text":
            text_col.append(col)
        elif column_type == "numerical":
            num_cols.append(col)   

    return {
        #"text": text_col,
        "cat": cat_col,
        "num": num_cols
    } 
