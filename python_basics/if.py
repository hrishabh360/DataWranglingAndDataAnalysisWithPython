my_number =128


def ebebe(my_number):
    my_number = int(my_number) #converting my_number to int
    if my_number > 100:
        print(f"{my_number} is greater")
    elif my_number == 100:
        print(f"BINGOO")
    elif my_number == 69:
        side_eyes_emoji = "\U0001F440 \U0001F440"  # Unicode characters for side eyes
        # Print the custom-made emoji
        print(side_eyes_emoji)
    else:
        print(f"{my_number} is small")


my_number = input("Please insert number: ")

ebebe(my_number)
ebebe(12)
ebebe(122)
ebebe(100)

#----

# if ft. loop

my_numbers = range(10) # 0 to 9

for num in my_numbers:
    if num > 5:
        print(num, "is greater than 5")
    elif num < 5:
        print(num, "is less than 5")
    else:
        print(num, "is equal to 5")


# ----





