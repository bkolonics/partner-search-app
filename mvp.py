# pylint: disable=C0114
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def excel_to_dataframe(file: str, **kwargs: str) -> pd.DataFrame:
    """Converts excel file to dataframe"""
    return pd.read_excel(file, **kwargs)

def plot_dataframe(df: pd.DataFrame, **kwargs: str) -> None:
    """Plots dataframe"""
    fig = df.plot(kind='bar', **kwargs).get_figure()
    fig.savefig('EC Contribution per Project.pdf', bbox_inches='tight')

def statistic(Cost: pd.DataFrame ) -> None:
    """function that print statistics about dataframe"""
    print(Cost.describe())
    print("var     ", np.var(Cost))
    print("skew    ", Cost.skew())
    _, bin_edges = np.histogram(Cost, bins=18)
    (_, ax) = plt.subplots()
    ax.hist(Cost, bin_edges, cumulative = False)
    ax.set_xlabel('Cost')
    ax.set_ylabel('Frequency')
    plt.show()
if __name__ == '__main__':

    print(excel_to_dataframe('assets/participants.xlsx', sheet_name='Sheet1'))
    plot_dataframe(excel_to_dataframe('assets/participants.xlsx', sheet_name='Sheet1'),x="name", y="ecContribution" , figsize=(100, 30), fontsize=1, title="EC Contribution per Project")
    print(type(excel_to_dataframe('assets/projects.xlsx', sheet_name='Sheet1')["totalCost"]))
    print(statistic(excel_to_dataframe('assets/projects.xlsx', sheet_name='Sheet1')["totalCost"]))
    