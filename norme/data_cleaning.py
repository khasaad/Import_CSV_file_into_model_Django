import pandas as pd


# Split file data.csv to several columns according to the symbol '|'
def split_data(file_csv: str, cond: str):
    dataframe = pd.read_csv(file_csv)
    dataframe[list(dataframe.columns)[0].split(cond)] = dataframe[list(dataframe.columns)[0]].str.split(cond, expand=True)
    dataframe.drop(columns=dataframe.columns[0], axis=1, inplace=True)
    return dataframe

if __name__ == '__main__':
    df = split_data('data.csv', '|')
    df.to_csv('new_data.csv', encoding='utf-8', index=False)
