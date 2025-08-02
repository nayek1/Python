a = (1,22,5,3,4,5)
print(a)
no = a.count(5) # Count the number of times 5 appears in the tuple
print(no)

i = a.index(5) # Find the index of the first occurrence of 5
print(i)

# Concatenation

a = (1,2,3) 
b = (4,5,6)
c = a + b # Concatenate the two tuples
print(c)

# Repetition
a = (1,2,3) 
b = a * 3 # Repeat the tuple 3 times
print(b)

# Slicing
a = (1,2,3,4,5,6)
b = a[1:4] # Slice the tuple from index 1 to 4
print(b)

# Length
a = (1,2,3,4,5)
b = len(a) # Find the length of the tuple
print(b)

#Operators
a = (1,2,3)
print(2 in a) # Check if 2 is in the tuple
print(2 not in a) # Check if 2 is not in the tuple  


# Unpacking
a = (1,2,3)
x, y, z = a # Unpack the tuple into variables x, y, z
print(x, y, z)

# Nested tuple
a = (1,2,3,(4,5,6))
print(a) # Print the nested tuple
print(a[3]) # Print the nested tuple at index 3
print(a[3][1]) # Print the element at index 1 of the nested tuple

# Nested tuple with different data types
a = (1,2,3,(4,5,6), "sagar", [1,2,3])   
print(a) # Print the nested tuple with different data types
print(a[3]) # Print the nested tuple at index 3

# Sorted tuple
t = (9, 8, 7, 6, 5, 4, 3, 2, 1)
sorted_tuple = sorted(t) # Sort the tuple in ascending order
print(sorted_tuple) # Print the sorted tuple

# Touple Constructors
lst = [1, 2, 3, 4, 5]
t = tuple(lst) # Convert the list to a tuple
print(t) # Print the tuple