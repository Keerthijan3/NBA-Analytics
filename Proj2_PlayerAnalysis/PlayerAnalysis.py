'''
This script will be used to evaluate how player skillset has changed over the years for different positions
The script must be passed a position (C, SG, SF, PF, PG)

'''

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    pos = sys.argv[1]
except:
    print("Position not passed!")
    sys.exit()
    

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

players = pd.read_csv('../Data/Players.csv')
seasons = pd.read_csv('../Data/Seasons_Stats.csv')

seasons = seasons[seasons['Year']>1979]
seasons_centers = seasons[seasons['Pos']==pos]
df = seasons_centers[['Year', 'Player', 'G', 'USG%', '3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB', 'DRB', 'AST', 'STL', 'BLK', 'PTS']]
threepoint = list()
threepointa = list()
twopoint = list()
twopointa = list()
ft = list()
fta = list()
orb = list()
drb = list()
ast = list()
stl = list()
blk = list()
pts = list()
usg = list()
years = list()
for year in range(1980, 2018):
    dfyear = df[df['Year']==year]
    threepoint.append(np.mean(dfyear['3P'].values/dfyear['G'].values))
    threepointa.append(np.mean(dfyear['3PA'].values/dfyear['G'].values))
    twopoint.append(np.mean(dfyear['2P'].values/dfyear['G'].values))
    twopointa.append(np.mean(dfyear['2PA'].values/dfyear['G'].values))
    ft.append(np.mean(dfyear['FT'].values/dfyear['G'].values))
    fta.append(np.mean(dfyear['FTA'].values/dfyear['G'].values))
    orb.append(np.mean(dfyear['ORB'].values/dfyear['G'].values))
    drb.append(np.mean(dfyear['DRB'].values/dfyear['G'].values))
    ast.append(np.mean(dfyear['AST'].values/dfyear['G'].values))
    stl.append(np.mean(dfyear['STL'].values/dfyear['G'].values))
    blk.append(np.mean(dfyear['BLK'].values/dfyear['G'].values))
    pts.append(np.mean(dfyear['PTS'].values/dfyear['G'].values))
    usg.append(np.mean(dfyear['USG%'].values))
    years.append(year)

Plot(years, threepoint, 'Three Pointers per Game for ' + pos, pos + 'threep.png', 'Pts/game')
Plot(years, threepointa, 'Three Pointers Attempted per Game for ' + pos, pos + 'threea.png', 'Pts/game')
Plot(years, twopoint, 'Two Pointers per Game for ' + pos, pos + 'twop.png', 'Pts/game')
Plot(years, twopointa, 'Two Pointers Attempted of ' + pos, pos + 'twoa.png', 'Pts/game')
Plot(years, ft, 'Free Throws per Game for ' + pos, pos + 'ftp.png', 'Pts/game')
Plot(years, orb, 'Offensive Rebounds per Game for ' + pos, pos + 'orb.png', 'Reb/game')
Plot(years, drb, 'Defensive Rebounds per Game for ' + pos, pos + 'reb.png', 'Reb/game')
Plot(years, ast, 'Assists per Game for ' + pos, pos + 'ast.png', 'Ast/game')
Plot(years, stl, 'Steals per Game for ' + pos, pos + 'stl.png', 'Stl/game') 
Plot(years, blk, 'Blocks per Game for' + pos, pos + 'blk.png', 'Blk/game')
Plot(years, pts, 'Points per Game for' + pos, pos + 'ppg.png', 'Pts/game')