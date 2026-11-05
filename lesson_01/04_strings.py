# 🐍 Lesson 5 — Strings
# Now we're going to move from numbers to text.

# A string is a sequence of characters.
name = "Israfil"

# String can be combined using the + operator:
first_name = "Israfil"
last_name = "Mallick"

full_name = first_name + " " + last_name
print(full_name)  # Israfil Mallick

# 🔢 Strings and numbers are different
# This works:
age = 25
print(age + 5)

# print("Age: " + age) # This will cause an error 


print("Age: " + str(age))


# String have positions
name = "Python"

# Python sees characters at positions called indexes:
#  P   y   t   h   o   n
#  0   1   2   3   4   5

print(name[0])
print(name[1])