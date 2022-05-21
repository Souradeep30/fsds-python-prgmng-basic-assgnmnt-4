#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer 1
num = int(input("Enter a number: "))

ref = 1
for i in range(num, 0, -1):
   ref = ref*i
    
print("\nFactorial of {}: {}".format(num, ref))


# In[2]:


#Answer 2
num = int(input("Enter a number: "))

for i in range(1, 11):
    print("{} x {} = {}".format(num, i, num*i))


# In[3]:


#Answer 3
fibo_length = int(input("Enter a length: "))

a = 0
b = 1
print(a, end = ' ')
print(b, end = ' ')
while(fibo_length-2 > 0):
    nt = a + b
    print(nt, end = ' ')
    a = b
    b = nt
    
    fibo_length -= 1


# In[4]:


#Answer 4
import math


# In[5]:


def fibo_check(num):
    l = len(str(num))  ## l = number of digits of number
    sum1 = 0 
    temp_num = num
    while(num > 0):
        d = num % 10
        sum1 += int(math.pow(d, l))
        num = num // 10

    if(sum1 == int(temp_num)):
        return 1
    else:
        return 0


# In[8]:


num = int(input("Enter a number: "))

if(fibo_check(num)):
    print("{} is an armstrong number".format(num))
else:
    print("{} is not an armstrong number".format(num))


# In[9]:


#Answer 5
low = int(input("Enter the lower value of range: "))
high = int(input("Enter the higher value of range: "))

print("\nFrom {} to {} following are the Armstrong Number:".format(low, high), end='\n')
for i in range(low, high+1):
    
    if(fibo_check(i)):
        print(i, end = ' ')


# In[10]:


#Answer 6
num = int(input("Enter a positive number: "))

total_sum = 0
for i in range(1, num+1):
    total_sum += i
    
print("Sum of {} natural number is {}".format(num, total_sum))


# In[ ]:




