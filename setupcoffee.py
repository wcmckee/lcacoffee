
# coding: utf-8

# Script to setup files and folders for the pos system.

# In[2]:

import os
import getpass


# In[3]:

getusr = getpass.getuser()


# In[ ]:




# In[4]:

homdurz = ('/home/' + getusr + '/sellcoffee')


# In[5]:

homdurz


# In[9]:

prodz = (homdurz + '/products')


# In[10]:

usrnam = (homdurz + '/usernames')


# In[11]:

usrnam


# In[ ]:




# In[6]:

os.mkdir(homdurz)


# In[8]:

os.mkdir(prodz)


# In[ ]:

os.mkdir(usrnam)

