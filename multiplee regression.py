#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt


# In[9]:


df1=pd.read_excel('Trucking.xlsx')
df1


# In[11]:


import matplotlib.pyplot as plt
plt.scatter(df1['x1'],df1['travel_time'],color="green")
plt.ylabel('Travel time')
plt.title('simple linear regression with miles traveled')


# In[12]:


plt.scatter(df1['n_of_deliveries'],df1['travel_time'],color='red')
plt.ylabel('Travel time')
plt.title('simplle linear regression with number of deliveries')


# In[19]:


import matplotlib.pyplot as plt
plt.figure()
plt.scatter(df1['x1'],df1['travel_time'],color='green')
plt.scatter(df1['n_of_deliveries'],df1['travel_time'],color='red')
plt.ylabel('Travel time')
plt.title('Multiple regression')
plt.xlabel('x1 in green and x2 in red')


# In[20]:


Reg1=ols(formula="travel_time~ x1",data=df1)
Fit1=Reg1.fit()
print(Fit1.summary())


# In[24]:


from statsmodels.formula.api import ols
model=ols('travel_time~x1+n_of_deliveries',data=df1).fit()
model.summary()


# In[25]:


print(anova_lm(Fit1))


# In[30]:


anova_table=anova_lm(model,type=1)
anova_table


# In[ ]:




