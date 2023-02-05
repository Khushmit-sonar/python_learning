##set - collection of unique values
##same value not occure in the set twice.

# create the empty set

s = set()

 ##add element to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s) ##op -- {1, 2, 3, 4}

##we can remove element from set

s.remove(2)
print(s) ## {1, 3, 4} || 2 has been removed


##len is used to calculate the length of list , set,  etc

print(f"The set had {len(s)} elements.")  ##op-- The set had 3 elements.