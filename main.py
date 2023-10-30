import src.extraction as ext
import src.cleaning as clean
import src.visualizing as vis


#imports

import pandas as pd

#df + url

df_1 = pd.read_csv("data/Dataset Global Fashion Brands Brand Equity Ranking Growth Rate  COO ROO 2001-2021.csv")
df_2= pd.read_csv("data/LuxFashion-Q42019.csv")
df = pd.read_csv("data/merged.csv")
df_clean = pd.read_csv("data/Luxury_Fashion.csv")

url = 'https://fashionunited.com/i/top200'
url_2 = 'https://www.wallpaper.com/fashion-beauty/milan-fashion-week-aw-2023-highlights'
url_3 = "https://www.fhcm.paris/en/paris-fashion-week/calendar"
url_4 = "https://www.vogue.com/fashion-shows"

# extract

soup = ext.download_html(url)

df_3 = ext.get_table_web(soup)

soup = ext.download_html(url_2)

MFW = ext.titles_article(soup)

soup = ext.download_html(url_3)

PFW = ext.brands_filtered(soup)

soup = ext.download_html(url_4)

NYFW = ext.get_nav_brands(soup)

merged = ext.merge_df(df_1,df_2,df_3,MFW,PFW,NYFW)

# Cleaning functions

clean_df = clean.clean_dataset(df)

lf = clean.extract_clean(clean_df)


#Visualizing functions

vis.plot_top5(df_clean)

vis.plot_top10(df_clean)

vis.sentiment10(df_clean)

vis.webvisibility10(df_clean)

vis.runway10(df_clean)

vis.top2017(df_clean)

vis.equity2017(df_clean)

vis.top10tail(df_clean)