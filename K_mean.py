#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_excel('Clustering_ex.xlsx')
data


# In[8]:


fig=plt.figure(figsize=(5,5))
x=data['Variable_1']
y=data['Variable_2']
n=range(1,8)
fig, ax=plt.subplots()
ax.scatter(x,y,marker='o',c='red',alpha=0.5)
plt.grid()
plt.xlabel("Variable_1")
plt.ylabel("Variable_2")
for i,txt in enumerate(n):
      ax.annotate(txt,(x[i],y[i]))


# In[9]:


from sklearn.cluster import KMeans

KMeans=KMeans(n_clusters=2)
KMeans.fit(data)


# In[10]:


labels=KMeans.predict(data)
centroids=KMeans.cluster_centers_


# In[11]:


centroids


# In[15]:


fig=plt.figure(figsize=(5,5))
colmap={1:'r',2:'b'}
colors=map(lambda x:colmap[x+1], labels)
colors1=list(colors)
fig, ax=plt.subplots()
ax.scatter(x,y,color=colors1,alpha=0.5,edgecolor='k')
for idx,centroid in enumerate(centroids):
    plt.scatter(*centroid,color=colmap[idx+1])
    
for i,txt in enumerate(n):
    ax.annotate(txt,(x[i],y[i]))
plt.grid()
plt.xlim(0,8)
plt.ylim(0,8)
plt.show()
        


# In[ ]:




