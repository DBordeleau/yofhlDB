import cs50
import pandas as pd

# list of data frames that we will read from the html page and then append to our final data frame
list_dfs = []

# loop through all seasons and read data into our list, using 10 years for sample data
for year in range (1980, 2004):
    url = f"https://www.hockey-reference.com/leagues/NHL_{year}_skaters.html"
    list_dfs.append(pd.read_html(url, header=1)[0].assign(year=year))

# adding all to final data object that we will export to a csv file. Sometimes player stats don't have age listed for some reason
result = (pd.concat(list_dfs).loc[lambda x: ~x["Age"].str.contains("Age")]
              .reset_index(drop=True))

# output to csv file that will be used to make db
result.to_csv("hdb_data_3.csv", index=False)