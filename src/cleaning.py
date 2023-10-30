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


def clean_dataset (df):

    ''' Function containing all the first cleaning steps for this dataset.'''

    df.drop(columns=["Unnamed: 0"], inplace=True)
    dropping_rows = [24, 18, 12]
    df.drop(index=dropping_rows, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.drop(columns=["Rank2001", "Rank2002", "Rank2003", "Rank2004", "Rank2005", "Rank2006", "Rank2007", "Rank2008", "Rank2009", "Rank2010", "Rank2011", "Rank2012", "Rank2013", "Rank2014", "Rank2015", "Rank2016"], inplace=True)
    df.drop(columns=["Equity2001", "Equity2002", "Equity2003", "Equity2004", "Equity2005", "Equity2006", "Equity2007", "Equity2008", "Equity2009", "Equity2010", "Equity2011", "Equity2012", "Equity2013", "Equity2014", "Equity2015", "Equity2016"], inplace=True)
    df.drop(columns=["GrowthRate2001", "GrowthRate2002", "GrowthRate2003", "GrowthRate2004", "GrowthRate2005", "GrowthRate2006", "GrowthRate2007", "GrowthRate2008", "GrowthRate2009", "GrowthRate2010", "GrowthRate2011", "GrowthRate2012", "GrowthRate2013", "GrowthRate2014", "GrowthRate2015", "GrowthRate2016"], inplace=True)
    df.drop(columns=["Rank", "BrandSector", "BrandSubSector"], inplace=True)
    df.rename(columns={"Social Visibility": "SocialVisibility2023"}, inplace=True)
    df.rename(columns={"Web Visibility": "WebVisibility2023"}, inplace=True)
    df.rename(columns={"Sentiment": "Sentiment2023"}, inplace=True)
    df.rename(columns={"Growth": "Growth2023"}, inplace=True)
    df.rename(columns={"Search": "Search2023"}, inplace=True)
    df.rename(columns={"Total": "Rank2023"}, inplace=True)
    df.rename(columns={"Mcap $": "Mcap2023billions"}, inplace=True)
    df.rename(columns={"Type": "pub_priv"}, inplace=True)
    df.rename(columns={"MFW": "MFW2023"}, inplace=True)
    df.rename(columns={"PWF": "PFW2023"}, inplace=True)
    df.rename(columns={"NYFF": "NYFW2023"}, inplace=True)
    
    return df



def clean_cap(cap):

    ''' Function to extract digits and transform them to floats.'''

    p_match = re.search(r'\$?(\d+\.\d+)\s*b', str(cap))
    if p_match:
        digit = p_match.group(1)
        return float(digit)
    else:
        return 'unknown'
    
def extract_clean(clean_df):

    ''' Function to apply the regex function to the Market Capitalization and then save the final df to csv.'''

    clean_df["Mcap2023billions"] = clean_df["Mcap2023billions"].apply(clean_cap)
    clean_df.to_csv(f"data/Luxury_Fashion.csv", index=False)
    return clean_df
    


