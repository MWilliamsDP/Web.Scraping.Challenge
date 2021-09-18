from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.facts.df
collection = db.mars 


executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https:redplanetscience.com'
browser.visit(url)

time.sleep(1)

def scrape():
    html = browser.html
    news = bs(html, 'html.parser')
    #Set variable to pull first headline and teaser paragraph, 
    news_title = news.find_all('div', class_='content_title')[0].text
    news_p = news.find_all('div', class_='article_teaser_body')[0].text

    #Set Photo URL and scraping
    url2 = 'https://spaceimages-mars.com/'
    browser.visit(url2)
    html_photo = browser.html
    news_photo = bs(html_photo, 'html.parser')



    image_url=news_photo.find('img', class_='headerimage fade-in')['src']
    image_url=url2 + image_url

    #READ table from URL
    url_facts='https://galaxyfacts-mars.com'
    facts=pd.read_html(url_facts)
    type(facts)
    facts

    #Convert to dataframe
    factsDF = facts [0]

    #Convert to html
    facts_html=factsDF.to_html()

    #MARS HEMISPHERES

    H_url = 'https://marshemispheres.com/'
    browser.visit(H_url)
    H_html = browser.html
    H_soup = bs(H_html, 'html.parser')
    images=H_soup.find_all('div', class_='item')

    image_urls=[]
    for h in images:
        H_title = h.find('h3').text
        img_url = h.find('div', class_='wide-image')
        image_urls.append({'Title':H_title, 'Image URL': img_url})

