#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests

import pandas as pd


# # 1) Write a python program to display all the header tags from wikipedia.org.

# In[2]:


page=requests.get('https://www.wikipedia.org')
page


# In[3]:


soup=BeautifulSoup(page.content)
soup


# In[4]:



headers=soup.find_all(['h1','h2','h3','h4','h5','h6'])
print('List of all headers tags:', *headers, sep='\n\n')
                                  


# # 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)  and make DataFrame
# 

# In[5]:


page=requests.get('https://www.imdb.com/list/ls091520106/')
page


# In[6]:


soup=BeautifulSoup(page.content)
soup


# In[7]:


name=[]
for i in soup.find_all('div',class_="lister-item mode-detail"):
    name.append(i.text.replace('\n',' '))
    
name     


# In[8]:


ratings=[]
for i in soup.find_all('div',class_="ipl-rating-widget"):
    ratings.append(i.text.replace('\n',' '))
    
ratings    


# In[9]:


yearofrelease=[]
for i in soup.find_all('span',class_="lister-item-year text-muted unbold"):
    yearofrelease.append(i.text)
    
yearofrelease 


# In[10]:


print(len(name),len(ratings),len(yearofrelease))


# In[11]:


import pandas as pd
df=pd.DataFrame({'Name of Movies':name, 'Rate':ratings, 'Year of Release':yearofrelease})
df


# # 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.
# 

# In[12]:


page=requests.get('https://www.imdb.com/list/ls009997493/')
page


# In[13]:


soup=BeautifulSoup(page.content)
soup


# In[14]:


name=[]
for i in soup.find_all('div', class_="lister-item-content"):
    name.append(i.text.replace('\n',' '))
    
name    


# In[15]:


rating=[]
for i in soup.find_all('div', class_="ipl-rating-star small"):
    rating.append(i.text.replace('\n',' '))
    
rating    


# In[16]:


year_of_release=[]
for i in soup.find_all('span', class_="lister-item-year text-muted unbold"):
    year_of_release.append(i.text)
    
year_of_release    


# In[17]:


print(len(name), len(rating), len(year_of_release))


# In[18]:


import pandas as pd
df=pd.DataFrame({'Name of Indian movies':name, 'Rate':rating, 'Year of Release':year_of_release})
df


# In[ ]:





# # Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) 
# from https://presidentofindia.nic.in/former-presidents.htm

# In[19]:


page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[20]:


soup=BeautifulSoup(page.content)
soup


# In[21]:


name=[]
for i in soup.find_all('div', class_="presidentListing"):
    name.append(i.text.replace('\n',' ').split('(')[0])
    
name    


# In[22]:


term_of_office=[]
for i in soup('div', class_="presidentListing"):
    term_of_office.append(i.text.replace('\n',' ').replace(':',' ').split('Term of Office')[1])
    
term_of_office    


# In[23]:


import pandas as pd
df=pd.DataFrame({'Name of Former President of India':name, 'Term of Office':term_of_office})
df


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[24]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[25]:


soup=BeautifulSoup(page.content)
soup


# In[26]:


namec=[]
for i in soup('span', class_="u-hide-phablet"):
    namec.append(i.text)
    
namec    


# In[27]:


match=[]
for i in soup('td', class_="table-body__cell u-center-text"):
    match.append(i.text.replace(',',''))
    
match
res=[i for j, i in enumerate(match) if j%2==0]
res


# In[28]:


points=[]
for i in soup.find_all('td', class_="table-body__cell u-center-text"):
    points.append(i.text)
    
points    

res2=[i for j, i in enumerate(points) if j%2!=0]
res2


# In[29]:


rating=[]
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
    
rating


# In[34]:


print(len(namec), len(res), len(res2), len(rating))


# In[ ]:





# b) Top 10 ODI Batsmen along with the records of their team and rating.

# In[35]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page


# In[36]:


soup=BeautifulSoup(page.content)
soup


# In[37]:


