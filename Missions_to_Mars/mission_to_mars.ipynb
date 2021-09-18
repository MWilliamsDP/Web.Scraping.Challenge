{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ea307ea5-552f-45a4-aaa5-61f2136766bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Dependencies\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pymongo\n",
    "from splinter import Browser\n",
    "from flask import Flask, render_template, redirect\n",
    "import pandas as pd\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9f64c03e-b92f-49d1-adb4-fdc8f5d2d612",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 93.0.4577\n",
      "Get LATEST driver version for 93.0.4577\n",
      "Driver [C:\\Users\\MW\\.wdm\\drivers\\chromedriver\\win32\\93.0.4577.63\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "#Set path and initialize Chrome\n",
    "executable_path = {\"executable_path\": ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dd654025-badf-467b-86c8-2a40459fb01e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#MARS NEWS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8af278cb-8050-4537-abe6-24d008c4b42c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set News URL and scraping\n",
    "url = 'https:redplanetscience.com'\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "news = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a92f66af-5c2c-4fd3-958a-820255c0b38d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set variable to pull first headline and teaser paragraph, \n",
    "news_title = news.find_all('div', class_='content_title')[0].text\n",
    "news_p = news.find_all('div', class_='article_teaser_body')[0].text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c83c1fc9-8003-43bf-91ed-8759d2424876",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's InSight Flexes Its Arm While Its 'Mole' Hits Pause\n",
      "Now that the lander's robotic arm has helped the mole get underground, it will resume science activities that have been on hold.\n"
     ]
    }
   ],
   "source": [
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7c1c5e46-06c0-4fe5-9e3d-12d4197f1d17",
   "metadata": {},
   "outputs": [],
   "source": [
    "#MARS IMAGE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d722c887-2ced-4efc-b871-88eb925102ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Set Photo URL and scraping\n",
    "url2 = 'https://spaceimages-mars.com/'\n",
    "browser.visit(url2)\n",
    "html_photo = browser.html\n",
    "news_photo = bs(html_photo, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cd79a757-a2f8-4d7f-ba14-48dfc39d0e75",
   "metadata": {},
   "outputs": [],
   "source": [
    "image_url=news_photo.find('img', class_='headerimage fade-in')['src']\n",
    "image_url=url2 + image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9d4d11d1-90ca-49ff-aec3-fa355cec51ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://spaceimages-mars.com/image/featured/mars3.jpg\n"
     ]
    }
   ],
   "source": [
    "print(image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b59913cf-02f7-4a19-86c9-a497f34bfff9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#MARS FACTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a7b04152-467a-4b3e-af7d-4c6c752ef09a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                         0                1                2\n",
       " 0  Mars - Earth Comparison             Mars            Earth\n",
       " 1                Diameter:         6,779 km        12,742 km\n",
       " 2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 3                   Moons:                2                1\n",
       " 4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 5          Length of Year:   687 Earth days      365.24 days\n",
       " 6             Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:          2 ( Phobos & Deimos )\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#READ table from URL\n",
    "url_facts='https://galaxyfacts-mars.com'\n",
    "facts=pd.read_html(url_facts)\n",
    "type(facts)\n",
    "facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "96059485-8d39-4a50-80cb-c213f08bc856",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Convert to dataframe\n",
    "factsDF = facts [0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "373559ac-ca8f-4f5b-9c69-723dbb37ea5c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type (factsDF)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "adda4b1f-b57e-4190-8bd4-32ce13e44df7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Convert to html\n",
    "facts_html=factsDF.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1ed7b37a-2a9f-4685-963f-9605c6a5d911",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>0</th>\\n      <th>1</th>\\n      <th>2</th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>0</th>\\n      <td>Mars - Earth Comparison</td>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>1</th>\\n      <td>Diameter:</td>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>2</th>\\n      <td>Mass:</td>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>3</th>\\n      <td>Moons:</td>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>4</th>\\n      <td>Distance from Sun:</td>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>5</th>\\n      <td>Length of Year:</td>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>6</th>\\n      <td>Temperature:</td>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#check\n",
    "facts_html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "87227f62-f08c-4599-8397-dfea57b99728",
   "metadata": {},
   "outputs": [],
   "source": [
    "#MARS HEMISPHERES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "46dd07e1-e038-471f-a07f-10ecbac6451e",
   "metadata": {},
   "outputs": [],
   "source": [
    "H_url = 'https://marshemispheres.com/'\n",
    "browser.visit(H_url)\n",
    "H_html = browser.html\n",
    "H_soup = bs(H_html, 'html.parser')\n",
    "images=H_soup.find_all('div', class_='item')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "806ad3ee-289a-499d-beb4-5c280c3859d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "image_urls=[]\n",
    "for h in images:\n",
    "    H_title = h.find('h3').text\n",
    "    img_url = h.find('div', class_='wide-image')\n",
    "    image_urls.append({'Title':H_title, 'Image URL': img_url})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a174bd1b-3b5e-49d5-bba2-615d0e43472f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'Title': 'Cerberus Hemisphere Enhanced', 'Image URL': None}, {'Title': 'Schiaparelli Hemisphere Enhanced', 'Image URL': None}, {'Title': 'Syrtis Major Hemisphere Enhanced', 'Image URL': None}, {'Title': 'Valles Marineris Hemisphere Enhanced', 'Image URL': None}]\n"
     ]
    }
   ],
   "source": [
    "print (image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c223329-74f5-4113-b061-f947e4d1ef5d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4d02d220-4909-44d7-8454-1ec08363d001",
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
