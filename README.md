# NBA Betting AI - Project 4
We chose to analyze and model NBA stat and team data  from 1980 to 2022, to predict which NBA teams would win in the 2022 season. 

## Table of Contents
* [Technologies](#Technologies-Used) 
* [Process](#Process)
  * [Data Scraping](#Data-Scraping-and-Cleaning)
  * [Modeling Data](#Modeling-the-Data-with-ML)
  * [Data Visualizations](#Creating-Data-Visualizations)
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
image of our scrape data

### Modeling the Data with ML
For data modeling we ran our datasets through a RandomForestRegressor using SciKit-Learn with Win/Loss% as our target.

### Creating Data Visualizations
Data visualizations were created via Matplotlib, which shows our calculated prediction lines and actual data lines for win/loss%.

## Conclusion
Sports betting is a highly competitive field with lots of large companies competing for information, which means there's alot of information witheld from the general public (knowledge is money). Due to that unfortunately there was a lack of data to make concrete and strongly accurate models. Along with that there is a large human element in sports making predicting things very difficult. Despite that we were able to predict with some accuracy that the Los Angeles Lakers and Toronto Raptors have the highest Win/Loss%.
