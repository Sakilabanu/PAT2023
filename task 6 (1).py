#!/usr/bin/env python
# coding: utf-8

# In[3]:


# You have been given Python List[10,501,22,37,100,999,87,351] your task is to create two List one
# which have all the Even Numbers and another List which will have all the ODD numbers in it?

import numpy as np

list1 = np.array([10,501,22,37,100,999,87,351])

only_odd = list1[list1 % 2 == 1]

print(only_odd)

only_even = list1[list1 % 2 == 0]

print(only_even)



# In[8]:


# Given a Python List [10,501,22,37,100,999,87,351] your task is to Count all the Prime Numbers and create a new Python List
# which willcontain all the  Prime Numbers in it?

mylist =[10,501,22,37,100,999,87,351]
prime =[]
for i in mylist :
    c=0
    for j in range(1,i):
        if i%j ==0:
            c+=1
    if c==1:
            prime.append(i)
print(prime)



# In[6]:


# Given a Python List [10,501,22,37,100,999,87,351] Find out how many numbers are there in the given Python List
# which are Happy numbers?
a = [10,501,22,37,100,999,87,351]
b = []
def happy(a):
    for i in range (len(a)):
        sum = a[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2
                sum = tempsum        
            if sum == 1:
                b.append(a[i])
    return b
print(happy(a))


# In[5]:


# Write a python program to find the sum of the first and last digit of an integer?

number = 3456

number = str(number)

first_digit = int(number[0])

last_digit = int(number[-1])

addition = first_digit + last_digit

print('Addition of first and last digit of the number is',   addition)



# In[33]:


# You have been given a list of N integers which represents the number of Mangoes in a bag. Each bag has a variable
# numbers of Mangoes. There are M students in a Guvi class.your task is to distribute the Mangoes in such a way 
# that each student gets one Bag. The difference between the number of Mangoes in a bag with maximum Mangoes and Bags
# with minimum Mangoes givento the student is minimum?

def man(n, m):
    res = 1
 
    if m > n - m:
        m = n - m
 
    for i in range(0, m):
        res *= (n - i)
        res /= (i + 1) 
 
    return res
 
# helper function for generating no of ways
# to distribute n mangoes amongst m student
def calculate_ways(n, m):
 
    # not enough mangoes to be distributed    
    if n<m:
        return 0
 
    # ways  -> (m + n-1)C(m-1)
    ways = man(m + n-1, m-1)
    return int(ways)
 
# Driver function
if __name__ == '__main__':
 
    # n represents number of mangoes 
    # m represents number of people
    n = 7 ;m = 5
 
    result = calculate_ways(n, m)
    print(result)


# In[25]:


# You have been three lists. Your task is to find the duplicates in the three lists. Write a python program for the same.
# You can use your own python lists?

def Intersecofsets(arr1, arr2, arr3):
     common = list(filter(lambda x: x in arr2 and x in arr3, arr1))
     print(common)

arr1 = [1, 5, 10, 20, 80, 50]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 50, 70, 80]

Intersecofsets(arr1, arr2, arr3)


# In[18]:


# Write a Python program to find the first non-repeating elements in a given list of integers?

def count(arr, n):


   visited = [False for i in range(n)]

    
   for i in range(n):

    
     if (visited[i] == True):
        continue

     
     count = 1
     for j in range(i + 1, n, 1):
        if (arr[i] == arr[j]):
          visited[j] = True
          count += 1
     if count == 1 :
        print(arr[i]);
   


arr = [10, 30, 40, 20, 10, 20, 50, 10]
n = len(arr)
count(arr, n)


# In[21]:


# Write a python program to find the minimum element in a rated and sorted list?

list1 = [21, 67, 3, 98]

list1.sort()

print("Smallest element is:", list1[0])


# In[22]:


# You have been given a python list[10,20,30,9] and a value of 59. Write a python program to find the triplet in the list 
# whose sum is equal to the given value?


from itertools import combinations
 
def findTriplets(lst, key):
     
    def valid(val):
        return sum(val) == key
         
    return list(filter(valid, list(combinations(lst, 3))))
 
lst = [10,20,30,9]
print(findTriplets(lst, 59))


# In[12]:


# Given a list[4,2,-3,6] write a python to find if there is a sub-list with sum equal to zero?


def subArray(arr, l):
    for i in range(l - 1):
        s = arr[i]
        for j in range(i + 1, l):
            s += arr[j]
            if s == 0:
                return True
    return False


array = [4, 2, -3, 1, 6]

print(subArray(array, len(array)))
        
      


# In[ ]:





# In[ ]:




