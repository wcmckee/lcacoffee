
# coding: utf-8

# This is a script to create coffee sales data. 
# It uses the same base template as lcacoffee.ipnb.
# 
# Create a dict with coffee data in 

# In[23]:

import arrow
import os


# In[24]:

#I need it to return the day of the week it is.
#etc. Monday, Tuesday, Wednesday, Thursday


# In[6]:

arut = arrow.utcnow()


# In[31]:

cofdat = dict()


# In[32]:

print arut.date()


# In[33]:

print arut.time()


# In[34]:

arut.weekday()


# In[35]:

cofdat.update({'Day': arut.weekday()})


# In[39]:

cofdat.update({'Date': str(arut.date())})


# In[40]:

print cofdat


# In[45]:

for dayhr in range(24):
    #print dayhr
    cofdat.update({dayhr: ' '})


# In[53]:

twenforst = arut.strftime('%H')


# In[54]:

twenforst


# In[46]:

cofdat


# In[55]:

cofdat.update({twenforst: 1})


# In[58]:

#Whats the point in creating keys for hours that don't
#get sales. Just get it to update with hour and add it

#Value is a database on the coffee sale. 
#Currently just numbers.


# In[56]:

cofdat


# In[60]:

sincofd = dict()


# In[61]:

import getpass


# In[63]:

gusr = getpass.getuser()


# In[64]:

gusr


# In[65]:

#Outlet is username of sales person


# In[67]:

#Product is coffee name. 
#Open and read file that the customer asks
#for type of coffee. 
#Have a order folder that coffees are 
#qued into. 
#Sellcoffee folder
#Usernames - customers
#Staff - Staff list


# In[78]:

#opctype = open('/home/wcmckee/sellcoffee/usernames/')


# In[82]:

coftag = ('coffee, soymilk')


# In[85]:

#Amount of coffee sales
cofsal = 45


# In[86]:

salstot = 4 * cofsal


# In[88]:

sincofd.update({'Outlet': gusr})

sincofd.update({'Product': 'flatwhite'})

sincofd.update({'ID': 1000})
#Tags for this sale. 
sincofd.update({'tags': coftag})
#Sales count of that product
sincofd.update({'count': 45})
sincofd.update({'sales': salstot})


# In[89]:

sincofd


# In[72]:

#Need a list of coffee types
#and assign ID to each coffee.

