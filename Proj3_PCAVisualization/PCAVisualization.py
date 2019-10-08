'''
This script creates a PCA analysis for NBA players where the y-axis is defense and x-axis is offense
Defense uses BPG, SPG, DRPG
Offense uses PPG, APG, ORPG
The script takes three arguments: year, players, fileoutput

ex. python PCAVisualization 2013 "[Carmelo Anthony, LeBron James, Kevin Durant]" outputfile

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from PIL import Image
import sys

def CreatePCA(year = 2017, targets = [], mingames=60, filename = None):
    players = pd.read_csv('../Data/Players.csv')
    seasons = pd.read_csv('../Data/Seasons_Stats.csv')
    season = seasons[seasons['Year']==year]
    df = season[['Player', 'Pos', 'G', 'GS', 'MP', 'ORB', 'DRB', 'AST', 'STL', 'BLK', 'PTS']]
    df['PPG'] = df['PTS']/df['G']
    df['BPG'] = df['BLK']/df['G']
    df['SPG'] = df['STL']/df['G']
    df['APG'] = df['AST']/df['G']
    df['DRPG'] = df['DRB']/df['G']
    df['ORPG'] = df['ORB']/df['G']
    df = df[df['G']>mingames]
    offencef = ['PPG', 'APG', 'ORPG']
    defencef = ['BPG', 'DRPG', 'SPG']
    xoff = df.loc[:, offencef].values
    xdef = df.loc[:, defencef].values
    y = df.loc[:,['Player']].values
    xoff = StandardScaler().fit_transform(xoff)
    xdef = StandardScaler().fit_transform(xdef)
    pca = PCA(n_components=1)
    xoff = pca.fit_transform(xoff)
    print(pca.components_)
    pca = PCA(n_components=1)
    xdef = pca.fit_transform(xdef)
    print(pca.components_)
    df = pd.DataFrame(data = xoff, columns = ['Offence'])
    df['Defence']=xdef
    df['Player'] = y
    dfog = df.copy()
    df.loc[~df.Player.isin(targets), 'Player'] = 'Others'
    targets=['Others']+targets
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Offence', labelpad=15, fontsize=12)
    ax.set_ylabel('Defence', labelpad=15, fontsize=12)
    ax.set_title('Player Offence and Defence for ' +str(year-1)+'-'+str(year), fontsize = 16)
    colors = ['gray', 'r', 'g', 'b', 'c', 'm', 'y', 'k']
    colors = colors[0:len(targets)]
    for target, color in zip(targets,colors):
        indicesToKeep = df['Player'] == target
        ax.scatter(df.loc[indicesToKeep, 'Offence']
               , df.loc[indicesToKeep, 'Defence']
               , c = color
               , s = 50)
    ax.legend(targets)
    ax.grid()
    if filename != None:
        plt.savefig(filename+'.png')
    return dfog

year = int(sys.argv[1])
filename = sys.argv[3]
players = sys.argv[2].strip('[]').split(',')
players = [players[0]]+[player[1:] for player in players[1:]]
df = CreatePCA(year,players, filename = filename)
