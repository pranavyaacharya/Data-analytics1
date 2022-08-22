#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[9]:


acad=pd.read_excel('C:/Users/User/Downloads/acad.xlsx')


# In[10]:


acad


# In[11]:


obs=pd.pivot_table(acad[['g','sm']],index='g',columns='sm',aggfunc=len)
obs


# In[12]:


from scipy.stats import chi2_contingency


# In[14]:


chi2,p,dof,tbl=chi2_contingency(obs)


# In[15]:


chi2


# In[16]:


p


# In[17]:


dof


# In[18]:


tbl


# In[ ]:




