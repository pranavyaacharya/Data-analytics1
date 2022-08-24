#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error


# In[27]:


data = pd.read_excel("HARDNESS.xls")


# In[28]:


data


# In[29]:


from sklearn.model_selection import train_test_split


# In[30]:


x=data['Hardness'].values.reshape(-1,1)
y=data['Tensile strength'].values.reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=88)


# In[31]:


x_train.shape,x_test.shape,y_train.shape,y_test.shape


# In[32]:


len(x_train)


# In[33]:


len(x_test)


# In[34]:


x_train


# In[35]:


from sklearn.linear_model import LinearRegression
reg=LinearRegression()


# In[36]:


reg.fit(x_train,y_train)


# In[37]:


reg.intercept_


# In[38]:


reg.coef_


# In[39]:


y_predict=reg.predict(x_test)


# In[40]:


y_predict


# In[41]:


mean_squared_error(y_test, y_predict)


# In[42]:


reg.score(x_test,y_test)


# In[43]:


reg.score(x_train,y_train)


# In[ ]:




