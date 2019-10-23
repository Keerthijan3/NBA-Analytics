# NBA-Analytics

This a repo of some NBA analysis scripts. Each script has more information on how to run it

AnalyzeHeightWeight: Outputs plots comparing player heights and weights over the years. This script also accepts a position to filter the players by position. From this script, studies of how the ideal NBA player's physique has changed over the years. (Are players today bigger than players from 20 years ago?)

Results: Avg player height and weight have been increasing until a bit before the 1990s. The standard deviation for the height/weight also increases before decreasing at ~1990.

PlayerAnalysis.py: This script similar to analyzes metrics of players over the years by position.

Results: A strong increase in 3 pointers have been seen in recent years. 

PCAVisualization.py: Often it is very difficult to measure how important a player is to a team. We have good defenders, goot scorers, good playmakers etc. But how can we judge how well of an all around player someone is. This script does two PCA of NBA players given a year. The first PCA uses offensive stats (PPG, APG, ORPG) and the second uses defensive stats (SPG, DRPG, BPG). As expected, players of high skill level are often outliers. Two axis for defense and offense are made which consists of various player skill metrics. 

Results: Players that perform better are often outliers in this PCA plot. How much of an outlier a player is can often tell us how important he is to the team. 


This repo used data from: https://www.kaggle.com/drgilermo/nba-players-stats
