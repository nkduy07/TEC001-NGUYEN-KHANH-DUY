def count_lines(file_path):
    count = 0

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() != "":
                count += 1
    return count

