# Retail Luxury Fashion - Data Analysis


## Overview
This data project focuses on Luxury Fashion Retail brands, providing valuable insights and analysis of the top brands in the industry. The project includes data related to brand rankings, market performance, customer sentiment, and more. It aims to offer a comprehensive understanding of the Luxury Fashion Retail landscape.

## Data sources

- Base dataset - [Kaggle](https://www.kaggle.com)
- Web scraping 


## Workflow

1. Identify a dataset of interest, from a publlic source.

2. Collection of additional data:


    Once the main dataset was identified, the project moved on to the enhancement phase by collecting additional data. This was achieved using web scraping techniques to extract information from websites.

3. Cleaning and tranforming the data:

    This included removing outliers, standardizing formats, and resolving any data inconsistencies.

4. EDA: 

    Exploratory Data Analysis, to better comprehend the correlation within the dataset.

5. Visualization:

    Generating graphs, charts, and plots that effectively represented the findings from the exploratory data analysis. These visualizations help communicate the results clearly.

## Hypothesis

1. The Luxury Fashion industry is evolving "The classics either modernize or dacay, and so it demostrates in their actual rankings.

2. What factors are involved in achieving a higher ranking position?

3. In our actual times Fashion runways are less of a necessity for exposure but a lifestyle event. 

## Analysis


From 3 different datasets, and 3 lists. Created the final dataset on which to work.

Composition of the final dataset:

- 27 Rows, 29 columns.
- Information in the columns:
    Name of the Brand, Rankings, Equity, Web Visibility, Sentiment (Popularity), Market  Capitalize and participation in the NYFW, MFW, PFW

On a first glance we can already see some changed in the values over the years.

Let's get more into detail on the results of the data.


## Results

1. Top 5 brands in 2023.

![image](https://github.com/emmacunill/luxury-fashion/blob/main/figures/rank_5.png?raw=true)

    ''' Why is Dior not in here? And Prada? What's going on? What's happenin'? '''
    
Let's see the Top 10

![image](https://github.com/emmacunill/luxury-fashion/blob/main/figures/rank_10.png?raw=true)



2. Why are they organized like in stairs? Does it have to do with the sentiment?

![image](https://github.com/emmacunill/luxury-fashion/blob/main/figures/sentiment_10.png?raw=true)

Apparently the only one that would make sense is Hermes, the rest of them doesn't seem to be that influenced by the Sentiment.

Maybe it has to do with visibility either on the web or runways.

Let's see: 

    - Web visibility

![image](https://github.com/emmacunill/luxury-fashion/blob/main/figures/web_visibility_10.png?raw=true)


    - Runway visibility

![image](https://github.com/emmacunill/luxury-fashion/blob/main/figures/runway_10.png?raw=true)

A we can see from the plots, It may have something to do with a mix of the visibility and the Sentiment. For example, Hermes is the most liked brand, and because of that he does'nt need the visibility to be that high. So web visibility is 60 and they only went to Paris Fashion Week. 

But Luis Vuitton as his Sentiment is not that high, they tried to compensate by going to 2 Fashion Weeks as a strategy to augment visibility and thus the sentiment.


3. Has it always been like this?


![image](https://github.com/emmacunill/luxury-fashion/blob/main/figures/top_2017.png?raw=true)

As we can see in the plot in the previous years the ranks were quite different. For starters, Hermes was thelower one from the top 5. We can also see the start of the decadency of Dior, from that graphic we could predict the position in the rank he's in 2023.


4. Does the equity get affected by the rank?

![image](https://github.com/emmacunill/luxury-fashion/blob/main/figures/eq_2017.png?raw=true)

We can see that obviously Equity doesn't get affected by rank. Maybe it has something to do with the way the company workaraounds is built. But what we can assume for sure is that there are some companies more rentable than others as they are less depending on the rank or the sentiment. For example Luis Vuitton. It's not even in the top 5 rank from 2017 to 2021 an it's the one with more equity.

5. Do the lower ranked brands try to gain visibility and position by participating in runways?

![image](https://github.com/emmacunill/luxury-fashion/blob/main/figures/runway_10_tail.png?raw=true)

We can see that all of them participate in at least 1 show. But only a few participate in more than one. That could be because of many factors, maybe they can't access to the big runaways shows, although what makes more sense is that they just don't participates. As in all Fashion weeks, those luxury brands have already a presaved spot.



## Conlusions 

As we see in the data, evolution stops for no one. While there are some brands that kept track of innovation and thus uppered their rank, there are other brands for example Dior, that decided to stay with the classics, and even though their decacy it's not super noticable it still follows a descending pattern. 

An that is mostly because of the focuse each brand gives to visibility, user popularity, and introducing and adapting the brand strategies with the new technologies.

We also can prove that Runways nowadays are ysed as a lifestyle event and are not a necessity to gain visibility or popularity. As if they were, the lower ranked brands would be participating in the maximum number possible of shows. And our data shows otherwise.


## Links of interest

[Brand Watch Index]("https://www.brandwatch.com/wp-content/uploads/2020/01/LuxFashion-Q42019.csv?rev=1698422964802")

[Fashion United]("https://fashionunited.com/i/top200")

[Canva Presentation]("https://www.canva.com/design/DAFywJ8Gbjo/z30AT2x216v3prputMbcuw/edit?utm_content=DAFywJ8Gbjo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
