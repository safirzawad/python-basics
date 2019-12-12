
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[11]:


pd.read_csv('StockPriceData.csv', delimiter=',',usecols= ['Adj Close'])


# In[12]:


stock=pd.read_csv('StockPriceData.csv', delimiter=',',usecols= ['Adj Close'])


# In[13]:


data = pd.DataFrame(stock)


# In[14]:


data.plot()


# In[22]:


data.rolling(100).mean().plot()


# In[27]:


MySmoothe= data.rolling(100).mean()


# In[31]:


data['mynewcolumn'] = MySmoothe


# In[33]:


data.head(20)


# In[34]:


data.dropna()


# In[35]:


data.plot()

