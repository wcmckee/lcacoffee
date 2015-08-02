
# coding: utf-8

# script that opens up public key from local webserver and copies the key to authorized keys.
# 

# In[32]:

#import requests
import urllib
#import os
import shutil
import getpass


# In[33]:

getusr = getpass.getuser()


# In[ ]:




# In[24]:

ipscpub = ('http://192.168.1.2')


# In[25]:

#os.chdir('/home/wcmckee/')


# In[34]:

reqpub = urllib.urlopen(ipscpub + '/id.pub')
    
#response = requests.get(ipscpub + '/id.pub', stream=True)
with open('/home/' + getusr + '/.ssh/authorized_keys', 'wb') as out_file:
    shutil.copyfileobj(reqpub, out_file)
    del reqpub


# In[ ]:



