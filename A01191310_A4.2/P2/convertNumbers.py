import time

def convert_to_binary(number):
    """Converts numbers to binary"""
    if number == 0:
        return '0'

    binary = ''

    if number < 0:
        binary += '-'
        number = abs(number)

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2

    return binary

def convert_to_hexadecimal(number):
    """Converts numbers to hexadecimal"""
    if number == 0:
        return '0'
    hex_chars = "0123456789ABCDEF"
    hexa_decimal = ''

    if number < 0:
        hexa_decimal += '-'
        number = abs(number)

    while number > 0:
        remainder = number % 16
        hexa_decimal = hex_chars[remainder] + hexa_decimal
        number //= 16

    return hexa_decimal

def converter(numbers):
    """Converts numbers to binary and hexadeciaml"""
    results = []
    print("Number, Binary, Hexa")
    for num in numbers:
        num_binary = convert_to_binary(num)
        num_hexa = convert_to_hexadecimal(num)
        print(num, num_binary, num_hexa)
        results.append([num, num_binary, num_hexa])
    return results


def read_numbers(filename):
    """Reads numbers in file provided by user"""
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                try:
                    num = int(line)
                    numbers.append(num)
                except ValueError:
                    print(f"Error of value in: {line_number}")
    except FileNotFoundError:
        print(f"Error: File not found in path: {filename}")
    return numbers

def write_answers(results, elapse_time):
    """Writes answer in file"""
    file_path = 'ConvertionResults.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Num - Bin - Hex\n")
        for res in results:
            num = res[0]
            bin_n = res[1]
            hex_n = res[2]
            file.write(f"{num} - {bin_n} - {hex_n} \n")
        file.write(f"Elapsed-Time: {elapse_time}")

def main():
    """Computes Statistics"""
    filename = input("")
    try:
        start_time = time.time()

        numbers = read_numbers(filename)
        print(numbers)
        end_time = time.time()
        elapse_time = end_time - start_time
        results = converter(numbers)
        write_answers(results, elapse_time)
        print(f"Elapsed Time: {elapse_time}")


    except FileNotFoundError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
