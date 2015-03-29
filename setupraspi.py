
# coding: utf-8

# Setup Raspberry Pi
# 
# Script used on freshly installed raspbrien install on a Raspberry Pi.
# Installs IPython Notebook
# Gets .ssh folder from local server
# Copy folders from local server.
# Home, Github code, sellcoffee,
# 
# Install Python script requirments
# (pip arrow/praw/requests etc).
# Install from local server
# 
# 

# In[1]:

#ssh into the pi and start doing commands.


# In[2]:

import shutil


# In[3]:

import os


# In[ ]:

os.chdir('/home/wcmckee/ipython/')


# In[ ]:

os.system('sudo python setup.py install')

