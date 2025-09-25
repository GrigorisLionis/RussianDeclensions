import random
import os
import unicodedata



# Configuration constants
CSV_FILE = "declensions.csv"
DECLENSIONS = ["NOMINATIVE", "GENITIVE", "DATIVE", "ACCUSATIVE", "INSTRUMENTAL", "PREPOSITIONAL"]
NUM_QUESTIONS = 29  # Since you're doing range(1,30) which is 29 iterations

def load_word_dictionary(file_path):
    """Load and parse the CSV file into a structured word dictionary."""
    word_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            elements = line.strip().split(",")
            if len(elements) < 6:
                continue  # Skip invalid lines
                
            word, plural_type, gender, declension, form, category = elements
            
            if word not in word_dict:
                word_dict[word] = {
                    "category": category,
                    "gender": gender,
                    "forms": {plural_type: {declension: form}}
                }
            else:
                update_word_forms(word_dict[word], plural_type, declension, form)
    
    return word_dict

def update_word_forms(word_data, plural_type, declension, form):
    """Update the forms dictionary for an existing word."""
    forms_dict = word_data["forms"]
    
    if plural_type not in forms_dict:
        forms_dict[plural_type] = {declension: form}
    else:
        forms_dict[plural_type][declension] = form

def get_random_word_and_form(word_dict):
    """Select a random word and form for quizzing."""
    word = random.choice(list(word_dict.keys()))
    word_data = word_dict[word]
    
    # Get available plural types for this word
    available_plural_types = list(word_data["forms"].keys())
    plural_type = random.choice(available_plural_types)
    declension = random.choice(DECLENSIONS)
    
    return word, word_data, plural_type, declension

def display_word_info(word, word_data, plural_type, declension):
    """Display information about the word and its forms."""
    print(f"\nWord: {word}")
    print(f"Category: {word_data['category']}")
    print(f"Gender: {word_data['gender']}")
    print(f"Plural Type: {plural_type}")
    print(f"Declension: {declension}\n")

def display_all_forms(word_data, plural_type):
    """Display all available forms for the selected plural type."""
    print("\nAll forms for this plural type:")
    forms = word_data["forms"][plural_type]
    
    for declension in DECLENSIONS:
        form=forms[declension]
        declension_padded = declension.ljust(15)  # Better than manual spacing
        print(f"{declension_padded} {form}")

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


def run_quiz(word_dict, num_questions):
    """Run the main quiz loop."""
    answers=[]
    for question_num in range(num_questions):
        word, word_data, plural_type, declension = get_random_word_and_form(word_dict)
        
        # Display the question
        display_word_info(word, word_data, plural_type, declension)
        
        # Get user input
        user_answer = input("Enter the form: ")

        
        # Show correct answer
        correct_form = word_data["forms"][plural_type].get(declension, "N/A")

        #check
        if (user_answer==strip_accents(correct_form)):
           print ("Correct!")
           continue


        print(f"Correct answer: {correct_form}")
        print(f"Correct answer: {strip_accents(correct_form)}")
        print(f"Your answer: {user_answer}")
        
        #make string
        current_answer=word+","+plural_type+","+declension+","+correct_form+","+user_answer        
        answers.append(current_answer)

        # Show all forms for reference
        display_all_forms(word_data, plural_type)
        
        # Wait for user to continue
        input("\nPress Enter to continue...")
        os.system("clear")
    return(answers)
def main():
    """Main function to run the application."""
    try:
        word_dict = load_word_dictionary(CSV_FILE)
        print(f"Loaded {len(word_dict)} words from dictionary")
        
        answers=run_quiz(word_dict, NUM_QUESTIONS)
        print(answers)
    except FileNotFoundError:
        print(f"Error: File '{CSV_FILE}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
