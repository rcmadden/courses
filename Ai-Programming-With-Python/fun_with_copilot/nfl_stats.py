"""
open the csv file called "nfl_offensive_stats.csv" and
read in the csv data from the file
"""
import csv
with open("nfl_offensive_stats.csv", "r") as nfl_file:
    # read the csv data
    nfl_data = list(csv.reader(nfl_file))

# NOTE: copilot provided the above code with list() which
# threw ValueError: I/O operation on closed file.
"""                                                              ③
the 3rd column in data is player position, the fourth column     ③
is the player, and the 8th column is the passing yards.          ③
For each player whose position in column 3 is "QB",              ③
determine the sum of yards from column 8                         ③
"""
# create a dictionary to hold the player name and passing yards
player_yards = {}
# loop through the data
for row in nfl_data:
    # if the position is QB
    if row[2] == "QB":
        # if the player is already in the dictionary
        if row[3] in player_yards:
            # add the yards to the player's total
            player_yards[row[3]] += int(row[7])
        else:
            # add the player to the dictionary
            player_yards[row[3]] = int(row[7])
"""                                                              ④
print the sum of the passing yards sorted by sum                 ④
of passing yards in descending order 
Do not include Tom Brady because he wins too much                            ④
"""
for player in sorted(player_yards, key=player_yards.get, reverse=True):
    if player != "Tom Brady":
        print(player, player_yards[player])


# NOTE: had to seed copilot with for keyword after prompt2 2 & 3
    # Prompt 1. Read in the data
    # prompt 2. Analyze the data
    # prompt 3. Print the results
        
"""
plot the players by their number of passing yards only for 
players with more than 4000 passing yards
"""
import matplotlib.pyplot as plt
import numpy as np
# create a list of the players with more than 4000 yards
players = [player for player in player_yards if player_yards[player] > 4000]
# create a list of the yards for each player
yards = [player_yards[player] for player in players]
# create a list of the x values
x = np.arange(len(players))
# create a bar chart
plt.bar(x, yards)
# add the player names to the x-axis
plt.xticks(x, players)
# add a title
plt.title("NFL Players Passing Yards")
# add a label to the y-axis
plt.ylabel("Yards")
# display the plot
plt.show()

# NOTE: had to seed the above to import numpy
# results did not sort or rotate x-axis labels like example
# however a bar chart was created with the correct data