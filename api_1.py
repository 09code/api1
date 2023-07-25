import requests
import csv
import json

api_url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(api_url)
api_data = response.json()

# Convert the JSON data to text representation
api_data_text = json.dumps(api_data, indent=4)

text_file_name = "api_data.txt"
with open(text_file_name, mode='w', encoding='utf-8') as file:
    file.write(api_data_text)

print("Data converted to text and saved into '{}' successfully.".format(text_file_name))
