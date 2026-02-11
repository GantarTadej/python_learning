'''
import time
valid_dict = {"food": 100, "transport": 50}

try:
    invalid_dict = {["food", "eat"]: 100} 
except TypeError as e:
    print(f"Error: {e}")
# understanding_dict_keys.py

Will these work as dict keys?
test1 = {(1, 2, 3): "valid?"}           # Tuple of numbers
test2 = {("food", "jan"): "valid?"}      # Tuple of strings  
test3 = {([1, 2], 3): "valid?"}          # Tuple containing list
print(f"{test1(1,2,3)}")

# Test 1: Tuple of immutable objects
test1 = {(1, 2, 3): "works!"}
print(test1[(1, 2, 3)])  # What happens?

# Test 2: Tuple containing a list
test2 = {([1, 2], 3): "works?"}  # What happens here?

# understanding_dict_keys.py

print("=" * 50)
print("TEST 1: Tuple of numbers")
print("=" * 50)
try:
    dict1 = {(1, 2, 3): "test"}
    print("✓ SUCCESS - Tuple of numbers works as key")
    print(f"Value: {dict1[(1, 2, 3)]}")
except TypeError as e:
    print(f"✗ FAILED - {e}")

print("\n" + "=" * 50)
print("TEST 2: Tuple of strings")
print("=" * 50)
try:
    dict2 = {("food", "transport"): "test"}
    print("✓ SUCCESS - Tuple of strings works as key")
    print(f"Value: {dict2[('food', 'transport')]}")
except TypeError as e:
    print(f"✗ FAILED - {e}")

print("\n" + "=" * 50)
print("TEST 3: Tuple containing a list")
print("=" * 50)
try:
    my_list = [1, 2]
    dict3 = {(my_list, "test"): "value"}
    print("✓ SUCCESS - Tuple with list works as key")
except TypeError as e:
    print(f"✗ FAILED - {e}")

print("\n" + "=" * 50)
print("TEST 4: Nested tuples")
print("=" * 50)
try:
    dict4 = {((1, 2), (3, 4)): "nested tuples"}
    print("✓ SUCCESS - Nested tuples work as key")
    print(f"Value: {dict4[((1, 2), (3, 4))]}")
except TypeError as e:
    print(f"✗ FAILED - {e}")

print("\n" + "=" * 50)
print("CHALLENGE TESTS")
print("=" * 50)

print("\nTEST: key1 = (1, 2, [3, 4])")
try:
    test = {(1, 2, [3, 4]): "value"}
    print("✓ Works")
except TypeError as e:
    print(f"✗ Failed: {e}")

print("\nTEST: key2 = ((1, 2), (3, 4))")
try:
    test = {((1, 2), (3, 4)): "value"}
    print("✓ Works")
except TypeError as e:
    print(f"✗ Failed: {e}")

print("\nTEST: key3 = ([1, 2], [3, 4])")
try:
    test = {([1, 2], [3, 4]): "value"}
    print("✓ Works")
except TypeError as e:
    print(f"✗ Failed: {e}")

print("\nTEST: key4 = ({'a': 1}, 'test')")
try:
    test = {({"a": 1}, "test"): "value"}
    print("✓ Works")
except TypeError as e:
    print(f"✗ Failed: {e}")

print("\nTEST: key5 = (1, 2, (3, [4, 5]))")
try:
    test = {(1, 2, (3, [4, 5])): "value"}
    print("✓ Works")
except TypeError as e:
    print(f"✗ Failed: {e}")


# understanding_sets.py
import time

# Simulate 1000 expenses with 20 unique categories
expenses = [{"category": f"Cat{i % 20}"} for i in range(1000)]

# Method 1: Your current approach (using list)
start = time.time()
categories_list = []
for expense in expenses:
    if expense["category"] not in categories_list:  # This checks EVERY item
        categories_list.append(expense["category"])
time_list = time.time() - start

# Method 2: Using a set
start = time.time()
categories_set = set()
for expense in expenses:
    categories_set.add(expense["category"])  # Set handles duplicates automatically
time_set = time.time() - start

print(f"List approach: {time_list:.6f} seconds")
print(f"Set approach: {time_set:.6f} seconds")
print(f"Set is {time_list/time_set:.1f}x faster")
print(f"\nBoth found {len(categories_list)} categories")
'''
# understanding_set_operations.py

# Restaurant A sells these categories:
restaurant_a = {"Food", "Drinks", "Desserts", "Merchandise"}

# Restaurant B sells these:
restaurant_b = {"Food", "Drinks", "Entertainment", "Events"}

# Question 1: What do both restaurants sell?
both = restaurant_a & restaurant_b  # Intersection
print(f"Both sell: {both}")

# Question 2: What does only A sell?
only_a = restaurant_a - restaurant_b  # Difference
print(f"Only A sells: {only_a}")

# Question 3: What does either sell?
either = restaurant_a | restaurant_b  # Union
print(f"Either sells: {either}")

# Question 4: What's unique to each (not shared)?
unique = restaurant_a ^ restaurant_b  # Symmetric difference
print(f"Unique to each: {unique}")