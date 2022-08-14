# [Project 1 World Cup Project](https://github.com/kaveh7293/Kaveh-Portfolio)
Example Data Science Portfolio
<h2> Overview of the Project</h2>
<ul>
<li>The data from group stage world cups between 1998 to 2018 were collected to obtain a model from which the results of group stage world cup in 2022 can be predicted. The csv file for the data can be found <a href='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/WorldCup.csv'>here. </a></li>
<li> A multi-class classfication model is fitted and used to predict wehther the first team wins, the teams draw or the second team wins.</li>
<li> The features which are used for this classfiction problem are the name of the countries, the teams continent, fifa ranking, the number of previous world champtionships, and wehther they were the host.</li>
<li>I first did some explanatory data analysis to answer some of the questions I had in my mind about the previous world cup. Then, I did some feature selection analysis to determine important features need to be selected for model training. Finally, I trained a random forest model to predict the results of the next world-cup in 2022.</li>
 </ul>
<h2> Determination of the Hardest Groups and the Easiest Groups in the Previous World-cups</h2> 
* What were the hardest groups in the group stage in each of the previous world cups. I chose the hardest group based on the smallest average of the fifa world    ranking in each group. We plot a barplot to return the average of the teams rankings in each of the world cups:
  
  <img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/1998.png'><br>
  <img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2002.png'><br>
  <img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2006.png'><br>
  <img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2010.png'><br>
  <img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2014.png'><br>
  <img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/2018.png'><br>

   
<p>The groups with the lowest average ranking are the hardest (death groups) and the groups with the maximum ranking are the easiest. We also determined this using python code.</p> 
<p> The following results were obtained by our python code and can be seen from barplots as well. The hardest group in the previous world-cups were: 
  <ul>         
         <li>The death group in 1998 is: H (the group teams were Japan, Argentina, Croatia, and Jamaica)</li>
         <li>The death group in 2002 is: F (the group teams were Argentina, England, Nigeria, and Sweden)</li>
         <li> The death group in 2006 is: E (the group teams were Italy, Ghana, Czechia, and USA)</li>
         <li>The death group in 2010 is: D (the group teams were Germany, Australia, Ghana, and Serbia)</li>         
         <li>The death group in 2014 is: D (the group teams were Uruguay, Costa_Rica, Italy, and England)</li>         
         <li>The death group in 2018 is: E (the group teams were Brazil, Costa_Rica, Serbia, and Switzerland)</li>
</ul></p>
<p>The easiest groups are:
<ul> 
<li>The easiest group in 1998 is: D (the group teams were Spain, Paraguay, Bulgaria, and Nigeria)</li>
<li>The easiest group in 2002 is: H (the group teams were Japan, Belgium, Tunisia, and Russia)</li>
<li> The easiest group in 2006 is: G (the group teams were Switzerland, South_Korea, France, and Togo)</li>
<li> The easiest group in 2010 is: F (the group teams were Italy, Paraguay, New_Zealand, and Slovakia)</li>
<li> The easiest group in 2014 is: F (the group teams were Argentina, Bosnia, Iran,and Nigeria)
<li> The easiest group in 2018 is: A (the group teams were Uruguay, Russia, Saudi_Arabia, and Egypt)</li>
          
The code for the above results can be found [here](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Difficulty_Level.py)

<p>some additional information can be interpreted from above plots are:
 <ol>
  <li>the error bars show the standard deviations of the fifa world rankings of the teams in each group. The smaller standard deviations means that the teams performance from which the fifa world ranking has been obtained were relatively similar. However, the larger standard deviations shows that the teams level are more different and probably there was not a severe competition between the teams for qualifying into knock out stage</li>
 <li>The height of the barplots for each group can be used to evaluated whether the fifa world ranking is fair because only 32 teams are qualified into the world cup. As shown, in most of the cases, the average of the rankings are arround 15 to 50. The groups whose average rankings are over 30 probably contain teams which are either the host (so they do not need to compete for qualification) or their fifa world ranking is well-determined. Another reason could be infair contribution of different continents. For example, in 2006 world cup none of the 4 Asian teams were qualified into the next stage.</li>
<li> To have groups with similar level of difficulties, fifa divided teams into four different categorizes. In each group, there are only one team from each category. The uniform height of the bar plots at each year can show the same level of difficulties for that world cup.</li>
   </p>

