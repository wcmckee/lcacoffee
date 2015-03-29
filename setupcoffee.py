
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


# In[ ]:




# In[6]:

os.mkdir(homdurz)


# In[ ]:



