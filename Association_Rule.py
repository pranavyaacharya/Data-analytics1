#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mlxtend


# In[2]:


import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori,association_rules


# In[4]:


df=pd.read_csv('GroceryStoreDataSet.csv',names=['products'],sep=',')
df.head()


# In[5]:


df.shape


# In[9]:


data=list(df['products'].apply(lambda x:x.split(",")))
data


# Apriori Algorithm and One Hot Encoding

# In[13]:


from mlxtend.preprocessing import TransactionEncoder
a=TransactionEncoder()
a_data=a.fit(data).transform(data)
df=pd.DataFrame(a_data,columns=a.columns_)
df=df.replace(False,0)
df=df.replace(True,1)
df


# In[17]:


df=apriori(df,min_support = 0.2, use_colnames = True, verbose = 1)
df 


# In[18]:


df_ar=association_rules(df,metric="confidence",min_threshold=0.6)
df_ar


# In[ ]:




