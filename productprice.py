
# coding: utf-8

# Product Price
# 
# Script to edit prices for products.
# 

# In[1]:

import os


# In[4]:

prodir = ('/home/wcmckee/sellcoffee/products/')


# In[5]:

print os.listdir(prodir)


# In[6]:

pricewhat = raw_input('Product to set price: ')


# In[7]:

priceset = raw_input('Price to set: ')


# In[8]:

fpathz = (prodir + pricewhat + '/' + pricewhat + '-price')


# In[10]:

wrpric = open(fpathz, 'w')


# In[11]:

wrpric.write(priceset)


# In[12]:

wrpric.close()


# In[14]:

rdpric = open(fpathz, 'r')

print rdpric.read()

rdpric.close()


# In[ ]:



