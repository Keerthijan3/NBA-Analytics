'''
This script will output plots based on player heights and weights over the years. 
This can shed some insight how the ideal bodytype of NBA players has changed over the years
To filter by player position, pass it in as an argument. Positions are C, SG, PF, SF, PG

'''
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
players = pd.read_csv('../Data/Players.csv')
seasons = pd.read_csv('../Data/Seasons_Stats.csv')

try:
    pos = sys.argv[1]
    seasons = seasons[seasons['Pos']==pos]
    naming = "( " + pos + " )"
except:
    pos = ""
    naming=""
height_arr = list()
weight_arr = list()
year = list()
stddevh = list()
stddevw = list()
for i in range(1950, 2018):
    season_players = seasons[seasons['Year']==i]
    season_players = season_players['Player'].values
    player_data = players.loc[players['Player'].isin(season_players)]
    heights = player_data['height'].values
    weights = player_data['weight'].values
    height_arr.append(np.mean(heights))
    weight_arr.append(np.mean(weights))
    stddevh.append(np.std(heights))
    stddevw.append(np.std(weights))
    year.append(i)
    
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.plot(year, height_arr, color="#d1ae45")
ax.set_facecolor("#2E2E2E")
ax.set_title('Avg Height vs Year for NBA Players'+ naming, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('Height (cm)', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'heightvsyear.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.plot(year, stddevh, color="#d1ae45")
ax.set_facecolor("#2E2E2E")
ax.set_title(' Height Standard Deviation vs Year for NBA Players' + naming, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('Height (cm)', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'heightstdvsyear.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.plot(year, stddevw, color="#d1ae45")
ax.set_facecolor("#2E2E2E")
ax.set_title('Weight Standard Deviation vs Year for NBA Players' + naming, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('Weight (kg)', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'weightstdvsyear.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.plot(year, weight_arr, color="#d1ae45")
ax.set_facecolor("#2E2E2E")
ax.set_title('Avg Weight vs Year for NBA Players' + naming, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('Weight (kg)', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'weightvsyear.png')
