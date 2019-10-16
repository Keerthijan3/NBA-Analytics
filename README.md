# NBA-Analytics

This a repo of some NBA analysis scripts. Each script has more information on how to run it

AnalyzeHeightWeight.py: Outputs plots based on NBA player heights and weights over the years. The standard deviation is also outputted. This script also accepts a position to filter the players by position. From this script, studies of how the ideal NBA player's physique has changed over the years. (Are players today bigger than players from 20 years ago?)

PlayerAnalysis.py: This script similar to analyzes metrics of players over the years by position. (ex. how much more three pointers are taken by centers?)

PCAVisualization.py: Often it is very difficult to measure how important a player is to a team. We have good defenders, goot scorers, good playmakers etc. But how can we judge how well of an all around player someone is. This script does two PCA of NBA players given a year. The first PCA uses offensive stats (PPG, APG, ORPG) and the second uses defensive stats (SPG, DRPG, BPG). As expected, players of high skill level are often outliers. Two axis for defense and offense are made which consists of various player skill metrics. 


This repo used data from: https://www.kaggle.com/drgilermo/nba-players-stats
