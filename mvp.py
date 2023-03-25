# pylint: disable=C0114
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def excel_to_dataframe(file: str, **kwargs: str) -> pd.DataFrame:
    """Converts excel file to dataframe"""
    return pd.read_excel(file, **kwargs)

def plot_dataframe(df_to_plot: pd.DataFrame) -> None:
    """Plots dataframe"""
    figure = df_to_plot.plot(kind='bar', x='shortName', y='ecContribution', fontsize=5, figsize=(10, 5),
                    title="EC Contribution per Project")
    figure.set_ylim(0, df_to_plot["ecContribution"].max())
    plt.show()


def annual_grants(df: pd.DataFrame) -> pd.DataFrame or None:
    """function that returns a dataframe with the annual grants"""
    try:
        df = df[["shortName", "ecContribution"]]
        return df
    
    except KeyError:
        print("Key not in dataframe")


def statistic(cost_col: pd.DataFrame ) -> None:
    """function that print statistics about dataframe"""
    print(cost_col.describe())
    print("var     ", np.var(cost_col))
    print("skew    ", cost_col.skew())
    _, bin_edges = np.histogram(cost_col, bins=18)
    _, ax = plt.subplots()
    ax.hist(cost_col, bin_edges, cumulative = False)
    ax.set_xlabel('cost_col')
    ax.set_ylabel('Frequency')
    plt.show()


if __name__ == '__main__':

    plot_dataframe(annual_grants(excel_to_dataframe('assets/participants.xlsx',
                                                     sheet_name='Sheet1')))
    print(statistic(excel_to_dataframe('assets/projects.xlsx',
                                       sheet_name='Sheet1')["totalCost"]))
    