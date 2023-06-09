# pylint: disable=C0114
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def excel_to_dataframe(file: str, **kwargs: str) -> pd.DataFrame:
    """Converts excel file to dataframe"""
    return pd.read_excel(file, **kwargs)

def plot_dataframe(df_to_plot: pd.DataFrame) -> None:
    """Plots dataframe"""
    figure = df_to_plot.plot(kind='bar', x='year', y='totalCost', fontsize=5,
                              figsize=(10, 5),
                              title="Total cost of projects per year")
    figure.set_ylim(0, df_to_plot["totalCost"].max())
    plt.show()


def annual_grants(df_of_project_file: pd.DataFrame) -> pd.DataFrame or None:
    """function that returns a dataframe with the annual grants"""
    try:
        # sum all the grants per year
        df_of_project_file = df_of_project_file.groupby('year')['totalCost'].sum().reset_index(
            name='totalCost')
        print(df_of_project_file)
        return df_of_project_file

    except KeyError:
        print("Key not in dataframe")
        return None


def statistic(cost_col: pd.DataFrame ) -> None:
    """function that print statistics about dataframe"""
    print(cost_col.describe().reset_index().to_string(index=False))
    print("var ", np.var(cost_col))
    print("skew ", cost_col.skew())
    _, bin_edges = np.histogram(cost_col, bins=18)
    _, ax = plt.subplots() # pylint: disable=C0103
    ax.hist(cost_col, bin_edges, cumulative = False)
    ax.set_xlabel('cost_col')
    ax.set_ylabel('Frequency')
    plt.show()

def validate_country_acronym(aconym: str) -> str:
    """function valideates country acronym"""
    if len(aconym) != 2:
        raise ValueError("Country acronym must be 2 characters long")

    if aconym not in excel_to_dataframe('assets/countries.xlsx',
                                        sheet_name='Countries')["Acronym"].values:
        raise ValueError("Country acronym not in list of countries")

    return aconym

def received_grants_per_partner_for_country(country: str, save: bool = False) -> pd.DataFrame:
    """
    function that returns a dataframe with the received grants per partner for a country and
    saves it to a excel file if save is True
    """
    df_of_participants = excel_to_dataframe('assets/participants.xlsx',
                                            sheet_name='Sheet1')


    df_of_participants = df_of_participants[df_of_participants["country"] == country]
    df_of_participants = df_of_participants[
        ['shortName', 'name', 'activityType', 'organizationURL', 'ecContribution', 'role']]
    count_project = df_of_participants.groupby('shortName').size().reset_index(name='count_project')
    sum_ecContribution = df_of_participants.groupby(    # pylint: disable=C0103
        'shortName')['ecContribution'].sum().reset_index(name='sum_ecContribution')
    df_of_participants['count_coordinator'] = df_of_participants[
        'role'].apply(lambda x: x.count('coordinator'))
    sum_coordinator = df_of_participants.groupby(
        'shortName')['count_coordinator'].sum().reset_index(name='count_coordinator')
    df_of_participants = df_of_participants[
        ['shortName', 'name', 'activityType', 'organizationURL', 'ecContribution', 'role']]
    df_of_participants = df_of_participants.drop(columns=['ecContribution', 'role'])
    df_of_participants = pd.merge(df_of_participants, count_project, on='shortName')
    df_of_participants = pd.merge(df_of_participants, sum_ecContribution, on='shortName')
    df_of_participants = pd.merge(df_of_participants, sum_coordinator, on='shortName')
    df_of_participants = df_of_participants.drop_duplicates(subset='name', keep="first")
    df_of_participants = df_of_participants.sort_values(by=['sum_ecContribution'], ascending=False)


    if save:
        if not os.path.exists('output'):
            os.makedirs('output')
        df_of_participants.to_excel(
            f"output/received_grants_per_partner_for_country_{country}.xlsx")

    return df_of_participants



if __name__ == '__main__':

    plot_dataframe(annual_grants(excel_to_dataframe('assets/projects.xlsx',
                                                     sheet_name='Sheet1')))
    statistic(excel_to_dataframe('assets/projects.xlsx',
                                       sheet_name='Sheet1')["totalCost"])

    selected_country = validate_country_acronym(input("Enter country acronym: "))
    print(received_grants_per_partner_for_country(selected_country , save=True))
