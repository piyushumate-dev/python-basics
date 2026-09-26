# It demonstrate the use of set in python.
collection={1, 2, 3, "Hello", "World"}
print(collection)
print(len(collection))

# repeated values is ignored in sets,
collection={1, 2, 3, 3, 3, "Hello", "Hello", "World"}
print(collection)
print(len(collection))
print(type(collection))

# Set Methods.
collection={1, 2, 3, 3, 3, "Hello", "Hello", "World"}

# 1] set.add(el)
collection.add(4)
print(collection)

# 2] set.remove(el)
collection.remove(4)
print(collection)

# 3] set.clear()
collection.clear()
print(collection)

# 4] set.pop()
collection={1, 2, 3, 3, 3, "Hello", "Hello", "World"}
print(collection.pop())

# 5] set1.union(set2)
set1={1, 2, 3}
set2={2, 3, 4}
print(set1.union(set2))

# 6] set1.intersection(set2)
print(set1.intersection(set2))

