#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

#set up browser
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

#Set up scrape function
def scrape():
    browser = init_browser()
    statdata = {}
     
     # Make a list of all team names
    teams = ['ATL','BRK','BOS','CHO','CHI','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
    pergame = []
    totals = []

    #Add in url and run browser
    for team in teams:
        url = f'https://www.basketball-reference.com/teams/{team}/2022.html'
        browser.visit(url)
        html=browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        #find first table
        tables = pd.read_html(url)
        atltables = tables[1]

        #clean table
        atl = atltables.set_index("Rk")
        atl1 = atl.rename(columns={'Unnamed: 1':'Player'})
        atl2 = atl1.dropna(subset=['Player'])

        #convert to html format and append to list
        ATLtable = atl2.to_html()
        ATLt = ATLtable.replace('\n','')
        pergame.append(ATLt)
        print(f"Found: {team} Per Game Stats")

        #find second table 
        atltables2 = tables[2]

        #clean
        atl2 = atltables2.set_index("Rk")
        atl12 = atl2.rename(columns={'Unnamed: 1':'Player'})
        atl22 = atl12.dropna(subset=['Player'])

        #convert to html format and append to list
        ATLtable2 = atl22.to_html()
        ATLt2 = ATLtable2.replace('\n','')
        totals.append(ATLt2)
        
        print(f"Found: {team} Totals Stats")
        print(f"Team Complete")
        print("---------------------------------------------------")


    statdata[''] = news_p