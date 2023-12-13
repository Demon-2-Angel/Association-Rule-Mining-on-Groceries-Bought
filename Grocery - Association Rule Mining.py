#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


try:
    import apyori
except:
    get_ipython().system('pip install apyori')

from apyori import apriori


# In[4]:


df = pd.read_csv(r"C:\Users\aniru\Machine Learning\Datasets\Grocery Dataset\Groceries_dataset.csv", parse_dates=['Date'])
df.head()


# In[5]:


df.isnull().any()


# In[6]:


all_products = df['itemDescription'].unique()
print("Total products: {}".format(len(all_products)))


# In[7]:


def ditribution_plot(x,y,name=None,xaxis=None,yaxis=None):
    fig = go.Figure([
        go.Bar(x=x, y=y)
    ])

    fig.update_layout(
        title_text=name,
        xaxis_title=xaxis,
        yaxis_title=yaxis
    )
    fig.show()


# In[8]:


x = df['itemDescription'].value_counts()
x = x.sort_values(ascending = False) 
x = x[:10]

ditribution_plot(x=x.index, y=x.values, yaxis="Count", xaxis="Products")


# In[9]:


one_hot = pd.get_dummies(df['itemDescription'])
df.drop('itemDescription', inplace=True, axis=1)
df = df.join(one_hot)
df.head()


# In[10]:


records = df.groupby(["Member_number","Date"])[all_products[:]].apply(sum)
records = records.reset_index()[all_products]


# In[11]:


def get_Pnames(x):
    for product in all_products:
        if x[product] > 0:
            x[product] = product
    return x

records = records.apply(get_Pnames, axis=1)
records.head()


# In[12]:


print("total transactions: {}".format(len(records)))


# In[13]:


## Removing zeros
x = records.values
x = [sub[~(sub == 0)].tolist() for sub in x if sub[sub != 0].tolist()]
transactions = x


# In[14]:


transactions[0:10]


# In[15]:


rules = apriori(transactions,min_support=0.00030,min_confidance=0.05,min_lift=3,min_length=2,target="rules")
association_results = list(rules)


# In[16]:


for item in association_results:

    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    print("Support: " + str(item[1]))

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")


# In[ ]:




