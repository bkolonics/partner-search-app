# pylint: disable=C0114
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def excel_to_dataframe(file: str, **kwargs: str) -> pd.DataFrame:
    """Converts excel file to dataframe"""
    return pd.read_excel(file, **kwargs)

def plot_dataframe(df_to_plot: pd.DataFrame, **kwargs: str) -> None:
    """Plots dataframe"""
    fig = df_to_plot.plot(kind='bar', **kwargs).get_figure()
    fig.savefig('EC Contribution per Project.pdf', bbox_inches='tight')

def statistic(cost_col: pd.DataFrame ) -> None:
    """function that print statistics about dataframe"""
    print(cost_col.describe())
    print("var     ", np.var(cost_col))
    print("skew    ", cost_col.skew())
    _, bin_edges = np.histogram(cost_col, bins=18)
    (_, ax) = plt.subplots()
    ax.hist(cost_col, bin_edges, cumulative = False)
    ax.set_xlabel('cost_col')
    ax.set_ylabel('Frequency')
    plt.show()
if __name__ == '__main__':

    print(excel_to_dataframe('assets/participants.xlsx', sheet_name='Sheet1'))
    plot_dataframe(excel_to_dataframe('assets/participants.xlsx', sheet_name='Sheet1'),x="name",
                    y="ecContribution" , figsize=(100, 30), fontsize=1,
                    title="EC Contribution per Project")
    print(type(excel_to_dataframe('assets/projects.xlsx', sheet_name='Sheet1')["totalcost_col"]))
    print(statistic(excel_to_dataframe('assets/projects.xlsx',
                                       sheet_name='Sheet1')["totalcost_col"]))
    