<h2> Performance of Different Continents in the Previous World-cups. </h2>
<p>In the following we show the number of wins, loses and draws for the teams from different continents. Teams from Europ and South America have the highest ratio of win/lose and win/draw compared to countries from different continents. This justify the lower number of teams from Asia and Africa in the world cup. In the following we investigate whether there is an improve in the performance of the countries from Asia, Africa and Concacaf regions. FIFA usually plans to improce the performance of the countries from these regions to make the World Cup more exciting.</p>
* This is the countplot for the performance of different continents in the world cups:
![](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Continents_Performances.png)

As shown, only the countries from Europe and South America have more wins than draws and loses


In the following the plot of average points per game for countries from different continents are shown for different world cup years:<br>

<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Africa.png'><br>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Concacaf.png'><br>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Europe.png'><br>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Oceania.png'><br>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/South_America.png'><br>

<p>The plot shows that African countries performances get worse after world cup 1998. Asian countries performance is better in 2002, 2010 and 2018 world cups compared to their performance in 2006 and 20014. THe best performace of Asian countries is in world cup 2002 when Japan and Korea were the hosts. South American counteries performance was very bad in 2002 with an average of about 0.6 points per game (Uruguay and Argentina were eliminated in the group stage). 
The code for generation of the above results can be found [here](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Performance_of_countries.py)</p>

<h2> Feature Selection</h2>
 <p> I use several feature selection method which can be used in general to determine the important features which should be accounted for during classfication:<br>
  <ol>
   <li> Feature selection based on visualization</li>
   <li> Filter-based feature selection
   <ul>
     <li> Feature selection based on simple correlation matrix </li>
    <li> Feature selection based on hypothesis testing</li>
   </ul>
    <li>Wrapper-based feature selection</li></ol>
<h3> Feature selection based on visualization</h3>
 <p> This type of feature selection is not very statistically sound, but it is straightforward and can be used to obtain general information about the relationship between different features and the corresponding results. In the following the relationsip between country name and the corresponding results that they obtained were shown:<br>
 <img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Country_Effect_Wins.png'><br>
 <img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Country_Effect_losts.png'><br>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Country_Effect_draws.png'><br>

As shown, different teams have different number of wins, draws and loses. As such the name of the countries could be important feature which should be accounted for during model development.  </p>
 <p> The effect of fifa ranking and whether the countries are host or not are investigated in the folowing plots:<br>
  <img src='https://github.com/kaveh7293/World-Cup-Results-Prediction--Accuracy-of-Common-Sense-/blob/main/Picture4.png'><br>
  The effect of different teams from different continents on the corresponding results can also be investigated using a plot showing the average points per game for the contries from different countries:<br>

<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Continents_Performances_Points.png' width='420' height='300'><br>
As shown, the results of visualization is only good for checking the intuition and see a general trends. Different methods such as filter-based and feature-based techniques are better to be used to make statistical conclusion about the important features.
<h3> Filter-based feature selection</h3>
 <h4>Feature selection based on hypothesis testing</h4>
 
 Because we have different types of features, different statistical hypothesis tests should be make to find out whether the corresponding results are dependant on specific features. The chi-squared test has been used to evaluate whether cateogrical features have important effects on the corresponding team results. Note that to do chi-squared hypothesis tests, we first created a contingency table (using pandas.crosstab), and then using the contingency table we could perform the hypothesis test (using stats.chi2contingency). Further, we did an one-way Anova F-test to determine whether numerical features affect the results that the teams had. The numerical features are the fifa ranking and the number of previous championships. I used scipy.stats.f_oneway in order to implement this hypothesis test. The following table shows the results of the hypothesis test for different features that have been used. 
 
 <table>
  <tr>
    <th>Feature</th>
    <th>Feature Type</th>
    <th>Hypothesis Test</th>
    <th>Null Hypothesis</th>
   <th> p value</th>
   

  </tr>
  <tr>
    <td>Country</td>
    <td>Categorical</td>
    <td>Chi-squared test</td>
   <td>Depedent variable and the feature are independent</td>
   <td>1.99e-9</td>
  </tr>
  
  <tr>
    <td>Continents</td>
    <td>Categorical</td>
    <td>Chi-squared test</td>
   <td>Depedent variable and the feature are independent</td>
   <td>3.3e-9</td>
  </tr>
  <tr>
    <td>Being a host</td>
    <td>Categorical</td>
    <td>Chi-squared test</td>
   <td>Depedent variable and the feature are independent</td>
   <td>0.02</td>
  </tr>
  
  
  <tr>
    <td>Fifa ranking test</td>
    <td>Numerical</td>
    <td>One-way Anova F-test</td>
    <td>Depedent variable and the feature are independent</td>
    <td>1.88e-12</td>
  </tr>
  
  <tr>
    <td>Number of previous champioships</td>
    <td>Numerical</td>
    <td>One-way Anova F-test</td>
    <td>Depedent variable and the feature are independent</td>
    <td>1.82 e-6</td>
  </tr>
