# Spanish Dictionary Program

spanish_dictionary = {
    "hola": "hello",
    "gracias": "thank you",
    "si": "yes",
    "no": "no",
    "agua": "water",
    "comida": "food",
    "casa": "house",
    "persona": "person",
    "hombre": "man",
    "mujer": "woman",
    "libro": "book",
    "escuela": "school",
    "dinero": "money",
    "trabajo": "work",
    "ir": "to go",
    "4venir": "to come",
    "caminar": "walk",
    "dia": "day",
    "noche": "night",
    "amigo": "friend"
}

word = input("Enter a Spanish word: ").lower()

if word in spanish_dictionary:
    print("Meaning:", spanish_dictionary[word])
else:
    print("Word not found.")
