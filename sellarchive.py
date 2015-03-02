
# coding: utf-8

# In[3]:

#Dict is 
#item product in dict. 'product' : 'internet'
#'count' : salesnum
#'tags' : tags to add
#Discount. add senior and under 18 prices.

#Read arcive folders


# In[4]:

import os


# In[6]:

rarch = os.listdir('/home/wcmckee/sellcoffee/archive/')


# In[7]:

rarch


# In[10]:

for rac in rarch:
    rejs = open('/home/wcmckee/sellcoffee/archive/' + rac, 'r')
    print rac
    print rejs.read()


# In[ ]:



