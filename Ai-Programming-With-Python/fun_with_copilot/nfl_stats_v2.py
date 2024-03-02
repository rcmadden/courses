'''from the file nfl_offinsive_stats.csv,
   get the total number of pass_yds for the player Aaron Rodgers
   where game_date is between the years 2019 and 2022'''

import pandas as pd

# read the csv file
nfl_stats = pd.read_csv('nfl_offensive_stats.csv')

# filter the data
# copilot gave player_name instead of player
aaron_rodgers = nfl_stats[(nfl_stats['player'] == 'Aaron Rodgers') & (nfl_stats['game_date'] >= '2019-01-01') & (nfl_stats['game_date'] <= '2022-12-31')]
print(aaron_rodgers) # this was added to test the list
print(aaron_rodgers['pass_yds'].sum())

# the list comprehension did not work as expected
