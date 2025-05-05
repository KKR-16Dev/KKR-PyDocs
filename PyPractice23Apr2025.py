# explain the difference between __str__ and __repr__ in Python?


# ChatGPT said:
# In Python, __str__ and __repr__ are both special methods used to define how an object is represented as a string. However, 
# they serve slightly different purposes:

# __str__: User-Friendly Representation

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person named {self.name}"

p = Person("Alice")
print(p)  # Output: Person named Alice


# __repr__: Developer/Debug-Friendly Representation

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person('{self.name}')"

p = Person("Alice")
print(repr(p))  # Output: Person('Alice')

# Call by Value 

def call_by_value(x):
    result = list(map(lambda i: i * 2, range(x)))
    print(result)
    return result

def modify_value(x):
    x = x * 2
    print("Inside function:", x)
a = 10
modify_value(a)
print("Outside function:", a)

# Inside function: 20
# Outside function: 10


# Call by Reference

def modify_list(lst):
    lst.append(100)
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)

# Inside function: [1, 2, 3, 100]
# Outside function: [1, 2, 3, 100]


varx = [1,0,1,1,1,0,1,0,6,2,9,3]
new_list = []
for rec in varx:
    if rec not in new_list:
        new_list.append(rec)
print(new_list)

n = len(new_list)
for i in range(n):
    for j in range(0, n-i-1):
        if new_list[j] > new_list[j+1]:
            new_list[j],new_list[j+1] = new_list[j+1], new_list[j]       
print(new_list)


