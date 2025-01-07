
def wordcount(text):
    words = text.split()
    count_of = len(words)
    return count_of

def char_count(text):
    lowercase = text.lower()
    counter = {}
    for char in lowercase:
        if char not in counter:
            counter.update({char: 1})
        else:
            add_one = counter[char] + 1
            counter.update({char: add_one})    
    return counter

def report(data, count_of_words):
    # count_each_letter = data.items()
    sorted_data_list = sorted(data.items())
    readout = ""

    for key, value in sorted_data_list:
        if key.isalpha():
            readout += f"The {key} character was found {value} times\n"

    print(
        f"--- Begin report of books/frankenstein.txt ---\n"
        f"{count_of_words} words found in the document\n"
        "\n"
        f"{readout}"
        "--- End report ---"
        )
    


def main():
    with open("books/frankenstein.txt") as f:                         # Opens frankenstein.txt and closes when finished
        file_contents = f.read()                                      # file_contents = all words in file
        
        
        report(char_count(file_contents), wordcount(file_contents))

        

if __name__ == "__main__":                                            # checks if script being run from this file or imported
    main()                                                            # execute main func