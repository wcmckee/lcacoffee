
# coding: utf-8

# Record Desktop Auto
# 
# Automatic start recording monitor when gimp opens and stop recording on gimp exit. Every hour make a new file. Pause record if mouse doesnt move for x time. 

# In[ ]:




# Record Desktop Automation
# 
# Script that helps recording digital painting with recordmydesktop.
# 
# 

# In[52]:

import os
import arrow
import json


# In[ ]:




# In[34]:

mytim = arrow.now()


# In[35]:

mytim


# In[36]:

mytimdat = mytim.datetime


# In[37]:

mytimdat.minute


# In[38]:

timtest  = str(mytimdat.hour) + str(mytimdat.minute) + str(mytimdat.second) 


# In[39]:

timtest


# In[40]:

timdatez = str(mytimdat.year) + str(mytimdat.month) + str(mytimdat.day)


# In[ ]:




# In[41]:

timdatez


# In[44]:

fulldtiz = str(timdatez) + str(timtest)


# In[46]:

fulldtiz


# In[47]:

rcordcmd = ('recordmydesktop -o /home/pi/Desktop/' + fulldtiz + ('.ogv --no-sound --on-the-fly-encoding'))


# In[48]:

rcordcmd


# In[50]:

#Make a meta file that contains file info. 
#


# In[51]:

opmeta = open('/home/pi/Desktop/' + fulldtiz + '.json', 'w')


# In[60]:

recordict = dict()


# In[61]:

recordict.update({'videofile': '/home/pi/Desktop/' + fulldtiz + '.ogv'})


# In[62]:

recordict


# Copyright is a barrier. What is your views on open source licences such as creative commons?

# In[ ]:

os.system(rcordcmd)


