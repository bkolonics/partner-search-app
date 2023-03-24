import pandas as pd

def excel_to_dataframe(file: str, **kwargs: str) -> pd.DataFrame:
    """Converts excel file to dataframe"""
    return pd.read_excel(file, **kwargs)

def plot_dataframe(df: pd.DataFrame, **kwargs: str) -> None:
    """Plots dataframe"""
    fig = df.plot(kind='bar', **kwargs).get_figure()
    fig.savefig('EC Contribution per Project.pdf', bbox_inches='tight')



if __name__ == '__main__':

    print(excel_to_dataframe('assets/participants.xlsx', sheet_name='Sheet1'))
    plot_dataframe(excel_to_dataframe('assets/participants.xlsx', sheet_name='Sheet1'),x="name", y="ecContribution" , figsize=(100, 30), fontsize=1, title="EC Contribution per Project")