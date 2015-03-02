
# coding: utf-8

# <h1>Product Sell</h1>
# 
# <h3>Script to sell a product.</h3> 
# 
# Gets products list from /sellcoffee/products folder.
# input what to sell. 
# or input 4 digit code of product.
# 
# Input amount of product to sell
# 
# Processes the sale, increasing number of product filename
# by input amount to sell.
# 
# Creates dict of sale, includes time, date, product (inputed data), amount (inputed sales amount), 
# served by, hostname of machine that processed transaction, 
# e receipts. 
# 

# In[109]:

import os
import arrow
import json


# In[110]:

prodir = ('/home/wcmckee/sellcoffee/products/')


# In[111]:

lsprod = os.listdir(prodir)


# In[112]:

print lsprod


# In[80]:

sellwhat = raw_input('Sell what: ')


# In[81]:

#Open the file up and increase the sale number by one.

selinp = open(prodir + sellwhat, 'r')

cursal = selinp.read()

selinp.close()


# In[82]:

conint = int(cursal)


# In[83]:

#1 is amount to sell. Maybe raw_input enter int to sell more
#than one

amounsel = raw_input('Amount to sell: ')
amount = int(amounsel)
newintz = conint + amount


# In[84]:

newintz


# In[115]:

fildir = (prodir + sellwhat + '/' + sellwhat + '-amount') 


# In[116]:

fildir


# In[ ]:




# In[118]:

sewha = open(fildir, 'w')

sewha.write(str(newintz))

sewha.close()


# In[86]:

opfolaz = open('/home/wcmckee/sellcoffee/products/' + sellwhat, 'r')

print opfolaz.read()


# In[87]:

opfolaz.close()


# In[88]:

#Need to report back by updating dict() of 24 hour value
#that sale is +. 

#Dict that is recect of current sale. Name of product, amount.
#Cost * amount.
#Paid by cash, eftpos, credit card etc...
#Change to be given.


# In[89]:

locdict = dict()


# In[90]:

autc = arrow.utcnow()


# In[91]:

hrsaledict = dict()


# In[92]:

authr = autc.strftime('%H')


# In[93]:

aumin = autc.strftime('%M')


# In[94]:

ausec =autc.strftime('%S')


# In[95]:

str(autc.date())


# In[96]:

auall = authr + aumin + ausec


# In[97]:

auall


# In[98]:

hrsaledict.update({auall : amount})


# In[99]:

locdict.update({'product' : sellwhat, 'amount' : amount, 'time': auall, 'date': str(autc.date())}) 


# In[105]:

lcojson = json.dumps(locdict)


# In[106]:

lcojson


# In[108]:

os.urandom(7)


# In[ ]:




# In[ ]:

#salcoj = open('/home/wcmckee/sellcoffee/archive/') 


# In[101]:

print hrsaledict


# In[102]:

#7 character unique id for each transaction
#More than 1 product type sale transaction.


# In[75]:

#Add another product? Y/n Question after the amount of product.
#


# In[ ]:



