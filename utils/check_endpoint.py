import requests
import os
import re
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = os.getenv("GEMINI_API_URL")
key = os.getenv("GEMINI_API_KEY")

import google.generativeai as genai

genai.configure(api_key=key)


def check_algorithm(file_path):

    with open(file_path, "r") as file:
        content = file.read()
    # Define the instruction statement
    instruction = "Evaluate this algorithm and give me response in json with two values { status : True or False, feedback : other info } and keep feedback very brief and relevant, json output is must, if file content is blank or not relevant then also give very brief json output"
    # payload = {"instruction": instruction, "algorithm": content}
    model = genai.GenerativeModel("tunedModels/algometertune01-mpzjrjamdczj")

    try:
        response = model.generate_content(instruction + "/n" + content)
        # Extract the relevant data (text content)
        text_content = response._result.candidates[0].content.parts[0].text

        # Regular expression to match and clean only the JSON portion
        json_match = re.search(r"\{.*\}", text_content, re.DOTALL)

        # Parse the JSON string to a Python dictionary
        parsed_response = json.loads(json_match.group(0))

        # # Extract the desired values
        # status = parsed_response["status"]
        # feedback = parsed_response["feedback"]

        # print("--------- Result for input Algorithm ------ ")
        # print(f"Status : {status}")
        # print(f"Other Feedback :{feedback}")

        # return parsed_response
        print(text_content)

    except requests.exceptions.RequestException as e:
        print({"error": str(e)})
        return {"error": str(e)}


if __name__ == "__main__":
    file_path = "/home/yash/Internship/Algo_meter/input/Sample_04.txt"
    check_algorithm(file_path)
