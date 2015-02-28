
# coding: utf-8

# Sale Rev
# 
# Sale Reverse. Sell Internet.
# 
# Python script for point of sale computer time.
# 
# more $ == more time.

# In[123]:

import arrow
import os
import json


# In[124]:

arut = arrow.utcnow()


# In[ ]:

arday = arut


# In[125]:

cofdot = dict()


# In[126]:

print('a to add time, b to remove time, c to')


# In[127]:

#subscripe based.
#Get time

#Password expire.
#One month pass.
#10pm to 10am weekend pass.


# In[128]:

armonth = arday.replace(month=+1)


# In[129]:

armonth.month


# In[130]:

bemon = arday.replace(month=+4)


# In[131]:

lsitems = os.listdir('/home/wcmckee/sellcoffee/products/')


# In[132]:

lsitems

#Sales per day of items. Resets at midnight.


# In[133]:

dirza = ('/home/wcmckee/sellcoffee/products/')


# In[140]:

daydict = dict()

#daydict.update({'datetime': str(arday.utcnow())})


# In[141]:

for lsit in lsitems:
    print lsit
    #open each item up and read it.
    opitez = open(dirza + lsit, 'r')
    #print opitez.read()
    daydict.update({lsit : opitez.read()})
    opitez.close()
    
    #Make a json object for that days sales. 
    #Name of product. Amount Sold.
    


# In[142]:

print daydict


# In[143]:

#for r in arrow.Arrow.span_range('hour', arday, bemon):
    #print r
#    for res in r:
#        print res.humanize()
        


# In[144]:

#Total sales is value of all items in daydict


# In[147]:

print (daydict.values())


# In[149]:

addnum = 0 


# In[151]:

for dayv in daydict.values():
    print dayv
    addnum = addnum + int(dayv)


# In[156]:

totdsal = ('Total Sale numbers: ' + str(addnum))


# In[157]:

print totdsal


# In[ ]:



