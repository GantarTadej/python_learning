import sys
import time

#Byte allocations Python
'''
my_list = []
print(f'Empty list size: {sys.getsizeof(my_list)} bytes')

for i in range(100):
    my_list.append(i)
    print(f'After adding {i}: size = {sys.getsizeof(my_list)} bytes, length = {len(my_list)}')
'''
# Method 1: Start with empty list (lots of resizing)
'''

start = time.time()
list1 = []
for i in range(1000000):
    list1.append(i)
time1 = time.time() - start

# Method 2: Pre-allocate the space
start = time.time()
list2 = [None] * 1000000
for i in range(1000000):
    list2[i] = i
time2 = time.time() - start

print(f"\nAppending to empty list: {time1:.4f} seconds")
print(f"Pre-allocated list: {time2:.4f} seconds")
print(f"Speedup: {time1/time2:.2f}x faster")


# Test 1: Create pre-allocated list with None
start = time.time()
list_with_none = [None] * 1000000
time_create = time.time() - start

# Test 2: Create empty list (no allocation yet)
start = time.time()
empty_list = []
time_empty = time.time() - start

print(f"Creating [None] * 1000000: {time_create:.4f} seconds")
print(f"Creating []: {time_empty:.6f} seconds")
'''

import time

# Scenario: Find all expenses in "Food" category
expenses_list = [
    {"category": "Food", "amount": 10},
    {"category": "Transport", "amount": 5},
    # ... imagine 10,000 more
]

# Create 10,000 expenses
expenses_list = [{"category": f"Category{i%50}", "amount": i} for i in range(10000)]

# Method 1: Search through list
start = time.time()
food_expenses = [e for e in expenses_list if e["category"] == "Category25"]
time1 = time.time() - start

# Method 2: Use dictionary grouped by category
expenses_dict = {}
for exp in expenses_list:
    cat = exp["category"]
    if cat not in expenses_dict:
        expenses_dict[cat] = []
    expenses_dict[cat].append(exp)

start = time.time()
food_expenses2 = expenses_dict.get("Category25", [])
time2 = time.time() - start

print(f"List search: {time1:.6f} seconds")
print(f"Dict lookup: {time2:.6f} seconds")
print(f"Dict is {time1/time2:.0f}x faster")