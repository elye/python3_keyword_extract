import sys
import nltk
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter

def extract_noun_count(text):
    punctuations = "!\"#$%&()*/:;<=>?@[\]^_`{|}~"
    for punct in punctuations:
        text = text.replace(punct, "").lower()

    proper_nouns = extract_proper_nouns(text)

    # Count the occurrences of each proper noun
    proper_noun_counts = Counter(proper_nouns)

    # Sort proper nouns by their counts in descending order
    sorted_proper_nouns = sorted(proper_noun_counts.items(), key=lambda x: x[1], reverse=False)

    return sorted_proper_nouns
    # # Print the sorted list of proper nouns
    # print("Unique proper nouns sorted by frequency:")
    # for proper_noun, count in sorted_proper_nouns:
    #     print(f"{proper_noun}\t{count}")

def extract_proper_nouns(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)
    
    # Filter out nouns (NN, NNS, NNP, NNPS)
    nouns = [word for word, tag in tagged_words if tag.startswith('NN')]
    
    return nouns
