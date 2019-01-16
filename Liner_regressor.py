
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


# In[5]:


X = dataset.loc[:,['MaxTemp','MinTemp']].values
y = dataset.loc[:,'Price'].values


# In[16]:


X[:,0]


# In[7]:


y


# In[17]:


from sklearn.cross_validation import train_test_split


# In[18]:


from sklearn.tree import DecisionTreeRegressor as DTR


# In[19]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25, random_state = 0)


# In[20]:


dtr = DTR(random_state=0)


# In[21]:


dtr.fit(X,y)


# In[22]:


y_pred = dtr.predict(X_test)


# In[23]:


from sklearn.metrics import confusion_matrix


# In[42]:


acc = y_test - y_pred
print(len(acc))
crct = acc[acc == 0]
print(len(crct))
incrct = acc[acc <= -75]
print(len(incrct))
pin = acc[acc >= 75]
print(len(pin))


# In[43]:


100 - ((len(incrct) + len(pin))/len(acc) * 100)

