
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


examinee = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew',
'Laura', 'Kevin', 'Jonas'],
'scores': [12.5, 9, 16.5, 2.3, 9, 20, 14.5, 4.5, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualified':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
data = pd.DataFrame(examinee)


# In[4]:


data


# In[5]:


data.replace(['yes','no'],[1,0])

