
# coding: utf-8

# Setup Raspberry Pi
# 
# Script used on freshly installed raspbrien install on a Raspberry Pi.
# Installs IPython Notebook
# Gets .ssh folder from local server
# Copy folders from local server.
# Home, Github code, sellcoffee,
# 
<<<<<<< HEAD
=======
# .gimp-2.8
# .ipython
# 
# 
>>>>>>> 33339176764b46364df5f23a3c832970688bf476
# Install Python script requirments
# (pip arrow/praw/requests etc).
# Install from local server
# 
<<<<<<< HEAD
# 

# In[1]:
=======
# Get public ssh key from local web server that allows remote machine to ssh into new pi and copy req folders.
# 
# copy interfaces file accross - and assign a 
# new number. Also create new colour hostname.
# 
# How hostnames work.
# Dict that has all current hostnames with their static ip.
# Dict that has all future hostnames with their static ip.
# 
# when new machine added remove hostname/static ip from future hostnames and add to current hostnames.
# 
# 32 - zinkwhite
# 33 - corlsbudcayon
# 34 - naplesyellow
# 35 - etc..
# 
# Need to get a colour generator script.
# 
# 

# In[ ]:




# In[394]:
>>>>>>> 33339176764b46364df5f23a3c832970688bf476

#ssh into the pi and start doing commands.


<<<<<<< HEAD
# In[2]:

import shutil


# In[3]:

import os
=======
# In[446]:

import shutil
import colourlovers
import os
from colourlovers import ColourLovers
import requests
import json


# In[ ]:




# In[396]:

#from colourlovers import ColourLovers
#cl = ColourLovers()
#cl.color('#37cbff')
#c = ColourLovers


# In[397]:

cl = ColourLovers()
#Better to go with the random. Need to generate 
#liscolor = cl.colors('top', numResults=50, result_offset=50)
liscolor = cl.colors('random')


# In[398]:

hostnamecolor = list()


# In[399]:

#From the examples - get the hex num. fill image with color. save.

#from PIL import Image


#im = Image.open("/home/wcmckee/test.jpg")


# In[400]:

#os.chdir('/home/wcmckee/colortest/')


# In[401]:

#Image.new('RGB', (100,100), color=lisc.hex)#


# In[402]:

colordict = dict()


# In[403]:

urld = dict()


# In[404]:

for lisc in liscolor:
    print lisc.title
    #myimg = Image.new('RGB', (100,100), color=lisc.hex)
#    myimg.save('/home/wcmckee/colortest/' + (lisc.title), format='png')
    print lisc.hsv
    print lisc.description
    colordict.update({'title' : lisc.title, 'description' : lisc.description})
    colordict.update({'hex' : lisc.hex})
    urld.update({'url' : lisc.url})
    
    
    hostnamecolor.append(lisc.title)


# In[405]:

print colordict.values()


# In[406]:

#print colordict['url']


# In[407]:

hoslisf = []
repls = []
lowlisf = []


# In[408]:

for mec in hostnamecolor:
    #mec.replace(' ', '-')
    mec.replace(' ', '-')
    hoslisf.append(mec.replace(' ', '-'))


# In[409]:

for hosz in hoslisf:
    lowlisf.append(hosz.lower())
    print hosz
    


# In[452]:

for hosa in lowlisf:
    print hosa
    repls.append(hosa.replace("'", ''))
    colordict.update({'ftitle' : hosa})
    


# In[411]:

repls


# In[463]:

os.chdir('/home/wcmckee/colortest/')


# In[464]:

res = requests.get(urld['url'], stream=True)

with open(str(colordict['title'].replace(' ', '-')) + '.png', 'wb') as outfil:
    shutil.copyfileobj(res.raw, outfil)
    del res


# In[465]:

lowlisf


# In[414]:

colordict.update({'locurl' : ('/home/wcmckee/colortest/' + colordict['title'].replace(' ', '-')) + '.png'})


# In[415]:

colordict


# In[416]:

#from IPython.display import Image
#Image(filename= colordict['locurl'])


# In[417]:

sthex = colordict['hex'].replace('#', '')


# In[418]:

sthex


# In[419]:

intens = []
absens = []
midtens = []


# In[420]:

for schr in sthex:
    print schr, schr.isalpha()
    #if schr == 
    if schr.isalpha():
        intens.append(schr)


# In[421]:

intens


# In[422]:

for schr in sthex:
    print schr, schr.isdigit()
    if schr.isdigit():
        absens.append(schr)


# In[423]:

for rabse in absens:
    print rabse
    if int(rabse) >= 5:
        #print 'mid
        print 'mid'
        midtens.append(rabse)
        
        


# In[458]:

lownumza = []


# In[459]:

for rabse in absens:
    print rabse
    if int(rabse) <= 5:
        #print 'mid
        print 'low'
        lownumza.append(rabse)


# In[424]:

print absens


# In[425]:

for mit in midtens:
    print mit


# In[426]:

#absenc = set(absens) - set(midtens)


# In[427]:

#absenc


# In[428]:

#midlis = list(absenc)


# In[429]:

leabs = len(lownumza)
leints = len(intens)
lemid = len(midtens)


# In[439]:

#leabs
colordict.update({'absens-num' : leabs, 'midsens-num' : lemid})


# In[460]:

leabs


# In[461]:

lemid


# In[462]:

leints


# In[441]:

colordict.update({'intense-num' : leints})


# In[442]:

midtens


# In[443]:

if leabs < leints:
    print 'intense'
    print leints
    colordict.update({'generalfeel' : 'intense'})


# In[ ]:




# In[444]:

if leabs > leints:
    print 'absense'
    print leabs
    colordict.update({'generalfeel' : 'absense'})


# In[453]:

colordict


# In[454]:

jsnfil = json.dumps(colordict)


# In[455]:

jsnfil


# In[457]:

opjsf = open('/home/wcmckee/colortest/' + colordict['ftitle'] + '.json', 'w')
opjsf.write(jsnfil)
opjsf.close()


# In[471]:

#prehost = '192.168.1.'
#lisofip = []


# In[ ]:

#These are all the ip addresses i want to dish out.
#address is in a file and when assigned to a new
#hostmachine, the address is removed. 

#Lets do it now. 


# In[494]:

#opipfza = open('/home/wcmckee/colortest/freeip.txt', 'w')
#opipfza.write(str(lisofip))


# In[ ]:




# In[495]:

#for lispo in lisofip:
#    print lispo
#    opipfza.write(str(lispo))
#    opipfza.write('\n')


# In[496]:

#opipfza.close()


# In[497]:

#for hosips in range(130,180):
#    print prehost + str(hosips)
#    lisofip.append(prehost + str(hosips))


# In[ ]:




# lookup hex code and tell me what color it is

# In[4]:

#Fetches home dir from local server backup.
#This is the backup pi. 

#os.system('rsync -azP wcmckee@192.168.1.8:/home/ /home/')
>>>>>>> 33339176764b46364df5f23a3c832970688bf476


# In[ ]:

<<<<<<< HEAD
os.chdir('/home/wcmckee/ipython/')
=======
#os.chdir('/home/wcmckee/ipython/')
>>>>>>> 33339176764b46364df5f23a3c832970688bf476


# In[ ]:

<<<<<<< HEAD
os.system('sudo python setup.py install')
=======
#s.system('sudo python setup.py install')
>>>>>>> 33339176764b46364df5f23a3c832970688bf476

