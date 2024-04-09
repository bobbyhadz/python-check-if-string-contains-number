# Check if a string contains a number in Python

def contains_number(string):
    return any(char.isdigit() for char in string)


print(contains_number('abc123'))  # 👉️ True
print(contains_number('abc'))  # 👉️ False
print(contains_number('-1abc'))  # 👉️ True

if contains_number('abc123'):
    # 👇️ this runs
    print('The string contains a number')
else:
    print('The string does NOT contain a number')

# -----------------------------

# ✅ check if a string contains a specific number

print('123' in 'abc123')  # 👉️ true
print('567' in 'abc123')  # 👉️ False