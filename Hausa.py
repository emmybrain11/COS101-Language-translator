# Hausa Dictionary Program

hausa_dictionary = {
    "sannu": "hello",
    "nagode": "thank you",
    "eh": "yes",
    "a'a": "no",
    "ruwa": "water",
    "abinci": "food",
    "gida": "house",
    "mutum": "person",
    "yaro": "boy/child",
    "yarinya": "girl",
    "makaranta": "school",
    "littafi": "book",
    "kudi": "money",
    "aiki": "work",
    "kashe": "turn off / kill",
    "kunna": "turn on",
    "tafiya": "journey / walking",
    "zuwa": "to go",
    "dare": "night",
    "rana": "day"
}

# User input
word = input("Enter a Hausa word: ").lower()

# Check and display meaning
if word in hausa_dictionary:
    print("Meaning:", hausa_dictionary[word])
else:
    print("Word not found in dictionary.")
