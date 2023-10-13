#You can use double or single quotes:
print("Hello")
print('Hello')

a = "Hello"
print(a)

#You can assign a multiline string to a variable by using three quotes or single three quotes:
a = """Hello World,
Good Morning,
Python is awesome,
Fortnite on top."""
print(a)

a = '''Hello World,
Good Morning,
Python is awesome,
Fortnite on top.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "fortnite":
  print(x) 

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
