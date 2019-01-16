
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


ds = pd.read_csv('data/dataset-price.csv')


# In[4]:


ds.head()


# In[5]:


dt = ds.set_index(['Month','Day'])
dt.head()


# In[6]:


dt.plot(figsize=(20,10),subplots= True);

