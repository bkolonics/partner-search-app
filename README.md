# Partner search app

This project contains several functions that perform data analysis on Excel files related to research grants.

## Installation

To use this project, clone or download it from the GitHub repository.
````bash
git clone https://github.com/bkolonics/partner-search-app.git
````

Install the required packages:
````bash
pip3 install -r requirements.txt
````
## Usage

To use the functions, run main.py in the terminal:

````bash
python3 mvp.py
````

## Functionning

* The function excel_to_dataframe converts an excel file to a Pandas dataframe. The function takes in a file path as a string and returns a dataframe.

* The function plot_dataframe plots a dataframe in a bar chart format. The function takes in a Pandas dataframe and plots it. * The chart represents the "EC Contribution per Project" with the x-axis showing the short name and y-axis showing the EC Contribution.

* The function annual_grants returns a dataframe with annual grants. The function takes in a Pandas dataframe and returns a new dataframe with the short name and EC contribution.

* The function statistic prints the statistics about a dataframe. The function takes in a Pandas dataframe and prints the mean, standard deviation, min, max, variance, and skewness of the input. Additionally, the function plots the histogram of the input dataframe.

* The function validate_country_acronym validates if a country acronym is in the list of countries. The function takes in a country acronym as a string and checks if it is a two-character string and if it exists in the list of countries.

* The function received_grants_per_partner_for_country returns a dataframe with the received grants per partner for a specific country. The function takes in a country acronym as a string and an optional save flag. The function loads data from an excel file and filters it by the specified country. The function then calculates the number of projects, the sum of EC contributions, and the count of coordinators for each participant. The function returns a dataframe with the short name, name, activity type, organization URL, count of projects, sum of EC contributions, and count of time the organization has been coordinator. If the save flag is True, the function saves the dataframe to an excel file in the "output" directory.

* The main function is called when the script is run. It calls the plot_dataframe function and the statistic function with data from the "assets" directory. It then prompts the user to enter a country acronym, validates it, and calls the received_grants_per_partner_for_country function with the validated country acronym and a save flag of True. The resulting dataframe is printed to the console and saved to an excel file.