
# coding: utf-8

# gifey
# 
# Downloads gifs based on a keyword from gifphy to a folder and serve them via a web server. 
# 
# Find keywords from where?
# 
# Creative Commons Keywords - add the gif back into the posts.
# 
# Intergrate Nikola. Start saving the gif files in galleries folder. Why doesn't galleries folder render gif files? 
# 
# Create nikola post that has the title (keyword) and post contents is the gif url (galleries - keyword)
# 
# 

# In[1]:

import os


# In[2]:

import requests
import json
import shutil
import dominate
from time import gmtime, strftime

import getpass

from walkdir import filtered_walk, dir_paths, all_paths, file_paths


# In[3]:

getusr = getpass.getuser()


# In[4]:

getusr


# In[17]:

keyword = input('Keyword: ')


# In[18]:

gifydir = ('/home/{}/gify/'.format(getusr))


# In[19]:

gifdi = os.listdir('/home/{}/gify/posts'.format(getusr))


# In[20]:

keywddir = ('/home/{}/gify/galleries/{}'.format(getusr, keyword))


# In[21]:

if os.path.isdir(keywddir) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(keywddir)


# In[22]:

opwritj = requests.get('http://api.giphy.com/v1/gifs/search?q={}&api_key=dc6zaTOxFJmzC'.format(keyword))


# In[23]:

wrijrd = opwritj.text


# In[24]:

jswri = json.loads(wrijrd)


# In[25]:

jswln = len(jswri['data'])


# In[26]:

jswln


# In[27]:

for jsw in range(0, jswln):
    if '.gif' in jswri['data'][jsw]['images']['downsized']['url']:
        print(jswri['data'][jsw]['images']['downsized']['url'])
        response = requests.get((jswri['data'][jsw]['images']['downsized']['url']), stream=True)
        with open(keywddir + '/' + str(jsw) + '.gif', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            del response


# In[28]:

os.chdir(gifydir)


# In[29]:

os.system('nikola build')


# In[ ]:



