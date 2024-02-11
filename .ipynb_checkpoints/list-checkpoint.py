
# ---

my_list = ["cat", 101, 12.9878, "dogs"]

#Counting the comma instead of data 

my_element = my_list[1:3]
print(f"my_list[1:3] = {my_element}")

my_element = my_list[1:-1]
print(f"my_list[1:-1] = {my_element}")

my_element = my_list[1:4]
print(f"my_list[1:4] = {my_element}")

my_element = my_list[1: ]
print(f"my_list[1: ] = {my_element}")

my_element = my_list[ : ]
print(f"my_list[ : ] = {my_element}")


# -------


# Adding to list 

my_list = ["cat", "dogs"]
my_list.append("rat")

my_list[1] = ["rat"]
print(my_list)

my_list.insert(1, "rat")
print(my_list)


# ----
