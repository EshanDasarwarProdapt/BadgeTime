#used to count the occurrences of each element in a list
from collections import Counter

# l = ["apple", "banana", "apple", "orange", "banana", "apple"]
# counter = Counter(l)

# print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# d = {}

# for i in l:
#     d[i] = d.get(i,0) + 1

# print(d)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# from collections import namedtuple

# student = namedtuple("Student", ["name", "age", "grade"])

# s1 = student("Ravi", 20, "A")

# print(s1.name)  # Output: Ravi
# print(s1.age)   # Output: 20    
# print(s1.grade) # Output: A

# from collections import deque

# dq = deque([1, 2, 3, 4, 5])
# dq.append(6)  # Add to the right
# dq.appendleft(0)  # Add to the left
# print(dq)  # Output: deque([0, 1, 2, 3, 4, 5, 6])

from collections import ChainMap

student = {"name": "Ravi", "age": 20}

course = {"course": "Python", "duration": "3 months"}

combined = ChainMap(student, course)
print(combined)
print(combined["name"])  # Output: Ravi
print(combined["course"])  # Output: Python

