# LESSON # 7 (The Set and Frozen Set)

# Creating sets
my_set = {123, 452, 5, 6}
my_set2 = set([123, 452, 5, 6])
print("my_set:", my_set)
print("my_set2:", my_set2)
print("Are both sets equal?", my_set == my_set2)

# Attempting to store a mutable object (list) in a set - This will raise an error
try:
    my_set_error = {[123, 452, 5, 6]}
except TypeError as e:
    print("Error:", e)

# Set with multiple data types
multi_type_set = {7, 9.0, False, True, "Hello! World", (1, 5, 9, 'hi')}
print("multi_type_set:", multi_type_set)

# Sets are unordered
set2 = {'Java', 'Python', 'JavaScript', 'java'}
print("Unordered set:", set2)

# Attempting to modify a set element
my_set = {1, 2, 3, 4, 5}
try:
    my_set[0] = 10
except TypeError as e:
    print("Set modification error:", e)

# Removing elements
my_set.remove(3)
my_set.discard('A')  # No error if 'A' is not found
print("Set after removal:", my_set)

# Adding elements
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing multiple elements using difference_update()
my_set.difference_update({1, 5})
print("Set after difference_update:", my_set)

# Union of two sets
set_a = {1, 2, 3, 5}
set_b = {1, 5, 6, 7}
set_union = set_a | set_b  # Using '|' operator
print("Union of sets:", set_union)

# Ensuring uniqueness
my_set.add(2)
my_set.add("Hello! World")
print("Set after attempting to add duplicates:", my_set)

# Popping an element (removes arbitrary element)
print("Before pop():", my_set)
my_set.pop()
print("After pop():", my_set)


# Demonstrating Hashing and Set Behavior in Python

a: str = "Hello! World"
b: str = "Hello! World"

print("id(a) =", id(a))
print("id(b) =", id(b))
print("hash(a) =", hash(a))
print("hash(b) =", hash(b))
print("a.__hash__() =", a.__hash__())

# Attempting to use a set as a dictionary key (will raise an error)
try:
    my_set = {1, 2, 3, 4, 5, "Hello! World"}
    my_dict = {my_set: "Hello! World"}
except TypeError as e:
    print("Error:", e)

# Demonstrating how set order changes dynamically
my_set = {10, 3, 5, 8}
print("Initial set:", my_set)

my_set.add(20)
print("After adding 20:", my_set)

my_set.remove(10)
print("After removing 10:", my_set)

# Demonstrating frozenset
my_frozenset = frozenset([1, 2, 3, "Hello! World"])
print("my_frozenset:", my_frozenset)

# Demonstrating Set Methods
set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3, "Hello! World", 8, 9}

print("difference():", set1.difference(set2))
print("intersection():", set1.intersection(set2))
print("union():", set1.union(set2))
print("symmetric_difference():", set1.symmetric_difference(set2))
print("isdisjoint():", set1.isdisjoint(set2))
print("issuperset():", set1.issuperset(set2))
print("issubset():", set2.issubset(set1))
