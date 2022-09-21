#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset=pd.read_csv('retail_bakery_transactions.csv')


# In[4]:


dataset.columns=dataset.columns.str.lower()


# In[7]:


dataset=dataset.applymap(lambda s:s.lower() if type(s)==str else s)


# In[8]:


dataset.head()


# In[9]:


dataset.info()


# In[10]:


dataset.isnull().sum()


# In[12]:


transaction_list=dataset.groupby(['transaction','date_time'])['item'].apply(lambda x:list(x))


# In[13]:


transaction_list.head()


# In[14]:


df=transaction_list.values.tolist()


# In[15]:


df[:5]


# In[16]:


from mlxtend.preprocessing import TransactionEncoder


# In[17]:


encoder=TransactionEncoder().fit(df)


# In[18]:


onehot=encoder.transform(df)


# In[21]:


transf_df=pd.DataFrame(onehot,columns=encoder.columns_)


# In[22]:


transf_df.head()


# In[24]:


from mlxtend.frequent_patterns import fpgrowth


# In[34]:


frequent_itemsets=fpgrowth(transf_df,min_support=0.05,use_colnames=True)


# In[35]:


frequent_itemsets.sort_values('support',ascending=False)


# In[36]:


frequent_itemsets['length']=frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets


# In[38]:


frequent_itemsets['length'].value_counts()


# In[40]:


from mlxtend.frequent_patterns import association_rules


# In[42]:


rule=association_rules(frequent_itemset,metric='lift',min_threshold=1.0)


# In[44]:


rule.head()


# In[ ]:




