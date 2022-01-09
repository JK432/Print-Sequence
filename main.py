# Write a Python program to print
# A
# B B 
# C C C 
# D D D D 
# E E E E E
j=1
while j<6:
  for i in ['A','B','C','D','E']:
    d=(i+" ")*j
    e=str(d)
    print(e[:len(e)-1])
    j=j+1