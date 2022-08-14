<h2> Overview of the Project</h2>
<ul>
<li>The data from the group stages of previous world cups between 1998 to 2018 were collected so that I can train a model from which the results of group stage world cup in 2022 can be predicted. The csv file for the data can be found <a href='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/WorldCup.csv'>here. </a></li>
<li> A multi-class classfication model is fitted and used to predict wehther the first team wins, the teams draw or the second team wins.</li>
<li> The features which are used for this classfiction problem are the name of the countries, the teams continent, fifa ranking, the number of previous world champtionships, and wehther they were the host.</li>
<li>I first did some explanatory data analysis to answer some of the questions I had in my mind about the previous world cup. Then, I did some feature selection analysis to determine important features need to be selected for model training. Finally, I trained a random forest model to predict the results of the next world-cup in 2022.</li>
 </ul>

<h2> Explanatory Data Analysis</h2>
<h3> Determination of the Hardest Groups and the Easiest Groups in the Previous World-cups</h3> 
<p>What were the hardest groups in the group stage in each of the previous world cups. I chose the hardest group based on the smallest average of the fifa world    ranking in each group. We plot a barplot to return the average of the teams rankings in each of the world cups:<br>
  <img src='https://github.com/kaveh7293/World-Cup-Results-Prediction--Accuracy-of-Common-Sense-/blob/main/d1.png'><br>
</p>
   
<p>The groups with the lowest average ranking are the hardest (death groups) and the groups with the maximum ranking are the easiest. We also determined this using python code.</p> 
<p> The following results were obtained by our python code and can be seen from barplots as well. The hardest group in the previous world-cups were: 

 <table>
  <tr>
    <th>World Cup</th>
    <th>Group</th>
    <th>Teams</th>
  

  </tr>
  <tr>
    <td>1998</td>
    <td>H</td>
    <td> Japan, Argentina, Croatia, and Jamaica</td>
  </tr>
  <tr>
    <td>2002</td>
    <td>F</td>
    <td>Argentina, England, Nigeria, and Sweden</td>
  </tr> 
  <tr>
    <td>2006</td>
    <td>E</td>
    <td>Italy, Ghana, Czechia, and USA</td>
  </tr>
    <tr>
    <td>2010</td>
    <td>D</td>
    <td>Germany, Australia, Ghana, and Serbia</td>
  </tr>
  
  <tr>
    <td>2014</td>
    <td>D</td>
    <td>Uruguay, Costa_Rica, Italy, and England</td>
  </tr>
<tr>
 <td>2018</td>
 <td>E</td>
  <td>Brazil, Costa_Rica, Serbia, and Switzerland</td>
  </tr>
</table> 

</p>
<p>The easiest groups are:
 
  <table>
  <tr>
    <th>World Cup</th>
    <th>Group</th>
    <th>Teams</th>
  

  </tr>
  <tr>
    <td>1998</td>
    <td>D</td>
    <td>Spain, Paraguay, Bulgaria, and Nigeria</td>
  </tr>
  <tr>
    <td>2002</td>
    <td>H</td>
    <td> Japan, Belgium, Tunisia, and Russia</td>
  </tr> 
  <tr>
    <td>2006</td>
    <td>G</td>
    <td>Switzerland, South_Korea, France, and Togo</td>
  </tr>
    <tr>
    <td>2010</td>
    <td>F</td>
    <td>Italy, Paraguay, New_Zealand, and Slovakia</td>
  </tr>
  
  <tr>
    <td>2014</td>
    <td>F</td>
    <td>Argentina, Bosnia, Iran,and Nigeria</td>
  </tr>
<tr>
 <td>2018</td>
 <td>A</td>
  <td>Uruguay, Russia, Saudi_Arabia, and Egypt</td>
</tr>
</table> <br>
          
The code for the above results can be found [here](https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Difficulty_Level.py)

<p>some additional information can be interpreted from above plots are:
 <ol>
  <li>the error bars show the standard deviations of the fifa world rankings of the teams in each group. The smaller standard deviations means that the teams performance from which the fifa world ranking has been obtained were relatively similar. However, the larger standard deviations shows that the teams level are more different and probably there was not a severe competition between the teams for qualifying into knock out stage</li>
 <li>The height of the barplots for each group can be used to evaluated whether the fifa world ranking is fair because only 32 teams are qualified into the world cup. As shown, in most of the cases, the average of the rankings are arround 15 to 50. The groups whose average rankings are over 30 probably contain teams which are either the host (so they do not need to compete for qualification) or their fifa world ranking is well-determined. Another reason could be infair contribution of different continents. For example, in 2006 world cup none of the 4 Asian teams were qualified into the next stage.</li>
<li> To have groups with similar level of difficulties, fifa divided teams into four different categorizes. In each group, there are only one team from each category. The uniform height of the bar plots at each year can show the same level of difficulties for that world cup.</li>
   </p>

<h3> Performance of Different Countries and Continents in the Previous World-cups. </h3>
<p>In the following we show the number of wins, loses and draws for the teams from different continents. Teams from Europe and South America have the highest ratio of win/lose and win/draw compared to countries from different continents. This justify the lower number of teams from Asia and Africa in the world cup. In the following we investigate whether there is an improve in the performance of the countries from Asia, Africa and Concacaf regions. FIFA usually plans to improce the performance of the countries from these regions to make the World Cup more exciting.This is the countplot for the performance of different continents in the world cups:</p>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Continents_Performances.png' height='300' width='300'><br>


