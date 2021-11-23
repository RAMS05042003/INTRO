#!/usr/bin/env python
# coding: utf-8

# In[1]:


### wile loop
# print the numbers presnet in a range reverse order
# from upper bound to lower bound
up,lw=int(input("uppper bound")),int(input("lower bound"))
for num in range(up,lw,-1):
    print(num,end=' ')


# In[2]:


up,lw=int(input("uppper bound")),int(input("lower bound"))
for num in range(up,lw,-2):
    print(num,end=' ')


# In[4]:


# multiplication table in reverse order
n= int(input())
for num in range(10,0,-1):
    print(n,"x",num,"=",n*num)
    


# ### while loop
# - condition base iteration
# - developer/programer has to initiate the iterator first
# - user incrementation
# - **syntax**
#      - while condition
#          - statement goes here

# In[ ]:


it=1
while it<=10:
    print(it,end=' ')
    it+=1


# In[ ]:




