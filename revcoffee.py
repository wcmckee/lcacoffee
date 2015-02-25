
# coding: utf-8

# This is a script to create coffee sales data. 
# It uses the same base template as lcacoffee.ipnb.
# 
# Create a dict with coffee data in 
# 
# Sell a product = +1 to sales
# 
# Cash register base.
# 
# 10 cents, 20cents, 50cents, 1dollar, 2dollar,
# 5 dollar, 10 dollar, 20 dollar, 50 dollar, 100 dollar.
# 
# Point of sale open source project.

# In[222]:




# In[223]:

import arrow
import os


# In[224]:

#I need it to return the day of the week it is.
#etc. Monday, Tuesday, Wednesday, Thursday


# In[225]:

arut = arrow.utcnow()


# In[226]:

cofdat = dict()


# In[227]:

#cofdat


# In[229]:

#Add a product.
newprod = raw_input('Enter new product: ')

strprod = str(newprod)
#dicprod = dict()


# In[230]:

#dict({"test": "again"})


# In[231]:

print arut.date()


# In[232]:

print arut.time()


# In[233]:

arut.weekday()


# In[234]:

cofdat.update({'Day': arut.weekday()})


# In[235]:

cofdat.update({'Date': str(arut.date())})


# In[236]:

print cofdat


# In[237]:

#for dayhr in range(24):
    #print dayhr
#    cofdat.update({dayhr: ' '})


# In[238]:

twenforst = arut.strftime('%H')


# In[239]:

twenforst


# In[240]:

lisprod = ('/home/wcmckee/sellcoffee/products/')


# In[241]:

os.listdir(lisprod)


# In[242]:

opnumco = open('/home/wcmckee/sellcoffee/products/internet', 'r')

oprz = opnumco.read()


# In[243]:

#Need to +1 to this number 
salnumz = int(oprz) + 1


# In[244]:

salnumz


# In[245]:

savopnum = open('/home/wcmckee/sellcoffee/products/internet', 'w')

savopnum.write(str(salnumz))


# In[246]:

savopnum.close()


# In[247]:

cofdat.update({twenforst: salnumz})


# In[248]:

#cofdat.update({twenforst : numup


# In[249]:

cofdat


# In[250]:

cofdat.update({twenforst: 1})


# In[251]:

#Whats the point in creating keys for hours that don't
#get sales. Just get it to update with hour and add it

#Value is a database on the coffee sale. 
#Currently just numbers.


# In[252]:

print cofdat


# In[253]:

sincofd = dict()


# In[171]:

import getpass


# In[172]:

gusr = getpass.getuser()


# In[173]:

gusr


# In[174]:

#Outlet is username of sales person


# In[175]:

#Product is coffee name. 
#Open and read file that the customer asks
#for type of coffee. 
#Have a order folder that coffees are 
#qued into. 
#Sellcoffee folder
#Usernames - customers
#Staff - Staff list


# In[176]:

#opctype = open('/home/wcmckee/sellcoffee/usernames/')


# In[190]:

coftag = ('coffee, soymilk')


# In[ ]:

idnum = 1000


# In[178]:

#Amount of coffee sales
cofsal = salnumz


# In[179]:

salstot = 4 * salnumz


# In[180]:

sincofd.update({'Outlet': gusr})

sincofd.update({'Product': strprod})

sincofd.update({'ID': 10001})
#Tags for this sale. 
sincofd.update({'tags': coftag})
#Sales count of that product
sincofd.update({'count': salnumz})
sincofd.update({'sales': salstot})


# In[181]:

sincofd


# In[182]:

#Need a list of coffee types
#and assign ID to each coffee.


# In[186]:

strprod


# In[198]:

savprod = open('/home/wcmckee/sellcoffee/products/' + strprod, 'w')

savprod.write('1')

savprod.close()


# In[187]:

#strzict = dict({'test':'again'})


# In[188]:

#strzict


# In[188]:

dictprod = dict()


# In[189]:

#Add internet. Adds computer time to a account.
dictprod.update({newprod: sincofd})


# In[107]:

print dictprod

