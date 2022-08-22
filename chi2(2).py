#!/usr/bin/env python
# coding: utf-8

# In[2]:


import scipy
from scipy.stats import chi2
from scipy.stats import poisson


# In[4]:


import pandas as pd
import numpy as np


# In[5]:


data=pd.read_excel('P_distribution.xlsx')
data


# In[7]:


obseved_freq=data['Frequency']


# In[9]:


obseved_freq


# In[10]:


total_arrival=600
total_time_period=100
mu=total_arrival/total_time_period


# In[11]:


mu


# In[16]:


Expected_Freq=[]
for i in range(len(obseved_freq)):
    E_Freq=100*poisson.pmf(i,mu)
    Expected_Freq.append(E_Freq)


# In[17]:


Expected_Freq


# In[18]:


Expected_Freq_round_off=[round(elem,2)for elem in Expected_Freq]
Expected_Freq_round_off


# In[21]:


df=pd.DataFrame(list(zip(obseved_freq,Expected_Freq_round_off)),columns=['obseerved Frequency','Expected Frequency'])
df


# In[30]:


obs_freq=[5,10,14,20,12,12,9,8,10]
expected_freq=[6.20,8.92,13.39,16.06,16.06,13.77,10.33,6.88,8.39]


# In[31]:


scipy.stats.chisquare(obs_freq,expected_freq)


# In[ ]:




