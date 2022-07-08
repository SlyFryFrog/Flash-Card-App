import random

# Sets default variables
def dictionary_generator(text_file, answer_language, topic):
    dictionary = {}

    # Opens the file and creates a dictionary of the numbers and their corresponding words
    with open(text_file, encoding='utf-8') as file:
        # Creates a list of the data in the file
        for line in file:
            # Prevents the program from stopping if there is a blank line in the file
            if line == '\n':
                continue
            key, val = line.split(", ")
            
            dictionary[key] = val.strip()

    practice_generator(dictionary, answer_language, topic)


def practice_generator(dictionary, answer_language, topic):
    print(f"\nWelcome to the {answer_language + topic}!\nEnter the amount you would like to practice, or enter 'All' to practice everything in the topic. \n")
    number_range = input("Type here: ")

    if number_range.isdigit():
        # Creates a list of numbers to practice
        question = list(dictionary.keys())
        random.shuffle(question)
        del question[int(number_range):]

        return practice(question, dictionary, answer_language, topic)

    elif number_range == "All":
        question = list(dictionary.keys())
        random.shuffle(question)
        
        return practice(question, dictionary, answer_language, topic)
        
    else:
        print("Please enter a number.")
        practice_generator(dictionary, answer_language, topic)


def practice(question, dictionary, answer_language, topic):
    # Creates a question for the user to answer
    for num in question:
        user_answer = input(f"\nType {num} in {answer_language} -- ")
        # Checks to see if the user's answer is correct
        if dictionary[num] == user_answer:
            print("Correct!")
        else:
            print(f"Incorrect, the answer is {dictionary[num]}")
    user_input = input(f"\nYou have finished {topic}!\nWould you like to repeat the topic? (y/n): ")

    if user_input == "y":
        practice_generator(dictionary, answer_language, topic)
        
    else:
        exit()
