
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# In[2]:


dataset = pd.read_csv('data/Dejay-price.csv',index_col='SlNo')
dataset.head()


# In[3]:


dataset['Rainfall(mm)'] = dataset['Rainfall(mm)'].convert_objects(convert_numeric=True)


# In[4]:


dataset['Date'] = pd.to_datetime(dataset.loc[:,['Year','Month','Day']])
dataset = dataset.set_index('Date')
dataset.head()


# In[38]:


def viz(x,y1,y2,y2l,title):
    fig,ax1 = plt.subplots(figsize=(12,6))
    color = 'tab:blue'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price', color=color)
    ax1.plot(x, y1, color=color, marker = '*')
    ax1.tick_params(axis='y', labelcolor=color)
    plt.legend()

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:red'
    ax2.set_ylabel(y2l, color=color)  # we already handled the x-label with ax1
    ax2.plot(x, y2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.title(title)
    plt.legend()
    plt.show()


# In[6]:


def viz1(d1,year):
    title = 'For year ' + str(year)
    d1.plot(figsize=(12,6),subplots= True, title = title)
    #plt.title('For Year ' + str(year))
    plt.show()


# In[7]:


def viz4(dfs,year):
    lbls = ['NoFestival','Festival']
    fig = plt.figure(figsize=(12,6))
    for i ,j in enumerate(np.unique(dfs.IsFestive)):
        plt.scatter(dfs[dfs.IsFestive == j].index,dfs[dfs.IsFestive == j]['Price'],c= ListedColormap(("red","green"))(i),label = lbls[j])
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Festival v/s Price for Year '+ str(year))
    plt.show()


# In[8]:


def desc(dataset,year):
    d4 = dataset[dataset.Year == year].loc[:,['Price','IsFestive']]
    #d1 = dataset[dataset.Year == year].loc[:,['MaxTemp','MinTemp','Price']]
    #viz1(d1,year)
    viz4(d4,year)


# In[9]:


def detail(dataset,year):
    d1 = dataset[dataset.Year == year].loc[:,['MaxTemp','MinTemp','Price']]
    viz(d1.index,d1['Price'],d1['MaxTemp'],'Temperature','Maximum Temperature v/s Price in Year '+ str(year))
    viz(d1.index,d1['Price'],d1['MinTemp'],'Temperature','Minimum Temperature v/s Price in Year '+ str(year))


# In[10]:


def detail2(dataset,year):
    d1 = dataset[dataset.Year == year].loc[:,['MaxRelativeHumidity(RH)','MinRelativeHumidity(RH)','Price']]
    viz(d1.index,d1['Price'],d1['MaxRelativeHumidity(RH)'],'Relative Humidity (RH)', 'Maximum Relative Humidity (RH) v/s Price in Year '+ str(year))
    viz(d1.index,d1['Price'],d1['MinRelativeHumidity(RH)'],'Relative Humidity (RH)', 'Minimum Relative Humidity (RH) v/s Price in Year '+ str(year))


# In[11]:


def detail3(dataset,year):
    d1 = dataset[dataset.Year == year].loc[:,['Rainfall(mm)','Price']]
    viz(d1.index,d1['Price'],d1['Rainfall(mm)'],'Rainfall(mm)', 'Rainfall (mm)) v/s Price in Year '+ str(year))


# In[35]:


desc(dataset,2010)


# In[12]:


desc(dataset,2011)


# In[13]:


desc(dataset,2012)


# In[14]:


desc(dataset,2013)


# In[15]:


desc(dataset,2014)


# In[16]:


desc(dataset,2015)


# In[39]:


detail(dataset,2010)


# In[18]:


detail(dataset,2011)


# In[19]:


detail(dataset,2012)


# In[20]:


detail(dataset,2013)


# In[21]:


detail(dataset,2014)


# In[22]:


detail(dataset,2015)


# In[23]:


detail2(dataset,2010)


# In[24]:


detail2(dataset,2011)


# In[25]:


detail2(dataset,2012)


# In[26]:


detail2(dataset,2013)


# In[27]:


detail2(dataset,2014)


# In[28]:


detail2(dataset,2015)


# In[29]:


detail3(dataset,2010)


# In[30]:


detail3(dataset,2011)


# In[31]:


detail3(dataset,2012)


# In[32]:


detail3(dataset,2013)


# In[33]:


detail3(dataset,2014)


# In[34]:


detail3(dataset,2015)

