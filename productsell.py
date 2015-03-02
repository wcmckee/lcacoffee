
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

# In[121]:

import os
import arrow
import json


# In[122]:

prodir = ('/home/wcmckee/sellcoffee/products/')


# In[123]:

lsprod = os.listdir(prodir)


# In[124]:

print lsprod


# In[125]:

sellwhat = raw_input('Sell what: ')


# In[135]:

fpathz = (prodir + sellwhat + '/' + sellwhat + '-amount')


# In[136]:

fpathz


# In[137]:

#Open the file up and increase the sale number by one.

selinp = open(fpathz, 'r')

cursal = selinp.read()

selinp.close()


# In[139]:

print cursal


# In[138]:

conint = int(cursal)


# In[140]:

#1 is amount to sell. Maybe raw_input enter int to sell more
#than one

amounsel = raw_input('Amount to sell: ')
amount = int(amounsel)
newintz = conint + amount


# In[141]:

newintz


# In[142]:

fildir = (prodir + sellwhat + '/' + sellwhat + '-amount') 


# In[143]:

fildir


# In[143]:




# In[144]:

sewha = open(fildir, 'w')

sewha.write(str(newintz))

sewha.close()


# In[145]:

opfolaz = open(fildir, 'r')

print opfolaz.read()


# In[146]:

opfolaz.close()


# In[147]:

#Need to report back by updating dict() of 24 hour value
#that sale is +. 

#Dict that is recect of current sale. Name of product, amount.
#Cost * amount.
#Paid by cash, eftpos, credit card etc...
#Change to be given.


# In[148]:

locdict = dict()


# In[149]:

autc = arrow.utcnow()


# In[150]:

hrsaledict = dict()


# In[151]:

authr = autc.strftime('%H')


# In[152]:

aumin = autc.strftime('%M')


# In[153]:

ausec =autc.strftime('%S')


# In[154]:

str(autc.date())


# In[155]:

auall = authr + aumin + ausec


# In[169]:

fzaq = (str(autc.date()) + '-' + auall)


# In[170]:

fzaq


# In[157]:

hrsaledict.update({auall : amount})


# In[158]:

locdict.update({'product' : sellwhat, 'amount' : amount, 'time': auall, 'date': str(autc.date())}) 


# In[159]:

lcojson = json.dumps(locdict)


# In[160]:

lcojson


# In[161]:

os.urandom(7)


# In[ ]:

fzaq


# In[ ]:

salcoj = open('/home/wcmckee/sellcoffee/archive/' + fzaq + '.json', 'w')

salcoj.write(lcojson)

salcoj.close()


# In[101]:

print hrsaledict


# In[102]:

#7 character unique id for each transaction
#More than 1 product type sale transaction.


# In[75]:

#Add another product? Y/n Question after the amount of product.
#


# In[ ]:



