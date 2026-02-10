# Understanding Data Structures

## What is this?

Hands-on learning for how data structures actually work in Python - not just how to use them, but **why** they exist and **when** to use each one.

**Approach:** Experiment, measure, understand.

---

## What I've Learned

### Lists - Memory Allocation (Feb 10, 2026)

**Key discovery:** Lists don't grow 1 item at a time - Python over-allocates to avoid constant resizing.

**Experiments in `understanding_lists.py`:**
- Measured how lists grow in memory
- Python resizes at specific points, not every append
- Tested append vs pre-allocation performance

**What I learned:**
1. Lists over-allocate memory for efficiency
2. Appending is faster than pre-allocating (counterintuitive!)
3. Pre-allocation only helps when you need random access during construction
4. For small datasets (<1000 items), differences are negligible

**When to use lists:**
- Default for ordered collections
- Adding items sequentially
- Need to maintain order
- Duplicates allowed

---

### Dictionaries - Hash Tables (Feb 10, 2026)

**Key discovery:** Dicts provide instant lookup using hashing, lists require iteration through everything.

**Experiments:**
- Compared searching 10,000 items: list vs dict
- Dict lookup was ~131x faster
- Learned about hash functions and direct memory access

**What I learned:**
1. Lists = O(n) search (check every item)
2. Dicts = O(1) lookup (direct access via hash)
3. Tradeoff: Dicts use more memory, keys must be unique
4. Optimization matters at scale, not for small datasets

**When to use dicts:**
- Fast lookup by key
- Grouping data by category/ID
- Counting occurrences
- Frequent "does X exist?" checks

**When to use lists:**
- Need order
- Need duplicates
- Simple sequential access
- Small dataset where performance doesn't matter

---

## Real Application: My Budget Tracker

**Current:** List of expense objects
- Simple and clear
- Fast enough for ~20-50 expenses
- No premature optimization

**When dict would make sense:**
- Restaurant with hundreds of daily transactions
- Need instant category totals
- Frequent category filtering
- Performance becomes noticeable

**Decision:** Stick with lists. Optimize when needed, not before.

---

## Learning Principles

1. **Measure, don't guess** - Run experiments
2. **Context matters** - "Best" depends on use case
3. **Understand tradeoffs** - Every structure has pros/cons
4. **Avoid premature optimization** - Readable code first
5. **Learn through real problems** - Connect theory to actual code

---

## Next Topics

- [ ] Hash collisions
- [ ] Why can't all objects be dict keys?
- [ ] Sets - when to use
- [ ] Java comparison - ArrayList vs HashMap
- [ ] Big O notation
- [ ] Memory profiling

---

## Running Experiments
```bash
cd data-structures-applied
python understanding_lists.py
```

---

*Updates as I learn more*