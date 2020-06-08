# covid-19-data-analysis

The purpose of this program is to check the total COVID-19 cases and deaths per million in each country at the time a lockdown was first declared, and then plot the data in bar charts.

* The lockdown dates have been extracted [from Wikipedia](https://en.wikipedia.org/wiki/COVID-19_pandemic_lockdowns) on 2020-06-03, with the help of [this tool](https://wikitable2csv.ggor.de/) by Gregor Weichbrodt. The original data are in `/original_data/COVID-19 pandemic lockdowns.csv` and in `/lockdown_dates.csv`. In the latter, the first and some of the last lines have been removed for formatting reasons.

* The rest of the data has been extrated [from 'Our World In Data' (OWID)](https://github.com/owid/covid-19-data/tree/master/public/data) on 2020-06-03. This data includes the new and total cases and death per million. The original data are in `/original_data/owid-covid-data.csv` and in `/owid_data.csv`.

* Both datasets are crossed, and only the country, the lockdown start date, and the new and total cases and deaths per million are kept.

* The crossed data are recorded in `/lockdown_dates_with_data.csv`, and plotted in bar charts, which can be found in `/charts/`.

Be aware that:

* I have excluded countries with subnational lockdowns, because the OWID dataset doesn't include regional data. This excludes for example China and the USA.

* I have removed the countries for which there no data for the lockdown start date. They are El Salvador, Kosovo, Lybia and Samoa.
