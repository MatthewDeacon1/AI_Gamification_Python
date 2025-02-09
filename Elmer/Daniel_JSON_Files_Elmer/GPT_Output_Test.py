import json
import os
import random

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the paths dynamically
json_path = os.path.join(script_directory, "Quizzes", "M1_Q1_Main.json")
question_files_directory = os.path.join(script_directory)


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
    try:
        question_files = [f for f in os.listdir(directory) if f.startswith("Question")]
        if question_files:
            selected_file = random.choice(question_files)
            return os.path.join(directory, selected_file)
        else:
            print("No files starting with 'Question' found in the directory.")
            return None
    except FileNotFoundError:
        print(f"The directory {directory} was not found.")
        return None


# Function to adjust JSON structure to match the original format
def adjust_json_structure(data):
    for key in data:
        for item in data[key]:
            if "question" in item:
                question_content = item.pop("question")
                if "title" in question_content and question_content["title"] == "Selecciona la respuesta correcta":
                    del question_content["title"]  # Remove only the second occurrence of "title"
                item.update(question_content)  # Merge the question content into the main structure
    return data


# Function to replace the contents of M1_Q1_Main.json with the selected question file
def replace_json_content(target_path, source_path):
    source_data = load_json(source_path)
    if source_data is not None:
        adjusted_data = adjust_json_structure(source_data)
        try:
            with open(target_path, "w") as file:
                json.dump(adjusted_data, file, indent=4)
            print(f"Successfully replaced contents of {target_path} with {source_path}")
        except Exception as e:
            print(f"Error writing to {target_path}: {e}")


# Load the JSON file
data = load_json(json_path)

# If data is loaded, proceed with selecting a random "Question" file
if data:
    print("Data loaded successfully.")
    print(data)

    selected_file = select_random_question_file(question_files_directory)

    if selected_file:
        print(f"Randomly selected file: {selected_file}")
        replace_json_content(json_path, selected_file)
