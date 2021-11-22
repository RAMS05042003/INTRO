#!/usr/bin/env python
# coding: utf-8

# In[2]:


a,b,c=int(input()),int(input()),int(input())
if(a<b and a<c):
    print(" smallest",a)
elif(b<a and b<c):
    print("the smallest",b)
else:
    print("the smallest",c)


# In[7]:


year= int(input())
if(year%4==0 and year%100!=0):
    print("leap year")
elif(year%400==0):
    print("leap year")
else:
    print("not a leap year")
    


# In[10]:


# to print numbers from 1 to 10


# In[16]:


a=1
i=0
for a in range(a,10):
    print(a)


# In[18]:


for a in range(10,100,2):
    print(a)


# In[38]:


n = int(input())
for num in range (n,n*10,n):
    print(n ,"x" ,num ,"=",n*num)
    


# In[ ]:




