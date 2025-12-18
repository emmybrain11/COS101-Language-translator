# Igbo Dictionary Program

igbo_dictionary = {
    "ndewo": "hello",
    "daalu": "thank you",
    "ee": "yes",
    "mba": "no",
    "mmiri": "water",
    "nri": "food",
    "ulo": "house",
    "mmadu": "person",
    "nwoke": "man",
    "nwanyi": "woman",
    "akwukwo": "book",
    "ulo akwukwo": "school",
    "ego": "money",
    "oru": "work",
    "ije": "journey / walking",
    "bia": "come",
    "ga": "go",
    "ubochi": "day",
    "abali": "night",
    "enyi": "friend"
}

# User input
word = input("Enter an Igbo word: ").lower()

# Check and display meaning
if word in igbo_dictionary:
    print("Meaning:", igbo_dictionary[word])
else:
    print("Word not found in dictionary.")

