#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a function that takes a string and returns the numberof words in it.


# In[5]:


sentence = "This is a python selenium class"
words = len(sentence.split())
print("Number of words:", words)


# In[ ]:


# Write a function that takes a string and returns True if it is an anagram of another string,False otherwise.


# In[5]:


def isAnagram(a, b):  
    
    if len(a) != len(b): #Unequal Length strings cannot be anagrams
        return False
    
    
    first = sorted(a) #sort the first string
    
    second = sorted(b) #sort the second string
    
    
    if first == second: #check if both the strings are the same
        return True
    else:
        return False
    

ans = isAnagram("sleep","plsee") #driver code
print(ans)


# In[7]:


# Write a function that takes a string and returns the most frequent character in it.


# In[18]:


test_str = "OOty is tourist place"
res = max(test_str, key=lambda x: test_str.count(x))
print(res)


# In[ ]:


# Write a function that takes two strings and returns the longest common substring between them.


# In[33]:


def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer

print(longestSubstringFinder("blocked","blockses"))
print(longestSubstringFinder("wind", "winter"))


# In[ ]:


# Write a function that takes a string and returns True if it is a palindrome,False otherwise.


# In[38]:


def isPalindrome(s):
    return s == s[::-1]
 
s = "level" # Driver code
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


# In[ ]:


# Write a function that takes a string and returns the number of unique characters in it.


# In[44]:


# Python program to count the number of distinct
# characters present in the string str
S = "PythonClass"
a = ""
for i in S:
    if i not in a:
        a += i
print(len(a))


# In[ ]:


# Write a funtion that takes a string and returns a new string with all the vowels removed.


# In[46]:


string = "Sahil is small boy"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]

print("\nAfter removing Vowels: ", result)


# In[ ]:


# Create a pyramid of numbers from 1 to 20 using for loop.


# In[60]:


n = 20
num = [1,20]
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(chr(num), end=" ")
        num += 1
    num = [1-20]
    print()


# In[ ]:


# Write 


# In[ ]:





# In[ ]:




