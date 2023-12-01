import re

def find_number_and_index(text, part):
    digit_map = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    indices, numbers = [], []

    search_for = [str(i + 1) for i in range(9)] + (digit_map if part == 2 else [])

    for search_term in search_for:
        occurrences = [match.start() for match in re.finditer(search_term, text)]
        indices.extend(occurrences)
        numbers.extend([digit_map.index(search_term) + 1 if search_term in digit_map else int(search_term)] * len(occurrences))

    min_index = indices.index(min(indices))
    max_index = indices.index(max(indices))

    return 10 * numbers[min_index] + numbers[max_index]

def main():
    with open("day1.in") as file:
        lines = file.readlines()

    part_1_result = sum([find_number_and_index(line, part=1) for line in lines])
    part_2_result = sum([find_number_and_index(line, part=2) for line in lines])

    print("Part 1:", part_1_result)
    print("Part 2:", part_2_result)

if __name__ == "__main__":
    main()
