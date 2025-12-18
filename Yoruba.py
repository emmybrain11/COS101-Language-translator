yoruba_dictionary = {
    "baba": "Father",
    "iya": "Mother",
    "omo": "Child",
    "Ile": "House",
    "ounje": "food",
    "omi": "water",
    "owo": "money",
    "iwe": "book",
    "aso": "cloth",
    "bata": "shoe",
    "ise": 'work',
    "ore": "friend",
    "ojo": "rain",
    "ina": "fire",
    "aja": "dog",
    "ologbo": "cat",
    "oko": "farm",
    "oba": "king",
    "igbese": "step",
    "ayo": "joy"
}
print("YORUBA DICTIONARY")
print("_________________")

word = input("Enter a Yoruba word:").capitalize()

print(f"yhe meaning of '[word]' is:{yoruba_dictionary[word]}")
print("sorry, word not found in the dictionary.")