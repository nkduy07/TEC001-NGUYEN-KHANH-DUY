import random

def estimate_pi():
    try:
        total_points = int(input("Enter the number of random points: "))
        if total_points <= 0:
            print("Please enter a positive integer.")
            return

        points_inside_circle = 0

        for i in range(total_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

            if x ** 2 + y ** 2 < 1:
                points_inside_circle += 1

        pi_approximation = 4 * points_inside_circle / total_points

        print(f"Approximated value of pi: {pi_approximation}")

    except ValueError:
        print("Invalid input! Please enter a numeric integer value.")


if __name__ == "__main__":
    estimate_pi()