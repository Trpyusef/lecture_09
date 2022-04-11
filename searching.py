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
    wanted_indexes = set()
    for index in range(len(sequence) - len(wanted_vzor)):
        subsequence = sequence[index:(index + len(wanted_vzor))]
        same = True
        for letter_subsequence, letter_pattern in zip(subsequence, wanted_vzor):
            if letter_subsequence != letter_pattern:
                same = False
                break
        if same:
            wanted_indexes.add(index)
    return wanted_indexes

def binary_search(sequence, wanted_number):
    middle_index = (len(sequence)-1)/2
    left_margain = sequence[0]
    right_margain = sequence[-1]
    wanted_index = 0
    same = False
    while True:
        if number[middle_index] == wanted_number:
            wanted_index = wanted_index + middle_index
        elif number[middle_index] < wanted_number:
            left_margain = sequence[middle_index + 1]




def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)
    wanted_number = 2
    linear_search(unordered_numbers, wanted_number)
    print(linear_search(unordered_numbers, wanted_number))
    print(pattern_search(read_data("sequential.json", "dna_sequence"), "AA"))
    print(binary_search(read_data("sequential.json", "ordered_numbers"), 47))
if __name__ == '__main__':
    main()