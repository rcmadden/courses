"""
open the csv file called "nfl_offensive_stats.csv" and
read in the csv data from the file
"""
import pandas as pd

nfl_stats = pd.read_csv('nfl_offensive_stats.csv')
print(nfl_stats.head())

"""
in the data we just read in, the fourth column is the player 
and the 8th column is the passing yards. Get the sum of yards from
column 8 where the 4th column value is "Aaron Rodgers
"""

aaron_rodgers = nfl_stats[(nfl_stats['player'] == 'Aaron Rodgers') & (nfl_stats['game_date'] >= '2019-01-01') & (nfl_stats['game_date'] <= '2022-12-31')]
print(aaron_rodgers) # this was added to test the list

print(aaron_rodgers['pass_yds'].sum())

# using the exact prompts from the course it continued to return the wrong code from
# nfl_stats_v2.py
# even though i closed the editor and did not repoen the v2.py file on retry

# TODO: try exact same prompts after computer restart
  