
# coding: utf-8

# <h1>RevCoffee</h1>
# 
# <h3>Reverse Coffee Sales System</h3>
# 
# This is a script to create coffee sales data. 
# It uses the same base template as lcacoffee.ipnb.
# 
# Create a dict with coffee data in 
# 
# Sell a product = +1 to sales
# 
# Cash register base.
# 
# Hour, Daily, Monthly, Annual sales data of each item.
# 
# 10 cents, 20cents, 50cents, 1dollar, 2dollar,
# 5 dollar, 10 dollar, 20 dollar, 50 dollar, 100 dollar.
# 
# Point of sale open source project.

# In[ ]:




# In[1]:

import arrow
import os


# In[2]:

#I need it to return the day of the week it is.
#etc. Monday, Tuesday, Wednesday, Thursday


# In[3]:

arut = arrow.utcnow()


# In[4]:

cofdat = dict()


# In[5]:

#cofdat


# In[6]:

#Add a product.
yop = raw_input('add new product? y/n ')

if 'y' in yop:
    newprod = raw_input('Enter new product: ')

    strprod = str(newprod)
    #dicprod = dict
else:
    print 'not adding new product'


# In[7]:

yepz = raw_input('sell a product? y/n')
#input product type to sell.
if 'y' in yepz:
    lios = os.listdir('/home/wcmckee/sellcoffee/products/')
    print lios
    useprod = raw_input('Sell What? ')
    useprod


# In[8]:

#dict({"test": "again"})


# In[9]:

print arut.date()


# In[10]:

print arut.time()


# In[11]:

arut.weekday()


# In[12]:

cofdat.update({'Day': arut.weekday()})


# In[13]:

cofdat.update({'Date': str(arut.date())})


# In[14]:

print cofdat


# In[15]:

#for dayhr in range(24):
    #print dayhr
#    cofdat.update({dayhr: ' '})


# In[16]:

twenforst = arut.strftime('%H')


# In[17]:

twenforst


# In[18]:

lisprod = ('/home/wcmckee/sellcoffee/products/')


# In[52]:

os.listdir(lisprod)


# In[53]:

#Type in shortcuts for selecting items from list.
#id is code for what you can input in order to choose a
#product.


# In[20]:

opnumco = open('/home/wcmckee/sellcoffee/products/internet', 'r')

oprz = opnumco.read()


# In[21]:

#Need to +1 to this number 
salnumz = int(oprz) + 1


# In[22]:

salnumz


# In[23]:

savopnum = open('/home/wcmckee/sellcoffee/products/internet', 'w')

savopnum.write(str(salnumz))


# In[24]:

savopnum.close()


# In[25]:

cofdat.update({twenforst: salnumz})


# In[26]:

#cofdat.update({twenforst : numup


# In[69]:

cofdat


# In[70]:

cofdat.update({twenforst: 1})


# In[ ]:

#Get value [hour of the day] of key [amount sold]


# In[29]:

#Whats the point in creating keys for hours that don't
#get sales. Just get it to update with hour and add it

#Value is a database on the coffee sale. 
#Currently just numbers.


# In[30]:

print cofdat


# In[31]:

sincofd = dict()


# In[32]:

import getpass


# In[33]:

gusr = getpass.getuser()


# In[34]:

gusr


# In[35]:

#Outlet is username of sales person


# In[36]:

#Product is coffee name. 
#Open and read file that the customer asks
#for type of coffee. 
#Have a order folder that coffees are 
#qued into. 
#Sellcoffee folder
#Usernames - customers
#Staff - Staff list


# In[37]:

#opctype = open('/home/wcmckee/sellcoffee/usernames/')


# In[38]:

coftag = ('coffee, soymilk')


# In[39]:

idnum = 1000


# In[40]:

#Amount of coffee sales
cofsal = salnumz


# In[41]:

salstot = 4 * salnumz


# In[ ]:

#New product id will be os.listdir products len 
#1000 + products len
#This will increase by 1 each time a new product is added.
#Product ids start from 1000 or higher?


# In[56]:

amofp = len(os.listdir(lisprod))


# In[57]:

neidfp = (amofp + 1000)


# In[58]:

neidfp


# In[59]:

#Dict of new product created with this script. 
#Dict is stored with folder of product.
#Details on when product was first created
#It's name, ID, tags, sales counts.

sincofd.update({'Outlet': gusr})

sincofd.update({'Product': strprod})

sincofd.update({'ID': neidfp})
#Tags for this sale. 
sincofd.update({'tags': coftag})
#Sales count of that product
sincofd.update({'count': salnumz})
sincofd.update({'sales': salstot})


# In[60]:

sincofd


# In[61]:

#Need a list of coffee types
#and assign ID to each coffee.


# In[62]:

strprod


# In[63]:

savprod = open('/home/wcmckee/sellcoffee/products/' + strprod, 'w')

savprod.write('1')

savprod.close()


# In[64]:

#strzict = dict({'test':'again'})


# In[65]:

#strzict


# In[66]:

dictprod = dict()


# In[67]:

#Add internet. Adds computer time to a account.
dictprod.update({newprod: sincofd})


# In[68]:

print dictprod

