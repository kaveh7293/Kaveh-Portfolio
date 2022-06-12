# [Project 1 World Cup Project](https://github.com/kaveh7293/Kaveh-Portfolio)
Example Data Science Portfolio
## Overview for the Project
* The data from group stage world cups between 1998 to 2018 were collected to obtain a model from which the results of group stage world cup in 2022 can be predicted. The csv file for the data can be found [here](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/WorldCup.csv)
* A multi-class classfication model is fitted and used to predict wehther the first team wins, the teams draw or the second team wins
* The features which are used for this classfiction problem are the name of the countries, the teams continent, fifa ranking, the number of previous world champtionships, and wehther they were the host
*Before start model building, I answered some of the questions that I had in my mind:
  * What were the hardest groups in the group stage in each of the previous world cups. I chose the hardest group based on the smallest average of the fifa world    ranking in each group. We plot a barplot to return the average of the teams rankings in each of the world cups:
  
  
   ![](https://raw.githubusercontent.com/kaveh7293/Kaveh-Portfolio/main/images/1998.png)
   ![](https://raw.githubusercontent.com/kaveh7293/Kaveh-Portfolio/main/images/2002.png)
   ![](https://raw.githubusercontent.com/kaveh7293/Kaveh-Portfolio/main/images/2006.png)
   ![](https://raw.githubusercontent.com/kaveh7293/Kaveh-Portfolio/main/images/2010.png)
   ![](https://raw.githubusercontent.com/kaveh7293/Kaveh-Portfolio/main/images/2014.png)
   ![](https://raw.githubusercontent.com/kaveh7293/Kaveh-Portfolio/main/images/2018.png)
   
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
          
