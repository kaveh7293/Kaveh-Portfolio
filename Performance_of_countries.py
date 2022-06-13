# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:40:44 2022

@author: kaveh
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
os.chdir('G:/WORLD_CUP_data')
data=pd.read_csv('WorldCup.csv')


import re
X_winers=[]
X_losers=[]
X_draws=[]
j=0
# for loop to collect the winners in all the games
for i in range(288):
    if data.iloc[i,11]==0:
        
        xa=list(data.iloc[i,[0,1,2,3,4,12]].values)
        if re.split("\'", xa[0])[0]=='':
            xa[0]=re.split("\'", xa[0])[1]
        else:
            xa[0]=re.split("\'", xa[0])[0]

        if re.split("\'", xa[1])[0]=='':
            xa[1]=re.split("\'", xa[1])[1]
        else:
            xa[1]=re.split("\'", xa[1])[0]

        xb=list(data.iloc[i,[5,6,7,8,9,12]].values)
        if re.split("\'", xb[0])[0]=='':
            xb[0]=re.split("\'", xb[0])[1]
        else:
            xb[0]=re.split("\'", xb[0])[0]

        if re.split("\'", xb[1])[0]=='':
            xb[1]=re.split("\'", xb[1])[1]
        else:
            xb[1]=re.split("\'", xb[1])[0]

        X_winers.append(xa)
        X_losers.append(xb)
    elif data.iloc[i,11]==2:
        xa=list(data.iloc[i,[5,6,7,8,9,12]].values)
        if re.split("\'", xa[0])[0]=='':
            xa[0]=re.split("\'", xa[0])[1]
        else:
            xa[0]=re.split("\'", xa[0])[0]

        if re.split("\'", xa[1])[0]=='':
            xa[1]=re.split("\'", xa[1])[1]
        else:
            xa[1]=re.split("\'", xa[1])[0]

        
        xb=list(data.iloc[i,[0,1,2,3,4,12]].values)
        if re.split("\'", xb[0])[0]=='':
            xb[0]=re.split("\'", xb[0])[1]
        else:
            xb[0]=re.split("\'", xb[0])[0]

        if re.split("\'", xb[1])[0]=='':
            xb[1]=re.split("\'", xb[1])[1]
        else:
            xb[1]=re.split("\'", xb[1])[0]
    else:
        xd1=list(data.iloc[i,[5,6,7,8,9,12]].values)
        if re.split("\'", xd1[0])[0]=='':
            xd1[0]=re.split("\'", xd1[0])[1]
        else:
            xd1[0]=re.split("\'", xd1[0])[0]

        if re.split("\'", xd1[1])[0]=='':
            xd1[1]=re.split("\'", xd1[1])[1]
        else:
            xd1[1]=re.split("\'", xd1[1])[0]

        
        xd2=list(data.iloc[i,[0,1,2,3,4,12]].values)
        if re.split("\'", xd2[0])[0]=='':
            xd2[0]=re.split("\'", xd2[0])[1]
        else:
            xd2[0]=re.split("\'", xd2[0])[0]

        if re.split("\'", xd2[1])[0]=='':
            xd2[1]=re.split("\'", xd2[1])[1]
        else:
            xd2[1]=re.split("\'", xd2[1])[0]

        
        X_winers.append(xa)
        X_losers.append(xb)
        X_draws.append(xd1)
        X_draws.append(xd2)
WINS=pd.DataFrame(X_winers)
WINS.columns=['Country','Continent','Ranking','Num_Chapionships','IsHost','Year']
LOSES=pd.DataFrame(X_losers)
LOSES.columns=['Country','Continent','Ranking','Num_Chapionships','IsHost','Year']
DRAWS=pd.DataFrame(X_draws)
DRAWS.columns=['Country','Continent','Ranking','Num_Chapionships','IsHost','Year']
WINS['Points']=3
LOSES['Points']=0
DRAWS['Points']=1
data.head()
all_result=pd.concat([WINS,LOSES,DRAWS],ignore_index=True)
plt.figure(figsize=(10,8))

sns.countplot(x='Continent',hue='Result',data=all_result)
plt.figure(figsize=(10,8))
df_sorted_ii = all_result.sort_values(['Continent'])
sns.barplot(x='Continent',y='Points',data=df_sorted_ii)
df_sorted = all_result.sort_values(['Continent','Result'])
for i in ['Africa', 'Asia', 'Concacaf', 'Europe', 'Oceania', 'South_America']:
    plt.figure(figsize=(6,4))
    sns.barplot(x='Year',y='Points',data=df_sorted[df_sorted.Continent==i])
    plt.xlabel(' {}'.format(i))
    plt.ylim([0,3])