import time
import math
import statistics

def calc_count(numbers):
    """Calculates the sum of all list of numbers

        Parameters:
        numbers(int): a list of numbers

        Returns:
        int: the sum of all the numbers of a list

    """
    return len(numbers)

def calc_mean(numbers):
    """Calculates the mean of all list of numbers

        Parameters:
        numbers(int): a list of numbers

        Returns:
        int: the mean of all the numbers in a list

    """
    size = len(numbers)
    num_sum = sum(numbers)
    if num_sum > 0:
        return num_sum/size

def calc_median(numbers):
    """Calculates the median of all list of numbers

        Parameters:
        numbers(int): a list of numbers

        Returns:
        int: the median of all the numbers in a list

    """
    sorted_num = sorted(numbers)
    l = len(sorted_num)
    mid = l // 2
    return (sorted_num[mid] + sorted_num[mid - 1]) / 2 if l % 2 == 0 else sorted_num[mid]

def calc_mode(numbers):
    """Calculates the mode of all list of numbers

        Parameters:
        numbers(int): a list of numbers

        Returns:
        int: the mode of all the numbers in a list

    """
    words_seen = {}
    for num in numbers:
        words_seen[num] = words_seen.get(num, 0) + 1

    mode_values = numbers[0]
    for key, value in words_seen.items():
        if value > words_seen.get(mode_values):
            mode_values = key

    return mode_values

def calc_sd(numbers):
    """Calculates the standard deviation of all list of numbers

        Parameters:
        numbers(int): a list of numbers

        Returns:
        int: the sd of all the numbers in a list

    """
    return math.sqrt(round(calc_vd(numbers), 5))

def calc_vd(numbers):
    """Calculates the variance of all list of numbers

        Parameters:
        numbers(int): a list of numbers

        Returns:
        int: the variance of all the numbers in a list

    """
    n = len(numbers)
    if n <= 1:
        return 0
    mean = round(calc_mean(numbers),7)
    sq_diff = [(x - mean) ** 2 for x in numbers]
    variance = sum(sq_diff) / (n - 1)
    return variance

def read_numbers(filename):
    """Reads numbers in file provided by user"""
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                try:
                    num = float(line)
                    numbers.append(num)
                except ValueError:
                    print(f"Error of value in: {line_number}")
    except FileNotFoundError:
        print(f"Error: File not found in path: {filename}")
    return numbers

def write_answers(
        count,
        mean,
        median,
        mode,
        sd,
        var,
        elapse_time
):
    """Writes answer in file"""
    file_path = 'StatisticsResults.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Count: {count}\n")
        file.write(f"Mean: {mean}\n")
        file.write(f"Median: {median}\n")
        file.write(f"Mode: {mode}\n")
        file.write(f"Standard Deviation: {sd}\n")
        file.write(f"Variance: {var}\n")
        file.write(f"Compute Time: {elapse_time}\n")

def main():
    """Computes Statistics"""
    filename = input("")
    try:
        start_time = time.time()

        numbers = read_numbers(filename)
        print(numbers)
        count = round(calc_count(numbers),7)
        mean = round(calc_mean(numbers),7)
        median = round(calc_median(numbers),7)
        mode = round(calc_mode(numbers), 7)
        sd = round(calc_sd(numbers), 7)
        var = round(calc_vd(numbers), 5)
        end_time = time.time()

        lb_var = statistics.variance(numbers)
        lb_sd = statistics.stdev(numbers)
        elapse_time = end_time - start_time

        print(f"Count: {count}\n")
        print(f"Mean: {mean}\n")
        print(f"Median: {median}\n")
        print(f"Mode: {mode}\n")
        print(f"Standard Deviation: {sd}\n")
        print(f"Variance: {var}\n")
        print(f"Compute Time: {elapse_time}\n")

        print(f"Library Variance: {lb_var}")
        print(f"Library SD: {lb_sd}")

        write_answers(count,
                      mean,
                      median,
                      mode,
                      sd,
                      var,
                      elapse_time)

    except FileNotFoundError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
