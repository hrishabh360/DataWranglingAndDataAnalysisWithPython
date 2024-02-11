# with open("data.txt") as f:
#     for line in f:
#         print(line, end="") # end is supressing the new line from print statement


# with open("data.txt") as f:
#     for line in f:
#         line = line.strip()
#         print(line * 2) #This will treat line as string 


with open("data.txt") as f:
    for line in f:
        line = line.strip()
        line= int(line)
        print(line * 2)
