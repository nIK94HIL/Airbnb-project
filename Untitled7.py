#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


df = pd.read_csv("datasets.csv")
df


# In[4]:


df = pd.read_csv("datasets.csv").head()
df


# In[6]:


df.tail()


# In[3]:


df.shape


# In[9]:


df = pd.read_csv("datasets.csv")
df


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


df.dropna(inplace = True)


# In[8]:


df.isnull().sum()


# In[9]:


df.shape


# In[10]:


df.duplicated().sum()

df[df.duplicated()]


# In[11]:


df.drop_duplicates(inplace = True)


# In[12]:


df.duplicated().sum()
df[df.duplicated()]


# In[13]:


df.dtypes


# In[14]:


df['id'] = df['id'].astype(object)

df['host_id'] = df['host_id'].astype(object)


# In[29]:


df.dtypes


# In[20]:


plt.figure(figsize = (8,5))
sns.histplot(data=data, x = 'price',bins = 100)
plt.ylabel("Frequency")
plt.show()


# In[16]:


data = df[df['price']<1500]

sns.boxplot(data = data,x = 'price')


# In[21]:


df.columns


# In[23]:


sns.barplot(data = data,x ='neighbourhood_group',y = 'price',hue = 'room_type')


# In[29]:


plt.figure(figsize =(8,5))
plt.title("Locality and Review Dependency")
sns.scatterplot(data = data,x = 'number_of_reviews', y= 'price',hue = 'neighbourhood_group')
plt.show()


# In[30]:


sns.pairplot(data = data,vars = ['price','minimum_nights','number_of_reviews','availability_365'],hue = 'room_type')


# In[31]:


df.columns


# In[35]:


plt.figure(figsize = (10,7))
sns.scatterplot(data = data,x = 'longitude',y = 'latitude',hue = 'room_type')
plt.title("Geographical Distribution of AirBnb Listing")
plt.show()


# In[36]:


df.columns


# In[40]:


corr = df[['latitude','longitude','price','minimum_nights','number_of_reviews','reviews_per_month','availability_365','beds']].corr()
corr

plt.figure(figsize = (10,8))
sns.heatmap(data = corr,annot = True)


# In[ ]:




