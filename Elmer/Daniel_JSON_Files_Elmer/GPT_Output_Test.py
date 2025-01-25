import json
import os
import random

# Complete path to the JSON file
json_path = r"C:\Users\matth\OneDrive\Desktop\GPT_Output_Test\AI_Gamification_Python\Elmer\Daniel_JSON_Files_Elmer\Quizzes\M1_Q1_Main.json"


# Function to load the JSON file
def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in the file {file_path}.")
        return None


# Function to select a random file that begins with "Question"
def select_random_question_file(directory):
    # List all files in the directory that start with "Question"
    question_files = [f for f in os.listdir(directory) if f.startswith("Question")]

    if question_files:
        # Select a random file from the list
        selected_file = random.choice(question_files)
        return selected_file
    else:
        print("No files starting with 'Question' found in the directory.")
        return None


# Load the JSON file
data = load_json(json_path)

# If data is loaded, proceed with selecting a random "Question" file
if data:
    print("Data loaded successfully.")
    print(data)

    # Get the directory where the "Question" files are located
    question_files_directory = r"C:\Users\matth\OneDrive\Desktop\GPT_Output_Test\AI_Gamification_Python\Elmer\Daniel_JSON_Files_Elmer"

    # Select a random "Question" file from the directory
    selected_file = select_random_question_file(question_files_directory)

    if selected_file:
        print(f"Randomly selected file: {selected_file}")