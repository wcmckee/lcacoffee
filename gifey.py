
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


# In[6]:

import requests
import json
import shutil
import dominate
from time import gmtime, strftime

import getpass

from walkdir import filtered_walk, dir_paths, all_paths, file_paths


# In[7]:

getusr = getpass.getuser()


# In[8]:

getusr


# In[3]:

keyword = input('Keyword: ')


# In[4]:

from dominate.tags import *


# In[11]:

gifdi = os.listdir('/home/' + getusr + '/gify/')


# In[12]:

gifdi


# In[13]:

keywddir = ('/home/' + getusr + '/gify/' + keyword)


# In[14]:

if os.path.isdir(keywddir) == True:
    print ('its true')
else:
    print ('its false')
    os.mkdir(keywddir)


# In[15]:

opwritj = requests.get('http://api.giphy.com/v1/gifs/search?q=' + keyword + '&api_key=dc6zaTOxFJmzC')


# In[16]:

wrijrd = opwritj.text


# In[17]:

jswri = json.loads(wrijrd)


# In[18]:

jswln = len(jswri['data'])


# In[19]:

jswln


# In[20]:

for jsw in range(0, jswln):
    if '.gif' in jswri['data'][jsw]['images']['downsized']['url']:
        print(jswri['data'][jsw]['images']['downsized']['url'])
        response = requests.get((jswri['data'][jsw]['images']['downsized']['url']), stream=True)
        with open(keywddir + '/' + str(jsw) + '.gif', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            del response


# In[23]:

gifdi = os.listdir('/home/' + getusr + '/gify/')


# In[24]:

gifdi


# In[25]:

keyword


# In[27]:

posfild = ('/home/' + getusr + '/gify/site/posts/')


# In[28]:

posfild


# In[29]:

#galdir = ('galleries/' + keyword + '/' +)


# In[44]:

keyosli = os.listdir(keywddir)


# In[49]:

doc = dominate.document(title='gify')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div():
        attr(cls='header')
        h1('Gify ' + keyword)
        p(img('imgs/logo.svg', src='imgs/logo.svg'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        h1('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
    
    

with doc:
    with div(id='body').add(ol()):
        for rdz in keyosli:
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
        p('Gify is open source')
        a('https://github.com/getsdrawn/getsdrawndotcom')
        a('https://reddit.com/r/redditgetsdrawn')

#print doc


# In[53]:

savht = open('/home/' + getusr +'/gify/' + keyword + '/index.html' , 'w')


# In[54]:

savht.write(str(doc))


# In[55]:

savht.close()

