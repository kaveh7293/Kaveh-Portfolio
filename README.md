# [Project 1 World Cup Project](https://github.com/kaveh7293/Kaveh-Portfolio)
Example Data Science Portfolio
## Overview for the Project
* The data from group stage world cups between 1998 to 2018 were collected to obtain a model from which the results of group stage world cup in 2022 can be predicted. The csv file for the data can be found [here](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/WorldCup.csv)
* A multi-class classfication model is fitted and used to predict wehther the first team wins, the teams draw or the second team wins
* The features which are used for this classfiction problem are the name of the countries, the teams continent, fifa ranking, the number of previous world champtionships, and wehther they were the host
*Before start model building, I answered some of the questions that I had in my mind:
  * What were the hardest groups in the group stage in each of the previous world cups. I chose the hardest group based on the smallest average of the fifa world    ranking in each group. We plot a barplot to return the average of the teams rankings in each of the world cups:
  
  
   ![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/1998.png)
   ![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2002.png)
   ![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2006.png)
   ![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2010.png)
   ![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2014.png)
   ![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2018.png)
   
The groups with the lowest average ranking are the hardest (death groups) and the groups with the maximum ranking are the easiest. We also determined this using python code 
  * The following results were obtained by our python code and can be seen from barplots as well:          *The death group in 1998 is: H
         the group teams were ["Japan'" "Argentina'" "Croatia'" "Jamaica'"]
         
         *The death group in 2002 is: F
         the group teams were ["Argentina'" "England'" "Nigeria'" "Sweden'"]
         
         *The death group in 2006 is: E
         the group teams were ["Italy'" "Ghana'" "Czechia'" "USA'"]
         
         *The death group in 2010 is: D
         the group teams were ["Germany'" "Australia'" "Ghana'" "Serbia'"]
         
         *The death group in 2014 is: D
         the group teams were ["Uruguay'" "Costa_Rica'" "Italy'" "England'"]
         
         *The death group in 2018 is: E
         the group teams were ["Brazil'" "Costa_Rica'" "Serbia'" "Switzerland'"]

  * The easiest groups are:
  
          *The easiest group in 1998 is: D
          the group teams were ["Spain'" "Paraguay'" "Bulgaria'" "Nigeria'"]
          
          *The easiest group in 2002 is: H
          the group teams were ["Japan'" "Belgium'" "Tunisia'" "Russia'"]
          
          *The easiest group in 2006 is: G
          the group teams were ["Switzerland'" "South_Korea'" "France'" "Togo'"]
          
          *The easiest group in 2010 is: F
          the group teams were ["Italy'" "Paraguay'" "New_Zealand'" "Slovakia'"]
          
          *The easiest group in 2014 is: F
          the group teams were ["Argentina'" "Bosnia'" "Iran'" "Nigeria'"]
          
          *The easiest group in 2018 is: A
          the group teams were ["Uruguay'" "Russia'" "Saudi_Arabia'" "Egypt'"]
          
The code for the above results can be found [here](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Difficulty_Level.py)
  * some additional information can be interpreted from above plots are:
  * the error bars show the standard deviations of the fifa world rankings of the teams in each group. The smaller standard deviations means that the teams performance from which the fifa world ranking has been obtained were relatively similar. However, the larger standard deviations shows that the teams level are more different and probably there was not a severe competition between the teams for qualifying into knock out stage
  * The height of the barplots for each group can be used to evaluated whether the fifa world ranking is fair because only 32 teams are qualified into the world cup. As shown, in most of the cases, the average of the rankings are arround 15 to 50. The groups whose average rankings are over 30 probably contain teams which are either the host (so they do not need to compete for qualification) or their fifa world ranking is well-determined. Another reason could be infair contribution of different continents. For example, in 2006 world cup none of the 4 Asian teams were qualified into the next stage.
  * To have groups with similar level of difficulties, fifa divided teams into four different categorizes. In each group, there are only one team from each category. The uniform height of the bar plots at each year can show the same level of difficulties for that world cup.

## Performance of different continents in all the worldcups. 
In the following we show the number of wins, loses and draws for the teams from different continents. Teams from Europ and South America have the highest ratio of win/lose and win/draw compared to countries from different continents. This justify the lower number of teams from Asia and Africa in the world cup. In the following we investigate whether there is an improve in the performance of the countries from Asia, Africa and Concacaf regions. FIFA usually plans to improce the performance of the countries from these regions to make the World Cup more exciting
* This is the countplot for the performance of different continents in the world cups:
![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Continents_Performances.png)

As shown, only the countries from Europe and South America have more wins than draws and loses

A better plot can be the average points per game for the contries from different countries:

![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Continents_Performances_Points.png)

In the following the plot of average points per game for countries from different continents are shown for different world cup years:

![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Africa.png)
![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Asia.png)
![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Concacaf.png)
![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Europe.png)
![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Oceania.png)
![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/South_America.png)

The plot shows that African countries performances get worse after world cup 1998. Asian countries performance is better in 2002, 2010 and 2018 world cups compared to their performance in 2006 and 20014. THe best performace of Asian countries is in world cup 2002 when Japan and Korea were the hosts. South American counteries performance was very bad in 2002 with an average of about 0.6 points per game (Uruguay and Argentina were eliminated in the group stage). 
The code for generation of the above results can be found [here](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Performance_of_countries.py)

## Effect of different features on the results
The effect of features can be seen using count plot and heat map plot generated from contingency table:
![] (https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Country_Effect_losts.png)
