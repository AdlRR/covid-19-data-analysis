# covid-19-data-analysis

The purpose of this program is to check the total COVID-19 cases and deaths per million in each country at the time a lockdown was first declared, and then plot the data in bar charts.

Total cases or deaths for a certain date are an indicator of how advanced the pandemic is on that date, and I take the relative figures (per million) to account for the size of each country. Therefore, the total cases and total deaths per million at the date of the lockdown give an idea of how early or how late was each country to declare a lockdown.

Both cases and deaths are in theory good indicators of the progress of the pandemic. In practice, cases are often underreported because of insuficient testing, and countries also vary widely in the amount of tests they perform. Deaths are often better reported, and so they are a better indicator.

Total cases (or deaths) on a given date are the cases from 2019-12-31 (earliest date in the OWID dataset) up to the date. New cases are the cases reported on a given date. In the most usual model for a pandemic, the exponential growth model, new cases and total cases are proportional up to a constant (i.e. one is obtained from the other by multiplying by a constant and then adding another constant), so both figures give the same information. However, in real-world data, new cases in a single day are more exposed to noise, while in total data the noise in different days tends to even out, so the total data are more robust. The same applies to deaths.

* The lockdown dates have been extracted from Wikipedia (https://en.wikipedia.org/wiki/COVID-19_pandemic_lockdowns) on 2020-06-03, with the help of [this tool](https://wikitable2csv.ggor.de/) by Gregor Weichbrodt.

* The rest of the data has been extrated from 'Our World In Data' (https://github.com/owid/covid-19-data/tree/master/public/data) on 2020-06-03. This data includes the new and total cases and death per million.

* I have crossed both datasets and kept only the country, the lockdown start date, and the new and total cases and deaths per million.

Be aware that:

* I have excluded countries with subnational lockdowns, because the OWID dataset doesn't include regional data. This excludes for example China and the USA.

* I have removed the countries for which there no data for the lockdown start date. They are El Salvador, Kosovo, Lybia and Samoa.
