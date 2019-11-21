'''
This script will output plots based on player heights and weights over
the years.
This can shed some insight how the ideal bodytype of NBA players has 
changed over the years
To filter by player position, pass it in as an argument. Positions 
are C, SG, PF, SF, PG

'''
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


def Plot(x, y, title, filename, ylabel):
    '''
    Function to create plots and save

    '''
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, color="#d1ae45")
    ax.set_facecolor("#2E2E2E")
    ax.set_title(title, fontsize=16)
    ax.set_xlabel('Year', labelpad=15, fontsize=12)
    ax.set_ylabel(ylabel, labelpad=15, fontsize=12)
    plt.grid(True, color="#93a1a1", alpha=0.1)
    plt.savefig(filename)
    plt.close()


players = pd.read_pickle('Data/Players.pkl')
seasons = pd.read_pickle('Data/Seasons_Stats.pkl')

try:
    pos = sys.argv[1]
    seasons = seasons[seasons['Pos'] == pos]
    naming = "( " + pos + " )"
except:
    pos = ""
    naming = ""

height_arr = list()
weight_arr = list()
year = list()
stddevh = list()
stddevw = list()
for i in range(1950, 2018):
    season_players = seasons[seasons['Year'] == i]
    season_players = season_players['Player'].values
    player_data = players.loc[players['Player'].isin(season_players)]
    heights = player_data['height'].values
    weights = player_data['weight'].values
    height_arr.append(np.mean(heights))
    weight_arr.append(np.mean(weights))
    stddevh.append(np.std(heights))
    stddevw.append(np.std(weights))
    year.append(i) 
Plot(
    year, height_arr, 'Avg Height vs Year for NBA Players' + naming,
    pos+'heightvsyear.png', 'Height(cm)'
)
Plot(
    year, stddevh, 'Height Std. Dev. vs Year for NBA Players' + naming,
    pos+'heightstdvsyear.png', 'Height (cm)'
)
Plot(
    year, stddevw, 'Weight Std. Dev. vs Year for NBA Players' + naming,
    pos + 'weightstdvsyear.png', 'Weight (kg)'
)
Plot(
    year, weight_arr, 'Avg Weight vs Year for NBA Players' + naming,
    pos + 'weightvsyear.png', 'Weight (kg)'
)
