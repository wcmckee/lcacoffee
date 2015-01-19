
# coding: utf-8

# <h1>lcacoffee</h1>
# 
# script that displays coffees sold by hour at lca2015.
# Currently it opens a .json file and converts it into a python dict. 

# In[7]:

import json
import os
import pandas


# In[8]:

opcvs = open('/home/wcmckee/Downloads/convertcsv.json', 'r')


# In[9]:

opzrd = opcvs.read()


# In[10]:

jdunp = json.loads(opzrd)


# In[11]:

valia = []


# In[12]:

#pandas.read_json(jdunp)


# In[13]:

jdunp.count(int)


# In[14]:

len(jdunp)


# ok if i cycle through jdunp between 0 and 23 i get the results.
# 
# cycle through ints but as a string. must add ' '

# In[15]:

for numtwn in range(0,24):
    print "'" + str(numtwn) + "'"


# In[16]:

for jdr in jdunp:
    print jdr['0']


# In[17]:

for numtwn in range(0,24):
        print "'" + str(numtwn) + "'"


# In[18]:

for dej in jdunp:
    print dej.values()
    valia.append(dej.values())


# In[18]:




# In[19]:

dezrand = len(valia)


# In[20]:

azlis = []


# In[21]:

for vals in valia:    
    print vals
    azlis.append(vals)


# I need to filter the - - from the results. I really only need the values that have numbers. 
# 
# Take number in brackets away from number not in brackets. 
# The number in brackets is total amount of coffees sold. The number not in brackets is amount of volchers used. 
# The number that I get when i take away is the coffee sold without volchers. 
# 
# New dict that shows only the times that coffee were sold and the amount of coffgfges that were solf. Maybe that would works. 

# In[22]:

betra = []


# In[23]:

for azl in azlis:
    betra.append(azl)


# In[24]:

anoe = []
anez = []


# In[25]:

for betr in betra:
    betr.append(anoe)


# In[26]:

for deta in betr:
    #print deta
    if '- -' in deta:
        print deta
    else:
        anez.append(deta)


# In[27]:

fdic = []


# In[27]:




# In[28]:

for resut in anez:
    print resut
    fdic.append(resut)


# How come it is only adding the wednesday data in the results. It needs to have all the datas. 
# 
# Needs to take the number in brackets away from the number not in brackets.

# In[29]:

fdic


# In[30]:

optue = open('/home/wcmckee/Downloads/saletues.json', 'r')


# In[31]:

rdtue = optue.read()


# In[32]:

tuejs = json.loads(rdtue)


# In[39]:

tuejs


# In[41]:

for bran in tuejs:
    print bran


# In[ ]:



