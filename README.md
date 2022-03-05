# NBA Betting AI - Project 4
We chose to analyze and model the stat and team data provided from http://basketball-reference.com starting from 1980 to 2022, to predict which NBA teams would win in the 2022 season. 

## Table of Contents
* [Technologies](#Technologies-Used) 
* [Process](#Process)
  * [Data Scraping](#Data-Scraping-and-Cleaning)
  * [Modeling Data](#Modeling-the-Data-with-ML)
  * [Data Visualizations](#Creating-Data-Visualizations)
* [Limitations](#Limitations)
* [Conclusion](#Conclusion)

## Technologies Used
* Python3 (pandas, BeautifulSoup, and Matplotlib)
* Jupyter Notebook
* SciKit-Learn
* HTML5/CSS3
* Visual Studio Code

## Process
### Data Scraping and Cleaning
We scraped all of our NBA team stats data from http://basketball-reference.com, using Pythons pandas library, BeautifulSoup, and Jupyter Notebook. From there we used a series of loops to scrape, clean, and store the data into a list.
image of our scrape data.

### Modeling the Data with ML
For data modeling we ran our datasets through a RandomForestRegressor using SciKit-Learn with Win/Loss% as our target.

##Linear Regression
We wanted to try another model using Linear regression to assist with the team predictions by using Total Points for the season as our target.

### Creating Data Visualizations
Data visualizations were created via Matplotlib, which shows our calculated prediction lines and actual data lines for win/loss%.

## Limitations


## Conclusion
