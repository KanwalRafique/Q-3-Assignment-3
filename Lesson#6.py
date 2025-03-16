#-----------LESSON # 6 (LIST, TUPLES and DICTIONARY)-----------

# 1. Lists in Python
numbers = [3, 1, 4, 1, 5, 9]  # Creating a list
print("Original List:", numbers)

# Accessing List Elements
print("First Element:", numbers[0])  # Using index
print("Last Element:", numbers[-1])  # Using negative index

# Modifying Lists
numbers[2] = 7  # Changing value at index 2
print("Modified List:", numbers)

# List Slicing
print("Sliced List (index 1 to 3):", numbers[1:4])

# 2. Common List Methods
# Removing Elements
numbers.remove(1)  # Removes first occurrence of 1
print("After Removing 1:", numbers)

# Pop() Method
popped_value = numbers.pop()  # Removes last element
print("Popped Value:", popped_value)
print("After Pop:", numbers)

# Sorting a List
numbers = [3, 1, 4, 1, 5, 9]

# Default Sorting (Ascending Order)
sorted_numbers = sorted(numbers)  # Using sorted() to keep original list unchanged
print("Original List:", numbers)
print("Sorted List (Ascending Order):", sorted_numbers)

# Sorting in Descending Order
numbers.sort(reverse=True)
print("Descending Order:", numbers)

# Sorting by String Length
words = ["apple", "kiwi", "banana"]
words.sort(key=len)
print("Sorted by Length:", words)

# Sorting by Last Character
words.sort(key=lambda word: word[-1])
print("Sorted by Last Character:", words)

# Reversing a List
numbers = [1, 2, 5, 7, 10]
numbers.reverse()
print("Reversed List:", numbers)

# 3. Tuples in Python
tuple_example = (10, 20, 30, 40)  # Creating a tuple
print("Tuple:", tuple_example)
print("First Element of Tuple:", tuple_example[0])
# Tuples are immutable, so elements cannot be modified

# 4. Iterating Over Lists
# Using a for-loop
fruits = ["watermelon", "mango", "grape", "kiwi"]
for fruit in fruits:
    print(fruit)

# Using List Comprehension
squared = [x**2 for x in [1, 2, 3, 4, 5]]
print("Squared List:", squared)  # Output: [1, 4, 9, 16, 25]

filtered_squared = [x**2 for x in [1, 2, 3, 4, 5] if x > 3]
print("Filtered Squared List:", filtered_squared)  # Output: [16, 25]

# 5. Tuples in Python
# Creating Tuples
tuple1 = tuple(["apple", "banana", "cherry"])
tuple2 = (10, 20, 30)
mixed_tuple = ("hello", 42, 3.14, True)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Mixed Tuple:", mixed_tuple)

# Comparing Tuple Memory Addresses
tuple_1 = (10, 20, 30)
tuple_2 = (10, 20, 30)

print("Memory Address of tuple_1:", id(tuple_1))  
print("Memory Address of tuple_2:", id(tuple_2))  
print("Are tuples equal?", tuple_1 == tuple_2)  # True

# 6. Tuple Packing & Unpacking
packed_tuple = (1, 2, 3)
a, b, c = packed_tuple
print("Unpacked Values:", a, b, c)

# 7. Using enumerate() while Iterating Over Lists
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


#Python is a Type Hint Language**

### Type Hinting in Python


# Example of Type Hinting

a: int = input("Enter your name: ")
print(a, type(a))

## Dictionaries in Python

# Creating a dictionary
person: dict = {
    "name": "Alice",
    "age": 25,
    "visited_cities": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}
print(person)


#Using `dict()` constructor:
thisdict: dict = dict(name="John", age=36, country="Norway")
print(type(thisdict), "-", thisdict)

### Accessing Values

print(person["name"])  # Output: Alice
print(person.get("age", 99))  # Output: 25, returns 99 if not found
print(person.get("country", "Key not found"))  # Default value if key is missing

### Modifying a Dictionary

# Adding a new key-value pair
person["email"] = "alice@example.com"
# Modifying an existing value
person["age"] = 26
print(person)


### Deleting Items

# Using del
del person["visited_cities"]
# Using pop()
age: int = person.pop("age", -1)
print("Removed age:", age)
print(person)


### Dictionary Methods


#### Example:

print(person.keys())  # dict_keys(['name', 'email'])
print(person.values())  # dict_values(['Alice', 'alice@example.com'])
print(person.items())  # dict_items([('name', 'Alice'), ('email', 'alice@example.com')])

### Iterating Over a Dictionary

for key in person:
    print(key)

for key, value in person.items():
    print(key, ":", value)

### Practical Examples

#### Example 1: Building a Phonebook

phonebook: dict = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

name: str = input("Enter a name to search: ")
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}.")
else:
    print(f"{name} is not in the phonebook.")

#### Example 2: Counting Word Frequencies in a Text

sentence = "The quick brown fox jumps over the lazy dog. The dog barked."
word_counts: dict = {}

for word in sentence.lower().split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)