<p>As shown, only the countries from Europe and South America have more wins than draws and loses. In the following the plot of average points per game for countries from different continents are shown for different world cup years:</p><br>

<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Africa.png'><br>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Concacaf.png'><br>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Europe.png'><br>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/Oceania.png'><br>
<img src='https://github.com/kaveh7293/Kaveh-Portfolio/blob/main/South_America.png'><br>

<p>The plot shows that African countries performances get worse after world cup 1998. Asian countries performance is better in 2002, 2010 and 2018 world cups compared to their performance in 2006 and 20014. The best performace of Asian countries is in world cup 2002 when Japan and Korea were the hosts. South American counteries performance was very bad in 2002 with an average of about 0.6 points per game (Uruguay and Argentina were eliminated in the group stage). 
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

<img src='https://github.com/kaveh7293/World-Cup-Results-Prediction--Accuracy-of-Common-Sense-/blob/main/download.png'><br>
The results showed that only 43 features were important and the rest of features have small correlation (i.e., below 0.1) with the dependent variables.</p>
 <h5> disadvantage</h5>
 <p> Disadvantage of all the wrapper-based methods is that they do not account for correlation between features. As a result, two correlated features might be selected because their influence on the outputs are large.
 <p>
<h4> Feature selection using a wrapper-based method</h4>
 <p> This method uses a classfication model to evaluate whether containing a feature during classification have important effects on the quality of the prediction.  By doing so, the modeler can decide to chosse the optimal number of parameters. I used from feature-selection module in sklearn. I chose the first 50 features that have been ranked first by the model. The advantage of this method is that it accounts for correlation between the features </li>

 
 




<h2> Using a Model for Classification </h2>
<p> In this section, I used two models to predict the results of the games in the previous wrold cups and then use the trained model to predict the results of world cup 2022 in Qatar.  I used random forrest method and XGboost for classfication modeling. I used a randomized search method to obtain the optimal hyperparameters for these models. Finally, I tested the optimal model on the test dataset to evaulate which of these two models are the best. Note that, I used the test data to evaluate whether overfitting occurs or not. After making sure that there is no overfitting, I used the best model and fitted the whole data (including training and test data) with the same hyperparameters so that overfitting does not occur. The result of prediction quality are shown in the following table. As can be seen both methods have the same accuracy when they are used for test data set. However, the accuracy of the results for the training data shows that the random forest is overfitting the training data. As such, I used the XGboost and fit the whole data onto that.<br>



 <table>
  <tr>
    <th>Model</th>
    <th>Training Data Prediction Accuracy</th>
    <th>Test Data Prediction Accuracy</th>
  

  </tr>
  <tr>
    <td><strong>XGboost</strong></td>
    <td>0.49</td>
    <td>0.51</td>
  </tr>
  <tr>
    <td>Random Forest</td>
    <td>0.87</td>
    <td>0.51</td>
  </tr> </table>
<br>
 
</p>


<p> The results for the final model and final predictions are shown as follows. The following results are only for the first group. The full results can be found 
 <a href="https://github.com/kaveh7293/World-Cup-Results-Prediction--Accuracy-of-Common-Sense-/blob/main/final_results.xlsx">here </a> . Note that, I reported the probabilities rather than the predicted classes, because I found it more interesting to report the probabilities especially because in the previous world-cups there have been some interesting results (e.g., Mexico and Korea won Germany) which could be explained by the probabilistic nature of the soccer matchs.<br><br>
<table>
  <tr>
    <th>Team1</th>
    <th>Team2</th>
    <th>Probability (%) that Team1 will win </th>
    <th>Probability (%) that Team2 will win </th>
    <th>Probability (%) that Team1 and Team2 draw </th>


  </tr>
  <tr>
    <td>Qatar</td>
    <td>Equador</td>
    <td>33</td>
    <td>25</td>
    <td>42</td>

 </tr>
 <tr>
    <td>Qatar</td>
    <td>Senegal</td>
    <td>46</td>
    <td>36</td>
    <td>18</td>

 </tr>
 
 <tr>
    <td>Qatar</td>
    <td>Netherlands</td>
    <td>46</td>
    <td>36</td>
    <td>17</td>

 </tr>
 
 <tr>
    <td>Equador</td>
    <td>Senegal</td>
    <td>25</td>
    <td>20</td>
    <td>55</td>

 </tr>
 
 <tr>
    <td>Equador</td>
    <td>Netherlands</td>
    <td>25</td>
    <td>20</td>
    <td>55</td>

 </tr>
 
 <tr>
    <td>Senegal</td>
    <td>Netherlands</td>
    <td>46</td>
    <td>36</td>
    <td>18</td>

 </tr>
  </tr> </table>

 

<p> The code for all of above analysis can be found <a href='https://github.com/kaveh7293/World-Cup-Results-Prediction--Accuracy-of-Common-Sense-/blob/main/World_Cup.ipynb'> here.</a>
 
 

</p>
