import openai
import sys

# Set up your OpenAI API key
with open('api_key.txt', 'r') as file:
    file_contents = file.read()
openai.api_key = file_contents

if len(sys.argv) < 2:
    raise ValueError("Please provide the question_topic as an argument.")
question_topic = sys.argv[1]

print("Running API Question Generator")

# Define the system prompt
system_prompt = """
You are an expert Python question generator focused on creating high-quality questions of varying difficulty to teach students. 
The user prompt will specify the type of question, relative difficulty level (1-10, where 1 is the easiest), and question topic. 
Diversify the question subtypes or methods used within a particular question category. Ensure each part has only one unambiguous correct answer. 
Maintain a high standard of question quality, ensuring clarity, precision, and proper grammar. The output for the drag and drop questions should be a JSON with the following format:  
{
    "title": "Select the correct answer",
    "multipleResponses": true,
    "multipleResponseVariant": true,
    "blocks": [
        {
            "type": "info",
            "text": "Informational text about the question."
        },
        {
            "type": "question1",
            "correctValue": "correct_value",
            "text": "Question text with a blank space ___"
        },
        {
            "type": "question2",
            "correctValue": "correct_value",
            "text": "Question text with a blank space ___"
        }
    ],
    "answers": [
        {
            "text": "reply",
            "correctType": "question1"
        },
        {
            "text": "reply",
            "correctType": "question2"
        }
    ]
}
"""

# Define the user prompt
user_prompt = f"""
Create 10 drag and drop questions about {question_topic}. Where each drag and drop question increments by 1 in difficulty, going from 1 to 10. Respond with the questions formatted as JSON objects.
"""

# Make the API request
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    max_tokens=2048,
    n=1,
    temperature=0.5
)

# Get the API response
api_output = response.choices[0].message["content"].strip()

# Create a text file and export the API's output to that file
output_filename = "DNDQ_Generated.txt"
with open(output_filename, "w") as file:
    file.write(api_output)

print(f"The API output has been written to {output_filename}.")
