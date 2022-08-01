#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[7]:


df=pd.read_csv("C:/Users/User/Downloads/employees.csv")
df


# In[8]:


print(df.dtypes)
print(df.describe())


# In[10]:


print('Salary')
print(df['Salary'].head(10))


# In[11]:


print(df['Gender'].head(10))


# In[15]:


missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df=pd.read_csv("C:/Users/User/Downloads/employees.csv",na_values=missing_value_formats)
print(df['Gender'].head(10))


# In[22]:


import pandas as pd
missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df=pd.read_csv("C:/Users/User/Downloads/employees.csv",na_values=missing_value_formats)

def make_int(i):
    try:
        return int (i)
    except:
        return pd.np.nan
    df['Salary']=df['Salary'].map(make_int)
    


# In[23]:



    print(df['Salary'].head())


# In[24]:


print(df['Gender'].isnull().head(10))
print(df['Gender'].notnull().head(10))


# In[25]:


null_filter=df["Gender"].notnull()
print(df[null_filter].head())


# In[26]:


print(df.isnull().values.any())


# In[27]:


print(df.isnull().sum())


# In[28]:


new_df=df.dropna(axis=0)
print(new_df.isnull().values.any())


# In[31]:


new_df=df.dropna(axis=0,how='any')

print(new_df)


# In[34]:


new_df=df.dropna(axis=0,how='all')
print(new_df)


# In[35]:


new_df=df.dropna(axis=1,how='any') 
print(new_df)


# In[36]:


new_df=df.dropna(axis=1,how='all')  
print(new_df)


# In[37]:


df['Salary'].fillna(method='pad')


# In[38]:


df['Salary'].fillna(method='bfill')


# In[40]:


df['Salary'].fillna(df['Salary'].median())


# In[41]:


df['Salary'].fillna(int(df['Salary'].mean()))


# In[42]:


df['Salary'].replace(to_replace=np.nan,value=0)


# In[43]:


df['Salary'].interpolate(method="linear",direction="forward")


# In[ ]:




