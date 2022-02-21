# Surfs_Up
## Overview
The objective of this project was to gain experience with more advanced data storage, retrieval, and display by utilizing sqlalchemy to interact with a sqlite database 
and creating an application in Python using Flask to display query results in a web page. In the challenge portion of this project, queries were used to obtain the temperature 
data for the months of June and December and summary statistics for that data was calculated for the purpose of deciding the year round viability of a surf and ice-cream shop
in Oahu. The Results and Summary sections of this project will center around the challenge data.
## Results
### Summary Statistics
[June Temp. Statistics](https://github.com/MDaily7/surfs_up/blob/main/Resources/June_Temperatures.PNG)  
[December Temp. Statistics](https://github.com/MDaily7/surfs_up/blob/main/Resources/December_Temperatures.PNG)
### Statistics Comparison
The following comparisons are displayed in the images provided above
* The minimum temperature is only eight degrees less in December at 56 degrees compared to the 64 degrees minimum in June.
* The average temperature in June, about 75 degrees, is only slightly higher than the average for December at 71 degrees. 
* The maximum temperatures are only seperated by two degrees with June having a max temp of 85 and December having a max temp of 83 degrees. 
## Summary
Based on what is seen in the Results section, the surf and ice-cream shop in Oahu seems viable year round. The differences in temperatures between the two months are relatively
minimal. Ice-cream sales may dip a bit on the coldest of December days, but the average temperature is still within the 70s and reasonable for ice-cream and surfing; the temperature data 
in June seems as favorable for both as might be expected for a summer month. Additional queries may lend more credit to the evaluation. For example, a [June Precipitation Query](https://github.com/MDaily7/surfs_up/blob/main/Resources/June_prcp_query.PNG)
and a [December Precipitation Query](https://github.com/MDaily7/surfs_up/blob/main/Resources/December_prcp_query.PNG) with the same summary statistics accompanying them may provide additional insight. Perhaps the temperatures for the months don't differ
too much and seem reasonable for ice-cream and surfing, but the amount of rain could be a deterrent. 
## Resources
* [sqlite database](https://github.com/MDaily7/surfs_up/blob/main/hawaii.sqlite)
* Anaconda 4.11.0
* Python 3.7.11
* [Resources Folder](https://github.com/MDaily7/surfs_up/tree/main/Resources) containing images used in Results and Summary
* [Challenge Jupyter Notebook](https://github.com/MDaily7/surfs_up/blob/main/SurfsUp_Challenge.ipynb)
* [Project Jupyter Notebook](https://github.com/MDaily7/surfs_up/blob/main/climate_analysis.ipynb)
* [Flask Application](https://github.com/MDaily7/surfs_up/blob/main/app.py) Python script with Flask application for displaying query results in a web page
