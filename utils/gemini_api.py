import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def check_algorithm(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Define the instruction statement
    instruction = "Evaluate this algorithm and give me response in json with two values { status : True or False, feedback : other info }"

    payload = {"instruction": instruction, "algorithm": content}

    headers = {
        "Authorization": f'Bearer {os.getenv("GEMINI_API_KEY")}',
        "Content-Type": "application/json",
    }

    gemini_api_url = os.getenv("GEMINI_API_URL")

    try:
        response = requests.post(gemini_api_url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
