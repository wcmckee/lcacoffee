
# coding: utf-8

# <h1>Product Add</h1>
# 
# Script to add a new product to list of them. Location is /home/wcmckee/sellcoffee/products.
# 
# Better to have a file for products or a folder? Might be easier to have a folder.
# Each product has rsa key - public and private key.
# 

# In[31]:

import os
#from passlib.hash import pbkdf2_sha256
#import crypt, getpass, spwd
#from Crypto.PublicKey import RSA


# In[32]:

prodirz = ('/home/wcmckee/sellcoffee/products/')


# In[33]:

prolis = os.listdir(prodirz)


# In[34]:

print prolis


# In[35]:

prodoadd = raw_input('Name of product to add: ')


# In[36]:

prodirc = (prodirz + prodoadd)


# In[37]:

os.mkdir(prodirc)


# In[42]:

opmeta = open(prodirc + '/' +  prodoadd + '-amount', 'w')

opmeta.write('0')

opmeta.close()


# In[38]:

#switching to folders for each product. Inside folder has rsa
#and rsa.public.


# In[39]:

#opnewp = open(prodirz + prodoadd, 'w')

##opnewp.write('0')


# In[43]:

#new_key = RSA.generate(2048, e=65537)
#public_key = new_key.publickey().exportKey("PEM")
#private_key = new_key.exportKey("PEM")
#print private_key 
#sapriv = open(prodirc + '/' + prodoadd, 'w')
#sapriv.write(private_key)
#sapriv.close()

#print public_key 
#papriv =  open(prodirc + '/' +  prodoadd + '.pub', 'w')
#papriv.write(public_key)
#papriv.close()


# In[41]:

#dict that has all the product details. When it was first
#created. Price. 
#amount sold. This value will be zero when a product is created
#but add 1 with productsell script. 
#Store amount sold data in dict
#or just a file called productname-amountsold.


# In[ ]:




# In[ ]:

#opnewp.close()


# In[11]:

#for prol in prolis:
#    print prol
#    adprod = open(prodirz + prol + '.meta', 'w')
#    adprod.write(


# In[ ]:




# In[ ]:


#adprod = open(pro


# In[ ]:



