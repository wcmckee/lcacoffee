
# coding: utf-8

# In[1]:

import os


# In[2]:

import requests
import json
import shutil
import dominate
from time import gmtime, strftime


# In[3]:

keyword = input('Keyword: ')


# In[4]:

from dominate.tags import *


# In[5]:

gifdi = os.listdir('/home/wcmckee/Downloads/gify/')


# In[ ]:




# In[6]:

opwritj = requests.get('http://api.giphy.com/v1/gifs/search?q=' + keyword + '&api_key=dc6zaTOxFJmzC')


# In[ ]:




# In[7]:

wrijrd = opwritj.text


# In[8]:

jswri = json.loads(wrijrd)


# In[9]:

jswln = len(jswri['data'])


# In[10]:

jswln


# In[11]:

for jsw in range(0, jswln):
    if '.gif' in jswri['data'][jsw]['images']['downsized']['url']:
        print(jswri['data'][jsw]['images']['downsized']['url'])
        response = requests.get((jswri['data'][jsw]['images']['downsized']['url']), stream=True)
        with open('/home/wcmckee/Downloads/gify/'+ str(jsw) + '.gif', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            del response


# In[ ]:




# In[ ]:




# In[12]:

gifdi = os.listdir('/home/wcmckee/Downloads/gify/')


# In[13]:

gifdi


# In[ ]:




# In[ ]:




# In[14]:

doc = dominate.document(title='gify')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div():
        attr(cls='header')
        h1('Gify')
        p(img('imgs/logo.svg', src='imgs/logo.svg'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        h1('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
    
    

with doc:
    with div(id='body').add(ol()):
        for rdz in gifdi:
            #h1(rdz.title)
            #a(rdz.url)
            #p(img(rdz, src='%s' % rdz))
            #print rdz
            p(img(rdz, src = rdz))
            p(rdz)


                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            #h1(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))

    with div():
        attr(cls='body')
        p('GetsDrawn is open source')
        a('https://github.com/getsdrawn/getsdrawndotcom')
        a('https://reddit.com/r/redditgetsdrawn')

#print doc


# In[15]:

print(doc)


# In[16]:

savht = open('/home/wcmckee/Downloads/gify/index.html', 'w')


# In[17]:

savht.write(str(doc))


# In[18]:

savht.close()


# In[ ]:




# In[ ]:




# In[ ]:



