
# coding: utf-8

# <h1>Sale Rev</h1>
# 
# <h3>Sale Reverse. Sell Stuff.</h3>
# 
# Python script for point of sale computer time.
# 
# more $ == more time.
# 
# Opens up sales data of products and saves for daily reports.
# 
# Saving the data as a json object. File has name of product as key and amount sold for value. 
# 
# Easily merge json files. 
# 
# At the end of each day keep the product in product folder but change sales data to 0.
# 
# 

# In[123]:

import arrow
import os
import json


# In[124]:

arut = arrow.utcnow()


# In[ ]:

arday = arut


# In[168]:




# In[165]:

cofdot = dict()


# In[126]:

#print('a to add time, b to remove time, c to')


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


# In[158]:

jsday = json.dumps(daydict)


# In[163]:

#The json object.  Should sale it to a folder. Maybe to 
#/yr/mnth/day folder?
#All in one folder, name of json file is datetime.

jsday


# In[ ]:




# In[169]:

savjsf = open('/home/wcmckee/sellcoffee/archive/' + str(arut.date()) + '.json', 'w')


# In[170]:

savjsf.write(jsday)


# In[171]:

savjsf.close()


# In[172]:

#Reset value of int in products/nameofproducts folder to 0.


# In[174]:

for lst in lsitems:
    print lst
    opfolaz = open('/home/wcmckee/sellcoffee/products/' + lst, 'w')
    opfolaz.write('0')
    opfolaz.close()


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



