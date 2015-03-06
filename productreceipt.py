
# coding: utf-8

# Product Receipt
# 
# Adds together items and content from sellcofee/archive

# In[39]:

import os
import json
import dominate
from dominate.tags import * 
from time import gmtime, strftime
import time


# In[30]:

arctdir = ('/home/wcmckee/sellcoffee/archive/')


# In[31]:

arctdir


# In[32]:

lisar = os.listdir(arctdir)


# In[33]:

finlis = []


# In[34]:

for li in lisar:
    print li
    opli = open(arctdir + li, 'r')
    oprd = opli.read()
    finlis.append(oprd)


# In[35]:

#Merge together sales by time.


# In[36]:

#deblis = 


# In[37]:

for fi in finlis:
    #print fi
    newjs = json.loads(fi)
    print newjs['product']
    print newjs
    #print newjs['cost']
    print newjs['time']
    print newjs['date']
    print newjs['amount']


# In[41]:

finlis


# In[40]:

doc = dominate.document(title='BroBeur CyberCafe Transactions')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div():
        attr(cls='header')
        h1('BroBeur CyberCafe Transactions')
        h3('BroBeur CyberCafe Transactions')
        #p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        p('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
        #p(bodycom)
    
    

with doc:
    with div(id='body').add(ol()):
        for fi in finlis:
            #print fi
            newjs = json.loads(fi)
            h1(newjs['product'])
            #print newjs
            #print newjs['cost']
            p(newjs['time'])
            p(newjs['date'])
            p(newjs['amount'])
            #print newjs['cost']
            #oprdz = open((prodir + rdz + '/' + rdz + '-id'), 'r')
            #p('id: ' + oprdz.read())
            #oprdz.close()
            
            #prrdz = open((prodir + rdz + '/' + rdz + '-price'), 'r')
            #p('price: ' + prrdz.read())
            #prrdz.close()


                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            #h1(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))

    with div():
        attr(cls='body')
        p('sellcoffee is open source')
        a('https://github.com/wcmckee/lcacoffee')
        #a('https://reddit.com/r/redditgetsdrawn')

print doc


# In[ ]:

docre = doc.render()
#s = docre.decode('ascii', 'ignore')
yourstring = docre.encode('ascii', 'ignore').decode('ascii')
indfil = ('/home/wcmckee/sellreceipt/index.html')
mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()

