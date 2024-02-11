sounds = {
    "goat": "cr7cr7cr7",
    "cat": "meow",
    "dog": "woof",
    "duck": "quack",
    "sheep": "baaaa"
}

# sound = sounds["cat"]

# sounds["tiger"] = "roarr"
# sound = sounds["tiger"]

#why [] while calling dict ?? -- bcoz

sounds["tigger"] = "roarr"
sounds["tiger"] = sounds["tigger"]

print(sounds)

del sounds["tigger"]

sound = sounds["tiger"]
print(sounds)

# ----
# Dict ft. loop

sounds = {
    "goat": "cr7cr7cr7",
    "cat": "meow",
    "dog": "woof",
    "duck": "quack",
    "sheep": "baaaa",
    "tiger": "roarr"
}

for thing in sounds:
    print(thing)


for sound in sounds.values():
    print(sound)

for sound in sounds.keys():
    print(sound)

for sound in sounds.items():
    print(sound)

for animal, sound in sounds.items():
    print(animal, "GOES", sound)

#---


# Assigining multiple values to key

sounds = {
    "goat": "cr7cr7cr7",
    "cat": "meow",
    "dog": "woof",
    "duck": "quack",
    "sheep": "baaaa"
}

sounds["Human"] = ["Hi", "Hello", "How are you ??"]


for animal, sound in sounds.items():
    if animal == "Human":
        print(animal, "sometimes says", sound[0],
             "sometimes says", sound[1],
             "sometimes says", sound[2])
    else:
        print(animal, "goes", sound)

for animal, sound in sounds.items():
    if isinstance(sound, list):
        print(animal, "sometimes says", sound[0], "\n",
             "sometimes says", sound[1], "\n",
             "sometimes says", sound[2],  "\n")
    else:
        print(animal, "goes", sound)

    