</table><br>
 <p> As shown for all of the hypothsis tests, the p-values are small, so we can reject the null hypthesis in favour of alternative hypothesis (i.e., all the features are important).
<h4> Feature-based selection based on correlation coefficients</h4>
<p> I also did a feature selection based on the correlation coefficient between the dependenet variable and the features that have been transformed (for those features that are categorical) and scaled. The following figures show that there are 211 features where a majority of them have very small correlation witht the dependent variable. The large number of features can be attributed to the onehot enconding which result a high number of columns since there are so many countries. 

<img src='https://github.com/kaveh7293/World-Cup-Results-Prediction--Accuracy-of-Common-Sense-/blob/main/download.png'>

 <h2> Feature Selection</h2>

 Hypothesis testing: Since both of the Country and Result columns are categorical, we did a chi-squared hypothesis test. The resulting p value obtained 1.99 e-9. As a reult we reject the null hypothesis in favour of alternative hypothesis (i.e., the country and results are dependent)

* Because the continents are also a cateogrical type of data, we used a chi-squared test as well to assess whether there is a relationship between continents and the corresponding results. The p-value for the corresponding hypothesis test (null hypothesis: continents and their results are independent variables) obtained 3.3 e-9, which rejects the null hypothesis. 
*  The corresponding p values for these tests obtained to be 1.88 e-12 (effect of fifa ranking) and 1.82 e-6 (effect of previous world championships), so we can assure that both of these features have effect on the performance of the teams on each game. The following plots also confirm the results of those hypothesis tests:<br>
 




<h2> Using a Model for Classification </h2>
<p> In this section we used several models to predict the results of the games in the previous wrold cups and then use the trained model to predict the results of world cup 2022 in Qatar. </p>

<p>I used a <strong> random forest model</strong> to train the data from the previous world cups. In the first model, we did not select the column countries, to avoid overfitting (there is a correlation between the countries and continents, as shown in the explanatory data analysis section, most of the countries from Europe and South America have a higher number of wins). I used a <strong>randomized-search cross-validation </strong> method (i.e., using sklearn.model_selection.RandomizedSearchCV) to select the appropriate hyperparameters. The following values for the corresponding hyperparameters are recommended based on the cross validation results:<br>
<strong>RandomForestClassifier(bootstrap=False, max_depth=54, max_features='sqrt',
                       min_samples_split=10, n_estimators=50)</strong><br>
The result of the corresponding classification modeling was  0.90 accuracy score for the training data set and <strong>0.54</strong> accuracy score for the testing data set. As can be seen, there is a overfitting in the corresponding model. Using an accuracy score of 0.54 is also not that bad compared to random sampling of the resilts which have a assymptotic accuracy of 0.33.
</p>
<p> I repeated the above-mentioned classification modeling. In this time, I added the name of countries into my predictions. This is revealed that the accuracy score for the test data is less (i.e., <strong>0.44</strong>) in this situation.</p>
<h2>The results of modeling</h2>
<p> The results for the final model and final predictions are shown as follows. The following results are only for two groups. The full results can be found 
 <a href="https://github.com/kaveh7293/World-Cup-Results-Prediction--Accuracy-of-Common-Sense-/blob/main/final_results.xlsx">here </a> . Note that, I reported the probabilities rather than the predicted classes, because I found it more interesting to report the probabilities especially because in the previous world-cups there have been some interesting results (e.g., Mexico and Korea won Germany) which could be explained by the probabilistic nature of the soccer matchs.<br><br>
<img src='https://github.com/kaveh7293/World-Cup-Results-Prediction--Accuracy-of-Common-Sense-/blob/main/Screenshot%202022-07-17%20191646.png' width="650" height="400"><br>


<p> The code for all of above analysis can be found <a href='https://github.com/kaveh7293/World-Cup-Results-Prediction--Accuracy-of-Common-Sense-/blob/main/World_Cup.ipynb'> here.</a>

</p>
