def calculate_average(file):
    total_score = 0
    with open(file, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 2:
                score = float(parts[1])
                total_score += score
                count += 1
                average_score = total_score / count
    return average_score
