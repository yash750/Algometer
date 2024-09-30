import json


def test_01(path):
    with open(path, "r") as file:
        content = file.read()

    print(len(content))
    print(type(content))


def training_data_len():
    file_path = "/home/yash/Internship/Algo_meter/input/training_data.json"

    with open(file_path, "r") as file:
        training_data = json.load(file)

    examples = training_data["Examples"]
    print(len(examples))


if __name__ == "__main__":
    path = "/home/yash/Internship/Algo_meter/input/Sample_04.txt"
    training_data_len()
