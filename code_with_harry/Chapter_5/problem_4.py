"""
Q. What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?
Ans: The length of set s will be 2, because first 20 and then 20.0 will be treated as same element,
but '20' will be treated as string. 

To verify this run this code. 
"""


s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?
print(len(s))