import time

def count_words(words):
    """Count number of words on a list"""
    words_seen = {}
    for num in words:
        words_seen[num] = words_seen.get(num, 0) + 1

    sorted_words = dict(sorted(words_seen.items(), key=lambda item: item[1]))
    return sorted_words

def read_words(filename):
    """Reads numbers in file provided by user"""
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                try:
                    word = str(line)
                    words.append(word)
                except ValueError:
                    print(f"Error of value in: {line_number}")
    except FileNotFoundError:
        print(f"Error: File not found in path: {filename}")
    return words

def write_answers(words_count, elapse_time):
    """Writes answer in file"""
    file_path = 'WordCountResults.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Word - Count\n")
        for key, value in words_count.items():
            file.write(f"{key} - {value} \n")
            print(f"{key} - {value}")
        file.write(f"Elapsed-Time: {elapse_time}")

def main():
    """Computes Statistics"""
    filename = input("")
    try:
        start_time = time.time()

        words = read_words(filename)
        print(words)
        end_time = time.time()
        elapse_time = end_time - start_time
        results = count_words(words)
        write_answers(results, elapse_time)
        print(f"Elapsed Time: {elapse_time}")


    except FileNotFoundError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
