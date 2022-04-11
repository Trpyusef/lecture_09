import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
        if field in set(data.keys()):
            return data[field]


def linear_search(sequence, wanted_number):
    positions = []
    count = 0
    for index, number in enumerate(sequence):
        if number == wanted_number:
            count = count + 1
            positions.append(index)
    output = dict()
    output["positions"] = positions
    output["count"] = count
    return output


def pattern_search(sequence, wanted_vzor):
    wanted_indexes = []
    for index in range(len(sequence) - len(wanted_vzor)):
        if sequence[index:index+ len(wanted_vzor)] == wanted_vzor:
            wanted_indexes.append(index)
    return wanted_indexes




def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)
    wanted_number = 2
    linear_search(unordered_numbers, wanted_number)
    print(linear_search(unordered_numbers, wanted_number))
    print(pattern_search(read_data("sequential.json", "dna_sequence"), "AA"))
if __name__ == '__main__':
    main()