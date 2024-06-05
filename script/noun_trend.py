import sys
import nltk
import noun_extract

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter

def main(keyword):
    extract_from_file("./data/IO")
    extract_from_file("./data/IOD")
    extract_from_file("./data/KC")
    extract_from_file("./data/WWDC")

def extract_from_file(file_initial):
    print(f"{file_initial} Keyword: {keyword}")
    
    for year in range(2011, 2025):
        file_name = file_initial + "-" + str(year)
        try:
            with open(file_name, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            # print("File {file_name} not found.")
            continue

        noun_count = noun_extract.extract_noun_count(text)

        try:
            count = dict(noun_count)[keyword]
            print(f"{year}\t{count}")
        except KeyError:
            continue

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python noun_trend.py <keyword>")
    else:
        keyword = sys.argv[1]
        main(keyword)