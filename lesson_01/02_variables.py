# 🐍 Lesson 3 — Understanding Variables More Deeply
# Before we move on, I want you to understand something important.

# When you write:
name = "Israfil"

# Python doesn't really mean:
# "Create a box called name containing the text."

# A better mental model is:
# name ───────────► "Israfil"

# The variable name refers to an object.

# Similarly:
# age = 25

# conceptually:
# age ────────────► 25

# And you can change what a variable refers to:
age = 25
age = 26

print(age)


# Output:
# 26

# The old value isn't "changed" by the variable. The name age now refers to another integer object.

# We'll eventually learn why this distinction matters when you work with lists, objects, tensors, and neural networks.


# 🔥 Variables can also be used in calculations
age = 25
next_year = age + 1
print(next_year)


# Output:
# 26

# Or:
x = 10
y = 20
result = x + y
print(result)


# Output:
# 30

# Python can perform:
# +    addition
# -    subtraction
# *    multiplication
# /    division

# and we'll learn the other operators shortly.