batsmen_name=[]
for i in soup.find_all('td', class_="table-body__cell name"):
    batsmen_name.append(i.text.replace('\n',''))
    
batsmen_name


# In[38]:


team=[]
for i in soup.find_all('span', class_="table-body__logo-text"):
    team.append(i.text)
    
team


# In[39]:


rating=[]
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
    
rating


# In[40]:


print(len(batsmen_name), len(team), len(rating))


# In[41]:


import pandas as pd
df=pd.DataFrame({'Batsmen Name':batsmen_name, 'Team':team, 'Rating':rating})
df


# In[42]:


df.head(10)


# c) Top 10 ODI bowlers along with the records of their team and rating.

# In[43]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
page


# In[44]:


soup=BeautifulSoup(page.content)
soup


# In[45]:


bowler_name=[]
for i in soup.find_all('td', class_="table-body__cell rankings-table__name name"):
    bowler_name.append(i.text.replace('\n',''))
    
bowler_name


# In[46]:


team=[]
for i in soup.find_all('span', class_="table-body__logo-text"):
    team.append(i.text)
    
team    


# In[47]:


rating=[]
for i in soup.find_all('td', class_="table-body__cell rating"):
    rating.append(i.text)
    
rating   


# In[48]:


df=pd.DataFrame({"Bowler's Name":bowler_name, 'Team':team, 'Rating':rating})
df


# In[49]:


df.head(10)


# # 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[50]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[51]:


soup=BeautifulSoup(page.content)
soup


# In[52]:


team_name=[]
for i in soup.find_all('span', class_="u-hide-phablet"):
    team_name.append(i.text)
    
team_name    


# In[61]:


matches=[]
for i in soup.find_all('td', class_="table-body__cell u-center-text"):
    matches.append(i.text.replace('\n',''))
    
matches
res3=[i for j, i in enumerate(matches) if(j%2)==0]
res3


# In[62]:


points=[]
for i in soup.find_all('td', class_="table-body__cell u-center-text"):
    points.append(i.text.replace('\n',''))
    
points
res4=[i for j, i in enumerate(points) if(j%2)!=0]
res4


# In[63]:


rating=[]
for i in soup.find_all('td', class_="table-body__cell u-text-right rating"):
    rating.append(i.text.replace('\n',''))
    
rating


# In[ ]:





# In[ ]:





# b) Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[64]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
page


# In[65]:


soup=BeautifulSoup(page.content)
soup


# In[66]:


womens_batting=[]
for i in soup.find_all('td', class_="table-body__cell rankings-table__name name"):
    womens_batting.append(i.text.replace('\n',''))
    
womens_batting


# In[67]:


team=[]
for i in soup.find_all('span', class_="table-body__logo-text"):
    team.append(i.text.replace('\n',''))
    
team


# In[68]:


rating=[]
for i in soup.find_all('td', class_="table-body__cell rating"):
    rating.append(i.text)
    
rating


# In[69]:


print(len(womens_batting), len(team), len(rating))


# In[70]:


import pandas as pd
df=pd.DataFrame({'Womens Batting Name':womens_batting, 'Team':team, 'Rating':rating})
df


# In[71]:


df.head(10)


# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[72]:


page=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
page


# In[73]:


soup=BeautifulSoup(page.content)
soup


# In[74]:


all_rounder=[]
for i in soup.find_all('td', class_="table-body__cell rankings-table__name name"):
    all_rounder.append(i.text.replace('\n',''))
    
all_rounder


# In[75]:


team=[]
for i in soup.find_all('span', class_="table-body__logo-text"):
    team.append(i.text)
    
team


# In[76]:


rating=[]
for i in soup.find_all('td', class_="table-body__cell rating"):
    rating.append(i.text)
    
rating


# In[77]:


print(len(all_rounder), len(team), len(rating))


# In[78]:


df=pd.DataFrame({"All Rounder's Name":all_rounder, 'Team':team, 'Rating':rating})
df


# In[79]:


