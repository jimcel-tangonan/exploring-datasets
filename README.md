
## Repository of Projects

A compilation of examples showcasing the projects I've done using machine learning algorithms and data analysis.

#### 1. Selenium Webdriver - Instagram Automation
A python script to automate Instagram actions (i.e. commenting, liking, following) on user profiles with the goal of building influence. 

##### Script functions at ~125 profiles per 25 mins. 
  - Ignores all profiles that are private-users/having less than 25 posts/has non-english text; additionally, must have a         followers/following ratio of 0.1 - 100 to determine the profile status as influencer/microinfluencer/regular or spam.
  - Captures and stores IG username and other attributes for ML analysis.
  - Determines if photo has been previously liked and if able, leaves a like or comment.
  - When all criteria are met, the profile is followed; otherwise, it is ignored.

[link to script](_automate-instagram-actions)



#### 2. Brain weight(grams) and head size(cubic cm)
Source: R.J. Gladstone (1905). "A Study of the Relations of the Brain to to the Size of the Head". 
  - Description: Brain weight (grams) and head size (cubic cm) for 237 adults classified by gender and age group.
  
Visualizing how the preprocessing method `standardscaler`, when applied to the data, would benefit the linear_model algorithm. 

![Alt text](screenshot/standardscaler.png?raw=true "standardscaler.png")
---

Scaling and normalizing allowed the LinearRegression model to fit in such as way that when predicting, previously not explaining any deviations, to now explaining 68% of the variance. 


|               | MSE           | R-squared      |
| ------------- |:-------------:| :-------------:|
| StandardScaler| 0.3231        | 0.6805         |
| Unprocessed   | 1.983e+06     | -135.4         |

---


  
[link to notebook](_analysis-algorithms/preprocessing.ipynb)
