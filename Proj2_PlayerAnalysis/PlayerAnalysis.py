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

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, threepoint, color="#d1ae45")
ax.set_title('Three Pointers of ' + pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('3PG', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'threep.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, threepointa, color="#d1ae45")
ax.set_title('Three Pointers Attempted of '+pos, fontsize=16)
ax.set_xlabel('Year', labelpad = 15, fontsize=12)
ax.set_ylabel('3PG', labelpad = 15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'threea.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, twopoint, color="#d1ae45")
ax.set_title('Two Pointers of of '+ pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('2PG', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'twop.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, twopointa, color="#d1ae45")
ax.set_title('Two Pointers Attempted of '+ pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('Pts/game', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'twoa.png')


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, ft, color="#d1ae45")
ax.set_title('FT of '+pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('Pts/game', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'ftp.png')


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, orb, color="#d1ae45")
ax.set_title('ORB of '+pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('Reb/game', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'orb.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, drb, color="#d1ae45")
ax.set_title('DRB of '+pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('Reb/game', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'reb.png')


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, ast, color="#d1ae45")
ax.set_title('AST of '+pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('AST/game', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'ast.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, stl, color="#d1ae45")
ax.set_title('STL of '+pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('STL/game', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'stl.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, blk, color="#d1ae45")
ax.set_title('BLK of '+pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('BLK/game', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'blk.png')

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111)
ax.set_facecolor("#2E2E2E")
ax.plot(years, pts, color="#d1ae45")
ax.set_title('PTS of '+pos, fontsize=16)
ax.set_xlabel('Year', labelpad=15, fontsize=12)
ax.set_ylabel('Pts/game', labelpad=15, fontsize=12)
plt.grid(True, color="#93a1a1", alpha=0.1)
plt.savefig(pos+'ppg.png')