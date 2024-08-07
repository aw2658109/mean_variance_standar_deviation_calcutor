import numpy as np


def calculate_stats(numbers):

    mean = np.mean(numbers)
    variance = np.var(numbers)
    std_deviation = np.std(numbers)

    return {
        'mean': mean,
        'variance': variance,
        'std_deviation': std_deviation
    }


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    stats = calculate_stats(numbers)

    # Display the results
    print("Mean:", stats['mean'])
    print("Variance:", stats['variance'])
    print("Standard Deviation:", stats['std_deviation'])
