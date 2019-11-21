import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sys
from string import ascii_lowercase

'''
This script is to extract required player data from basketball-reference.com and save it into a pickle file. Output files are used for other scripts.
'''

def ExtractTable():
    for letter in ascii_lowercase:
        url = "https://www.basketball-reference.com/players/{}".format(letter)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', attrs={'class':'sortable stats_table'})
        if table==None:
            continue
        else:
            table = table.tbody
        cols = [th.getText() for th in soup.find('tr').find_all('th')]
        data = []
        trs = table.findAll('tr')
        for tr in trs:
            ths = tr.findAll('th')
            tds = tr.findAll('td')
            row = [th.getText() for th in ths]
            row = row + [td.getText() for td in tds]
            data.append(row)
        df = pd.DataFrame(data, columns = cols)
        if letter=='a':
            dftot = df
        else:
            dftot = pd.concat((dftot,df))
    dftot.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    dftot.dropna(inplace=True)
    ht = dftot['Ht'].values
    ht2=[]
    for i in range(0,len(ht)):
        imp = ht[i].split('-')
        met = int(imp[0])*30.48 + int(imp[1])*2.54
        ht2.append(int(met))
    dftot['height'] = ht2
    dftot['weight']=dftot['Wt'].astype(np.uint8)*0.453592
    dftot['weight']=dftot['weight'].astype(np.uint8)
    return dftot

if __name__ == "__main__":
    df = ExtractTable()
    df.to_pickle("./Data/Players.pkl")