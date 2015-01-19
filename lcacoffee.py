
# coding: utf-8

# <h1>lcacoffee</h1>
# 
# script that displays coffees sold by hour at lca2015.
# Currently it opens a .json file and converts it into a python dict. 

# In[29]:

import json
import os
import pandas
import getpass


# In[30]:

theuser = getpass.getuser()


# In[35]:

jsonfold = ('/home/' + theuser + '/github/lcacoffee/')
alldata = ('salebyhour.json')
tueda = ('saletues.json')
weda = ('saleweds.json')
thura = ('salethurs.json')
fria = ('salefri.json')

salhr = (jsonfold + alldata)
salhr


# In[36]:

opcvs = open(salhr, 'r')


# In[37]:

opzrd = opcvs.read()


# In[38]:

jdunp = json.loads(opzrd)


# In[39]:

valia = []


# In[40]:

#pandas.read_json(jdunp)


# In[41]:

jdunp.count(int)


# In[42]:

len(jdunp)


# ok if i cycle through jdunp between 0 and 23 i get the results.
# 
# cycle through ints but as a string. must add ' '

# In[43]:

for numtwn in range(0,24):
    print "'" + str(numtwn) + "'"


# In[44]:

for jdr in jdunp:
    print jdr['0']


# In[45]:

for numtwn in range(0,24):
        print "'" + str(numtwn) + "'"


# In[46]:

for dej in jdunp:
    print dej.values()
    valia.append(dej.values())


# In[46]:




# In[47]:

dezrand = len(valia)


# In[48]:

azlis = []


# In[49]:

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

# In[16]:

betra = []


# In[17]:

for azl in azlis:
    betra.append(azl)


# In[18]:

anoe = []
anez = []


# In[19]:

for betr in betra:
    betr.append(anoe)


# In[20]:

for deta in betr:
    #print deta
    if '- -' in deta:
        print deta
    else:
        anez.append(deta)


# In[21]:

fdic = []


# In[21]:




# In[22]:

for resut in anez:
    print resut
    fdic.append(resut)


# How come it is only adding the wednesday data in the results. It needs to have all the datas. 
# 
# Needs to take the number in brackets away from the number not in brackets.

# In[23]:

fdic


# In[24]:

optue = open('/home/wcmckee/Downloads/saletues.json', 'r')


# In[25]:

rdtue = optue.read()


# In[26]:

tuejs = json.loads(rdtue)


# In[27]:

tuejs


# In[28]:

for bran in tuejs:
    print bran


# In[28]:




# In[28]:




# In[ ]:



