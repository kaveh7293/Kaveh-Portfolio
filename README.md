# [Project 1 World Cup Project](https://github.com/kaveh7293/Kaveh-Portfolio)
Example Data Science Portfolio
#World Cup Project
* The data from group stage world cups between 1998 to 2018 were collected to obtain a model from which the results of group stage world cup in 2022 can be predicted
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
   
The groups with the lowest average ranking are the hardest and the groups with the maximum ranking are the easiest. We also determined this using python code 
  * The result for each world cup is as follows:

