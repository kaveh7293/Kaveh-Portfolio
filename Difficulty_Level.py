# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 18:57:28 2022

@author: kaveh
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
os.chdir('G:/WORLD_CUP_data')
data=pd.read_csv('WorldCup.csv')
data_ch=data[['Rank1','Rank2','world_cup','Group']]
data_grouped=data_ch.groupby(by=['world_cup','Group']).mean()
data_ch_visualization=data_ch.copy()
data_ch_visualization['Ranks']=0.5*(data_ch['Rank1']+data_ch['Rank2'])
data_ch_cis=data_ch_visualization[data_ch_visualization.world_cup==1998]
data_ch_cis=data_ch_cis.sort_values('Group')
data_ch_visualization.iloc[0:48,:]=data_ch_cis
plt.figure(figsize=(10,8))
for i in [1998,2002,2006,2010,2014,2018]:
    plt.figure(figsize=(10,8))
    sns.barplot(x='world_cup', y='Ranks', hue='Group', data=data_ch_visualization[data_ch_visualization.world_cup==i])
    plt.ylabel('Average Ranking')
data_grouped['average_ranks']=0.5*(data_grouped['Rank1']+data_grouped['Rank2'])

dict={1:1998,2:2002,3:2006,4:2010,5:2014,6:2018}
ind=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
death_group={}
death_group_year={}
for i in range(1,7):
   death_group[dict[i]]=data_grouped.loc[(dict[i],),'average_ranks']==data_grouped.loc[(dict[i],),'average_ranks'].min()
for i in range(1,7):
    for j in range(0,8):
        if death_group[dict[i]].iloc[j]==True:
            death_group_year[dict[i]]=ind[j]
            teams1=data[(data.Group=='E') & (data.world_cup==1998)][['Team1']]
            teams2=data[(data.Group=='E') & (data.world_cup==1998)][['Team2']]
        
for k,s in death_group_year.items():
    print('The death group in',str(k), 'is:',s)
    ds=data[(data.Group==s) & (data.world_cup==k)][['Team1','Team2']]
    datas=pd.concat([ds.Team1,ds.Team2])
    print('the group teams were',datas.unique())
dict={1:1998,2:2002,3:2006,4:2010,5:2014,6:2018}
ind=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
easy_group={}
easy_group_year={}
for i in range(1,7):
   easy_group[dict[i]]=data_grouped.loc[(dict[i],),'average_ranks']==data_grouped.loc[(dict[i],),'average_ranks'].max()
for i in range(1,7):
    for j in range(0,8):
        if easy_group[dict[i]].iloc[j]==True:
            easy_group_year[dict[i]]=ind[j]
            teams1=data[(data.Group=='E') & (data.world_cup==1998)][['Team1']]
            teams2=data[(data.Group=='E') & (data.world_cup==1998)][['Team2']]
easy_group_year
for k,s in easy_group_year.items():
    print('The easiest group in',str(k), 'is:',s)
    ds=data[(data.Group==s) & (data.world_cup==k)][['Team1','Team2']]
    datas=pd.concat([ds.Team1,ds.Team2])
    print('the group teams were',datas.unique())