from Practice import dictionary_generator

# Gives user choices on French topics
def French_options():
    print("\nWelcome to the French Flashcards!\n Select an option below, to choose, type the number (ex. '1'):\n")
    print("1. Number Practice\n2. Color Practice\n3. Home\n")

    user_input = input("\nType here: ")
    answer_language = "French"

    if user_input == "1":
        topic = " Numbers practice"
        text_file = "Text Files\French\French Numbers.txt"
        dictionary_generator(text_file, answer_language, topic)

    elif user_input == "2":
        topic = " Colors practice"
        text_file = "Text Files\French\French Colors.txt"
        dictionary_generator(text_file, answer_language, topic)

    elif user_input == "3":
        start()

    else:
        print("Please enter a valid option.")
        French_options()

# Gives user choices on Spanish topic
def Spanish_options():
    print("\nWelcome to the Spanish Flashcards!\n Select an option below, to choose, type the number (ex. '1'):\n")
    print("1. Number Practice\n2. Colors\n3. Home\n")

    user_input = input("\nType here: ")
    answer_language = "Spanish"

    if user_input == "1":
        topic = " Numbers practice"
        text_file = "Text Files\Spanish\Spanish Numbers.txt"
        dictionary_generator(text_file, answer_language, topic)

    elif user_input == "2":
        topic = " Colors practice"
        text_file = "Text Files\Spanish\Spanish Colors.txt"
        dictionary_generator(text_file, answer_language, topic)

    elif user_input == "3":
        start()

    else:
        print("Please enter a valid option.")
        Spanish_options()

# Starts program
def start():
    print("\nWelcome to Flashcards!\n Select an option below, to choose, type the number (ex. '1'):\n")
    print("1. French Flashcards\n2. Spanish Flashcards\n")

    user_input = input("\nType here: ")

    if user_input == "1":
        French_options()

    elif user_input == "2":
        Spanish_options()
    
    else:
        print("Please enter a valid option.")
        start()

if __name__ == "__main__":
    start()