df.head(10)


# # 7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# 

# i) Headline
# 

# In[2]:


page=requests.get('https://www.cnbc.com/world/?region=world')
page


# In[3]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


headlines=[]
for i in soup.find_all('div', class_="LatestNews-headlineWrapper"):
    headlines.append(i.text.replace('Ago','Ago ').split('Ago')[1])
    
headlines


# In[7]:


df=pd.DataFrame(headlines)
df


# ii) Time

# In[8]:


time=[]
for i in soup.find_all('time', class_="LatestNews-timestamp"):
    time.append(i.text)
    
time


# In[9]:


df=pd.DataFrame(time)
df


# iii) News Link

# In[10]:



import re
for i in soup.find_all('a', attrs={'href': re.compile("^https://")}):
    #link.append(i.text)
    link=i.get('href')
    print(link)
    


# # 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days. 
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# 

# Scrape below mentioned details :
# 
# i) Paper Title

# In[94]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[95]:


soup=BeautifulSoup(page.content)
soup


# In[96]:


titles=[]
for i in soup.find_all('h2', class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    titles.append(i.text)
    
titles


# ii) Authors

# In[97]:


author=[]
for i in soup.find_all('span', class_="sc-1w3fpd7-0 pgLAT"):
    author.append(i.text)
    
author


# iii) Published Date

# In[98]:


date=[]
for i in soup.find_all('span', class_="sc-1thf9ly-2 bKddwo"):
    date.append(i.text)
    
date


# iv) Paper URL 
# 

# In[100]:


import re
for i in soup.find_all('a', attrs={'href': re.compile("^https://")}):
    link=i.get('href')
    print(link)


# # 9) Write a python program to scrape mentioned details from dineout.co.in :

# i) Restaurant name

# In[101]:


page=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[102]:


soup=BeautifulSoup(page.content)
soup


# In[103]:


restaurant=[]
for i in soup.find_all('div', class_="restnt-info cursor"):
    restaurant.append(i.text.split(',')[0])
    
restaurant


# In[104]:


cuisine=[]
for i in soup.find_all('span', class_="double-line-ellipsis"):
    cuisine.append(i.text.split('|')[1])
    
cuisine


# iii) Location

# In[105]:


loc=[]
for i in soup.find_all('div', class_="restnt-loc ellipsis"):
    loc.append(i.text)
    
loc


# iv) Ratings

# In[106]:


rate=[]
for i in soup.find_all('div', class_="restnt-rating rating-4"):
    rate.append(i.text)
    
rate


# v) Image URL

# In[107]:


img_url=[]
for i in soup.find_all('img', class_="no-img"):
    img_url.append(i['data-src'])
    
img_url


# In[ ]:





# # 10) Write a python program to scrape the details of top publications from Google Scholar from

# https://scholar.google.com/citations?view_op=top_venues&hl=en
#     
# i) Rank

# In[108]:


page=requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[109]:


soup=BeautifulSoup(page.content)
soup


# In[110]:


rank=[]
for i in soup.find_all('td', class_="gsc_mvt_p"):
    rank.append(i.text.replace('.',''))
    
rank


# ii) Publication

# In[111]:


publication=[]
for i in soup.find_all('td', class_="gsc_mvt_t"):
    publication.append(i.text)
    
publication


# iii) h5-index

# In[115]:


index=[]
for i in soup.find_all('td', class_="gsc_mvt_n"):
    index.append(i.text)
    
index
res5=[ i for j, i in enumerate(index) if(j%2)==0]
res5


# iv) h5-median

# In[116]:


h5m=[]
for i in soup.find_all('span', class_="gs_ibl gsc_mp_anchor"):
    h5m.append(i.text)
    
h5m


# In[118]:


print(len(rank), len(publication), len(res5), len(h5m))


# In[119]:


df=pd.DataFrame({'Rank':rank, 'Publication':publication, 'h5-index':res5, 'h5-median':h5m})
df


# In[ ]:




