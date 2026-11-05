# 🐍 Lesson 4 — Python Operators
# Now we're going to properly learn operators.

# An operator performs an operation on values.

x = 10
y = 3

print(x + y)  # addition
print(x - y)  # subtraction
print(x * y)  # multiplication
print(x / y)  # division
print(x // y)  # floor division
print(x % y)  # modulus (remainder)
print(x ** y)  # exponentiation


# this one is important to understand:
print(10 % 3) # modulus operator give the remainder of the division


# 3 x 3 = 9

# 10 - 9 = 1

#Therefore, 10 % 3 = 1

number = 10
remainder = number % 2
print(remainder)  # 0 if even, 1 if odd


# 🔥 Operator precedence
# Python also follows mathematical order of operations.

result = 10 + 5 * 2  # multiplication is done first
print(result)  # 20

result = (10 + 5) * 2  # parentheses change the order
print(result)  # 30


# Operator precedence in Python is as follows:
# ()
#  ↓
# **
#  ↓
# *, /, //, %
#  ↓
# +, -