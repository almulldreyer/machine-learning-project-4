# Set up Dependencies
import pandas as pd
from bs4 import BeautifulSoup
import pymongo
import requests
from splinter import Browser
from flask_pymongo import PyMongo
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL for the NBA sities
    url = "https://www.teamrankings.com/nba/trends/win_trends/"
    url2 = "https://www.teamrankings.com/nba/trends/win_trends/?range=yearly_2020_2021"
    url3 = "https://www.teamrankings.com/nba/trends/win_trends/?range=yearly_2019_2020"
    url4 = "https://www.teamrankings.com/nba/trends/win_trends/?range=yearly_since_2018_2019"

    browser.visit(url)
    browser.visit(url2)
    browser.visit(url3)
    browser.visit(url4)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    nba_soup = BeautifulSoup(html, 'html.parser')

    # Per Game Stats, Total Stats, Team Complete
    stats_info = gambling_soup.find('div', class = 'content_title').text
    # news_title = mars_soup.find('div', class_='content_title').text

    # Paragraph/info on results
    stats_resultsinfo = gambling_soup.find('div', class_= 'article_teaser_body').text
    # news_p = mars_soup.find('div', class_='article_teaser_body').text

    # URL for the site
    featured_url = "https://www.teamrankings.com/nba/trends/win_trends/"
    browser.visit(featured_url)

    time.sleep(1)

    # Create BeautifulSoup object; parse with 'html.parser'

    featured_html = browser.html
    featured_soup = BeautifulSoup(featured_html, 'html.parser')

    # 
    featured_image = featured_soup.find_all(
        'img', class_='headerimage fade-in')[0]["src"]

    # Image URL to be printed

    featured_image_url = featured_url + featured_image

    # URL for team facts?
    ATL22 = "https://www.basketball-reference.com/teams/2022.html"

    # Read in the html table
    table = pd.read_html(https://www.basketball-reference.com/teams/2022.html)

    # Set the column names and only display the values
    new_df = table[1]
    new_df.columns = ["Per Game Stats" , "Total Stats" , "Team Complete""]
    new_df.set_index("Description", inplace=True)

    # Save file as HTML table
    info_df = new_df.to_html(border="1", justify="left")

    info_df.replace('\n', '')

    for team in teams:
       # img_title = individual.find('h3').text
       #  img_title = img_title.replace("Enhanced", "")

        #image_url = individual.find('img', class_='thumb')['src']
       # image_src = hemisphere_url + image_url
    # Define the hemispehere dictionary and set the values
        #hemisphere_dict = {}
        #hemisphere_dict["title"] = img_title
        #hemisphere_dict["img_src"] = image_src

        #images_titles.append(hemisphere_dict)
# Define a dictionary that will hold all the data from info above
    total_dict = {
        "Per Game Stats": stats_info,
        "Total Stats": stats_resultsinfo,
        "Team Complete": 
    }

# Quit the browser after scraping
    browser.quit()
    

# Return results
    return total_dict