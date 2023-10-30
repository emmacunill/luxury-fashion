import pandas as pd
import os
import numpy as np
import re
from collections import Counter
import matplotlib.pyplot as plt 
import seaborn as sb
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests 


df_1 = pd.read_csv("data/Dataset Global Fashion Brands Brand Equity Ranking Growth Rate  COO ROO 2001-2021.csv")

df_2= pd.read_csv("data/LuxFashion-Q42019.csv")

url = 'https://fashionunited.com/i/top200'

def download_html(url):

    ''' Function to get html content from a web with bs4. '''

    res = requests.get(url, timeout=5)
    html = res.content
    return BeautifulSoup(html, 'html.parser')

soup = download_html(url)

def get_table_web(soup):

    '''Function to get a table and transform it into a dataframe from an already requested link.'''

    table =  soup.find("table")
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text for col in cols]
        data.append(cols)
    ds = pd.DataFrame(data, columns=['Index','Rank', 'Company', 'Mcap $', 'Type'])
    ds = ds.drop(['Index'], axis=1)
    return ds

df_3 = get_table_web(soup)

df_3.to_csv(f"data/100_fashion_money.csv")

url_2 = 'https://www.wallpaper.com/fashion-beauty/milan-fashion-week-aw-2023-highlights'

soup = download_html(url_2)

def titles_article(soup):

    ''' Function to get titles from an article body'''

    ds =  soup.find("div", {"id": "article-body"})
    titles = ds.find_all("h2")
    brands = [i.getText() for i in titles]
    return [i for i in brands if "Week" not in i]

MFW = titles_article(soup)

url_3 = "https://www.fhcm.paris/en/paris-fashion-week/calendar"
soup = download_html(url_3)

def brands_filtered(soup):

    ''' Get brands from containers in a calendar in html. '''

    ds =  soup.find_all("div", {"class": "cal-item shown"})
    a =[i.find("a") for i in ds]
    names = [i.find("h3") for i in a]
    return [i.getText().title() for i in names]

PFW = brands_filtered(soup)

url_4 = "https://www.vogue.com/fashion-shows"
soup = download_html(url_4)

def get_nav_brands(soup):

    ''' Function to get the brand names from a nav bar'''

    li = soup.find_all("li", {"class":"NavigationListItemWrapper-cxLZKD iAYgTw link--secondary navigation__list-item"})
    return [i.getText() for i in li]

NYFW = get_nav_brands(soup)

def merge_df(df_1,df_2,df_3,MFW,PFW,NYFW):

    ''' Function to encapsulate all the merging of the dataframes and columns to end up with 
    a final dataframe'''

    df_1.rename(columns = {'BrandName':'Brand'}, inplace = True)
    df_1.at[2, "Brand"] = "Hermes"
    df_3.rename(columns={"Company": "Brand"}, inplace=True)
    df_3.at[3, "Brand"] = "Hermes"
    merged_1 = pd.merge(df_1, df_2, on="Brand", how="right")
    merged_df = pd.merge(merged_1,df_3, on="Brand", how="left")
    merged_df["MFW"] = merged_df['Brand'].apply(lambda x: 'yes' if x in MFW else 'no')
    merged_df["PWF"] = merged_df['Brand'].apply(lambda x: 'yes' if x in PFW else 'no')
    merged_df["NYFF"] = merged_df['Brand'].apply(lambda x: 'yes' if x in NYFW else 'no')
    merged_df.to_csv(f"data/merged.csv")
    return merged_df

merged = merge_df(df_1,df_2,df_3,MFW,PFW,NYFW)




