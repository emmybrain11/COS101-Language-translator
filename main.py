from yoruba import yoruba_dict
from hausa import hausa_dict
from khana import khana_dict
from igala import igala_dict
from idoma import idoma_dict

def main():
    print("WELCOME TO COS 101 LANGUAGE TRANSLATOR")
    print("------")
    print("1. Yoruba")
    print("2. Hausa")
    print("3. Khana")
    print("4. Igala")
    print("5. idoma")

    choice = input("Choose a language (1/2/3/4/5): ")
    word = input("Enter a word in English: ").lower()

    if choice == "1":
        print("Yoruba:", yoruba_dict.get(word, "Word not found"))

    elif choice == "2":
        print("Hausa:", hausa_dict.get(word, "Word not found"))

    elif choice == "3":
        print("Khana:", khana_dict.get(word, "Word not found"))

    elif choice == "4":
        print("Igala:", igala_dict.get(word, "Word not found"))
    elif choice == "5":
        print("idoma:", idoma_dict.get(word, "Word not found"))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()