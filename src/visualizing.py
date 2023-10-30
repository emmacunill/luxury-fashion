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


def plot_top5 (df):

   ''' Function to get plot top 5 ranked brands 2023'''

   top_5_brands = df.sort_values(by="Rank2023", ascending=False).head(5)
   sb.barplot(x = top_5_brands["Brand"], y = top_5_brands["Rank2023"], palette="BrBG").set(title='5 Top ranked Brands 2023')
   sb.set(font_scale=1.0)
   plt.xticks(rotation=45)
   plt.xlabel('Rank')
   for index, row in top_5_brands.iterrows():
      plt.text(index, row["Rank2023"] + 4, str(row["Rank2023"]), ha='center')
   plt.savefig(f"figures/rank_5.png", bbox_inches = "tight")
   

def plot_top10 (df):

   ''' Function to get plot top 10 ranked brands 2023'''

   top_10_brands = df.sort_values(by="Rank2023", ascending=False).head(10)
   sb.barplot(x = top_10_brands["Brand"], y = top_10_brands["Rank2023"], palette="BrBG").set(title='10 Top ranked Brands 2023')
   sb.set(font_scale=0.7)
   plt.xticks(rotation=45)
   plt.xlabel('Rank')
   for index, row in top_10_brands.iterrows():
      plt.text(index, row["Rank2023"] + 4, str(row["Rank2023"]), ha='center')
   plt.savefig(f"figures/rank_10.png", bbox_inches = "tight")
   



def sentiment10 (df):

   ''' Function to get plot sentiment top 10 ranked brands 2023'''

   top_10_brands = df.sort_values(by="Rank2023", ascending=False).head(10)
   sb.barplot(x = top_10_brands["Brand"], y = top_10_brands["Sentiment2023"], palette="bone").set(title='Sentiment Top 10 Brands')
   sb.set(font_scale=0.7)
   plt.xticks(rotation=45)
   plt.xlabel('Sentiment')
   for index, row in top_10_brands.iterrows():
      plt.text(index, row["Sentiment2023"] + 4, str(row["Sentiment2023"]), ha='center')
   plt.savefig(f"figures/sentiment_10.png", bbox_inches = "tight")
   


def webvisibility10 (df):

   ''' Function to get plot web visibility top 10 ranked brands 2023'''

   top_10_brands = df.sort_values(by="Rank2023", ascending=False).head(10)
   sb.barplot(x = top_10_brands["Brand"], y = top_10_brands["WebVisibility2023"], palette="copper").set(title='Web Visibility Top 10 Brands')
   sb.set(font_scale=0.7)
   plt.xticks(rotation=45)
   plt.xlabel('Web Visibility')
   for index, row in top_10_brands.iterrows():
      plt.text(index, row["WebVisibility2023"] + 4, str(row["WebVisibility2023"]), ha='center')
   plt.savefig(f"figures/web_visibility_10.png", bbox_inches = "tight")
   



def runway10 (df):

    ''' Function to get plot participation fashion weeks top 10 ranked brands 2023'''

    sb.set(rc={"figure.figsize": (8, 6)})
    top_10_brands = df.sort_values(by="Rank2023", ascending=False).head(10)
    visibility = top_10_brands[(top_10_brands["MFW2023"] == "yes") | (top_10_brands["PFW2023"] == "yes") | (top_10_brands["NYFW2023"] == "yes")]
    vis =visibility.melt(id_vars='Brand', var_name='FashionWeek', value_name='Participation')
    participating_brands = vis[vis['Participation'] == 'yes']
    sb.catplot(data=participating_brands, x="Brand", y="FashionWeek", kind="swarm", color="orange").set(title="Participating Brands in Fashion Weeks")
    sb.set(font_scale=1.2)
    plt.xticks(rotation=90)
    plt.savefig(f"figures/runway_10.png", bbox_inches = "tight")
   


def top2017(df):

    ''' Function to get plot rank evolution top 5'''

    top_5_2017 = df.sort_values(by='Rank2017', ascending=False).head(5)
    x_values = top_5_2017[["Rank2017", "Rank2018", "Rank2019", "Rank2020", "Rank2021"]]
    df_long = pd.melt(top_5_2017, id_vars='Brand', var_name='Year', value_name='Rank', value_vars=x_values)
    sb.lineplot(data=df_long, x='Year', hue='Brand', y='Rank', palette='Set1').set(title='Rank Evolution')
    plt.subplots_adjust(top=0.85)
    sb.set(font_scale=0.7)
    plt.savefig(f"figures/top_2017.png", bbox_inches = "tight")
   


def equity2017(df):

    ''' Function to get plot equity evolution top 5'''

    eq_2017 = df.sort_values(by='Equity2017', ascending=False).head(5)
    x_values = eq_2017[["Equity2017", "Equity2018", "Equity2019", "Equity2020", "Equity2021"]]
    df_long = pd.melt(eq_2017, id_vars='Brand', var_name='Year', value_name='Equity', value_vars=x_values)
    sb.lineplot(data=df_long, x='Year', hue='Brand', y='Equity', palette='Set1').set(title='Equity Evolution')
    plt.subplots_adjust(top=0.85)
    sb.set(font_scale=0.7)
    plt.savefig(f"figures/eq_2017.png", bbox_inches = "tight")
   



def top10tail(df):

    ''' Function to get plot of the participation of the 10 lower ranked brands'''

    sb.set(rc={"figure.figsize": (8, 6)})
    eq_2017 = df.sort_values(by='Rank2023', ascending=True).head(17)
    vis =eq_2017.melt(id_vars='Brand', var_name='FashionWeek', value_name='Participation')
    participating_brands = vis[vis['Participation'] == 'yes']
    sb.catplot(data=participating_brands, x="Brand", y="FashionWeek", kind="swarm", color="sienna").set(title="Lower ranked Brands in Fashion Weeks")
    sb.set(font_scale=1.2)
    plt.xticks(rotation=90)
    plt.savefig(f"figures/runway_10_tail.png", bbox_inches = "tight")
    
