import sys
import nltk
import noun_extract



def main(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found.")
        return

    sorted_proper_nouns = noun_extract.extract_noun_count(text)

    # Print the sorted list of proper nouns
    print("Unique proper nouns sorted by frequency:")
    for proper_noun, count in sorted_proper_nouns:
        print(f"{proper_noun}\t{count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nount_count.py <file_name>")
    else:
        file_name = sys.argv[1]
        main(file_name)