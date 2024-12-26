def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return 0


# Example usage
file_path = 'example.txt'  # Replace with your file path
word_count = count_words_in_file(file_path)
print(f"The number of words in the file is {word_count}.")
