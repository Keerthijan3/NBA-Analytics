import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sys

'''
This script is to extract required data from basketball-reference.com and save it into a pickle file. Output files are used for other scripts. 

If this code is run with a year passed as the argument, existing tables will be updated with that year. 

ex.
Create pickle files: python ExtractSeasonData.py
Update pickle files: python ExtractSeasonData.py 2019
'''

def ExtractTable(year):
    url = "https://www.basketball-reference.com/leagues/NBA_{}_totals.html".format(year)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', attrs={'class':'sortable stats_table'}).tbody
    cols = [th.getText() for th in soup.find('tr').find_all('th')][1:]
    data = []
    trs = table.findAll('tr')
    for tr in trs[1:]:
        tds = tr.findAll('td')
        row = [td.getText() for td in tds]
        data.append(row)
    df = pd.DataFrame(data, columns = cols)
    df.dropna(inplace=True)
    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df['Year']=year
    num_headers = ['G', 'GS', 'MP','3P', '3PA', '2P', '2PA', 'FT', 'FTA', 'ORB', 'DRB', 'AST', 'STL', 'BLK', 'PTS', 'Year']
    df[num_headers] =df[num_headers].astype(np.float32)
    return df

def CreateTable(start, end):
    '''

    Extracts data from start to end year. Creates a new table and saves.

    '''
    df = ExtractTable(start)
    for year in range(start+1,end+1):
        df2 = ExtractTable(year)
        df = pd.concat((df,df2))
    return df

def UpdateTable(year, df):
    '''
    Given a year, updates that year onto the table
    
    '''
    if year in df['Year'].values:
        return df
    df2 = ExtractTable(year)
    df = pd.concat((df,df2))
    return df

if __name__ == "__main__":
    try:
        year = sys.argv[1]
        df = pd.read_pickle("./Data/Seasons_Stats.pkl")
        df = UpdateTable(year, df)
        df.to_pickle("./Data/Seasons_Stats.pkl")
    except:
        df = CreateTable(1950, 2018)
        df.to_pickle("./Data/Seasons_Stats.pkl")
