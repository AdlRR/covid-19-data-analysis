#The lockdown data has been extracted from https://en.wikipedia.org/wiki/COVID-19_pandemic_lockdowns with the help of Gregor Weichbrot's tool (https://wikitable2csv.ggor.de/).
#Retrieved on 2020-06-03.
#Extract the lockdown dates from the csv file into a list of lists:
lockdown_dates = []
with open('lockdown_dates.csv', 'r', encoding = 'ANSI') as infile:
	for line in infile:
		row = []
		line = line[:-1] #remove the \n character at the end of the line
		row = line.split(',')
		lockdown_dates.append(row)

#The rest of the data has been extrated from 'Our World In Data' (https://github.com/owid/covid-19-data/tree/master/public/data).
#Retrieved on 2020-06-03.
#Extract the 'Our World In Data' COVID-19 data from the csv file into a list of lists:
owid_data = []
with open('owid_data.csv', 'r', encoding = 'ANSI') as infile:
	for line in infile:
		row = []
		line = line[:-1] #remove the \n character at the end of the line
		row = line.split(',')
		owid_data.append(row)

#Cross both datasets into a list of dictionaries. We keep:
# * 'country' and 'lockdown_start_date' from lockdown dates,
# * 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million' and 'new_deaths_per_million' from the OWID data.
lockdown_dates_with_data = []
for row_ld in lockdown_dates:
	if row_ld[4] == 'National': #We only take national lockdowns, because the OWID data does not include subnational data.
		row_ldwd = {}
		row_ldwd['country'] = row_ld[0]
		row_ldwd['lockdown_start_date'] = (row_ld[2])[0:10] #Some of the dates from lockdown_dates include a footnote, for example '2020-03-13[3]'. We keep only the 10 first characters, corresponding to the date in format YYYY-MM-DD.
		for row_od in owid_data:
			if ((row_ldwd['country'] == row_od[1])
			and (row_ldwd['lockdown_start_date'] == row_od[2])):
				#Cast the figures to floats:
				row_ldwd['total_cases_per_million'] = float(row_od[7])
				row_ldwd['new_cases_per_million'] = float(row_od[8])
				row_ldwd['total_deaths_per_million'] = float(row_od[9])
				row_ldwd['new_deaths_per_million'] = float(row_od[10])
		lockdown_dates_with_data.append(row_ldwd)

#Remove countries for which there no data for the lockdown start date, otherwise we will get errors. They are El Salvador, Kosovo, Lybia and Samoa.
for row in lockdown_dates_with_data:
	if 'total_cases_per_million' not in row.keys():
		lockdown_dates_with_data.remove(row)

#Sort the list according to the total death per million:
lockdown_dates_with_data.sort(key = (lambda row: row['total_deaths_per_million']))

#Put the crossed dataset into a csv file:
with open('lockdown_dates_with_data.csv', 'w', encoding = 'ANSI') as outfile:
	outfile.flush()
	line = ','.join(lockdown_dates_with_data[1].keys())
	outfile.write(line + '\n')
	for row in lockdown_dates_with_data:
		line = ''
		for value in row.values():
			line = line + str(value) + ','
		line = line[0:-1] #remove the comma at the end
		outfile.write(line + '\n')

#Sort the list according to each of the metrics, and plot each of the metrics on a graph:

#Total cases per million:
lockdown_dates_with_data.sort(key = (lambda row: row['total_cases_per_million']))
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[row['country'] for row in lockdown_dates_with_data],y=[row['total_cases_per_million'] for row in lockdown_dates_with_data])],
    layout_title_text="Total cases per million"
)
fig.show()

#New cases per million:
lockdown_dates_with_data.sort(key = (lambda row: row['new_cases_per_million']))
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[row['country'] for row in lockdown_dates_with_data],y=[row['new_cases_per_million'] for row in lockdown_dates_with_data])],
    layout_title_text="New cases per million"
)
fig.show()

#Total deaths per million:
lockdown_dates_with_data.sort(key = (lambda row: row['total_deaths_per_million']))
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[row['country'] for row in lockdown_dates_with_data],y=[row['total_deaths_per_million'] for row in lockdown_dates_with_data])],
    layout_title_text="Total deaths per million"
)
fig.show()

#New deaths per million:
lockdown_dates_with_data.sort(key = (lambda row: row['new_deaths_per_million']))
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[row['country'] for row in lockdown_dates_with_data],y=[row['new_deaths_per_million'] for row in lockdown_dates_with_data])],
    layout_title_text="New deaths per million"
)
fig.show()
