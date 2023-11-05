#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Write a Python program using Function to which will do the following:-
    #a) The function will create a text file with the current timestamp.
    #b) The file content should have the content of the current timestamp.

import datetime

def createfile():
    currtime = datetime.datetime.now()
    print(currtime)
    with open("timenow.txt", 'w') as file:
        file.write (str(currtime))

createfile()


# In[2]:


#2) Write another Python function to read from a textfile.The function will take the name of the text file and display
# the content of the file into the console.

f=open(r"C:\Users\sahbi\filehandling\file3.txt.","r")
f.read()


# In[ ]:





# In[ ]:




