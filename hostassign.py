
# coding: utf-8

# script to assign hostname and ip address to machine

# In[63]:

import os
import random
import json
import shutil


# In[37]:

colordir = os.listdir('/home/wcmckee/colortest/')


# In[42]:

alcolrz = []


# In[43]:

for cold in colordir:
    #print cold
    if '.json' in cold:
        print cold
        alcolrz.append(cold)


# In[47]:

alranza = random.choice(alcolrz)


# In[48]:

alranza


# In[71]:

checkexist = os.listdir('/home/wcmckee/colortest/assignedhosts/')
assignedh = []


# In[72]:

for chex in checkexist:
    print chex
    assignedh.append(chex)
    #os.remove('/home/wcmckee/colortest/' + chex)


# In[73]:

colordir


# In[80]:

assignedh


# In[83]:

toremvz = set(colordir) & set(assignedh)


# In[88]:

tolidt = list(toremvz)


# In[91]:

for tolid in tolidt:
    print tolid
    os.remove('/home/wcmckee/colortest/' + tolid)


# In[ ]:




# In[ ]:




# In[89]:

tolidt


# In[50]:

opjsflz = open('/home/wcmckee/colortest/' + alranza, 'r')


# In[51]:

nerza = opjsflz.read()


# In[53]:

nerza


# In[55]:

neadict = json.loads(nerza)


# In[8]:

opipdy = open('/home/wcmckee/colortest/freeip.txt', 'r')
iprdy = opipdy.read()


# In[12]:

ipclean = iprdy.replace('\n', ', ')


# In[13]:

ipclean


# In[15]:

ipliszq = ipclean.split(',')


# In[23]:

#New hostname is zero on the list. Need to remove this now

newhos = ipliszq[0]


# In[24]:

newhos


# In[57]:

neadict.update({'ipaddress' : newhos})


# In[58]:

neadict


# In[60]:

convjsn = json.dumps(neadict)


# In[62]:

convjsn
convipdy = open('/home/wcmckee/colortest/' + alranza, 'w')
convipdy.write(convjsn)
convipdy.close()


# In[64]:

shutil.move('/home/wcmckee/colortest/' + alranza, '/home/wcmckee/colortest/assignedhosts/')


# In[ ]:

#shutil.move('/home/wcmckee/colortest/' + alranza, '/home/wcmckee/colortest/assignedhosts/')


# In[29]:

newlisav = ipliszq[1:]


# In[35]:

newlisav

newfre = open('/home/wcmckee/colortest/freeip.txt', 'w')

for lisaw in newlisav:
    #print lispo
    newfre.write(str(lisaw))
    newfre.write('\n')

newfre.close()


# In[19]:

for ipzq in ipliszq:
    print ipzq


# In[ ]:



