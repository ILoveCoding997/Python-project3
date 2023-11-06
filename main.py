# Mad Libs Generator

list = [1, 2, 3, 4, 5]
list[0] = input("Enter a name: ")
list[1] = input("Enter a number: ")
list[2] = input("Enter an adjective: ")
list[3] = input("Enter an animal(plural): ")

# Insert words into final string

text = f"Hi there! My name is {list[0]} and I am {list[1]} years old. I like to eat {list[2]} {list[3]}."
print(text)
