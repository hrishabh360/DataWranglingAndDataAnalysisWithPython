words = ["Hello", "Python"]

for i in words:
    print(i)

for word in words:
    for count in range(3):
        print(word)

for word in enumerate(words):
    print(word)

for i, word in enumerate(words):
    print(f"Item {i} is {word}")


# -----

phrase = "Hello Python"

for i in phrase:
    print(i)

# -----

i = 1
j = 1

height = 5
width = 5

for i in i is <= height:
    for j in j is <= width:
        print("*")
        j+1
    print("\n")          
    i+1
    
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

#-----


